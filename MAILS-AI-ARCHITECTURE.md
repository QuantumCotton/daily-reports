# Mails.ai Architecture & From-Inbox Sending Mechanism

## Executive Summary

Mails.ai (and similar email warmup services like Warmy.io, Mailwarm, Mailreach) use a technique called **"From-Inbox Sending"** or **IMAP-based sending** rather than traditional SMTP. This allows warming emails to appear in the user's actual inbox while being automatically filtered out of the user's view.

---

## 1. What is "From-Inbox" Sending?

### Traditional SMTP vs. From-Inbox

| Method | How it Works | Email Source | User Visibility |
|--------|--------------|--------------|-----------------|
| **SMTP** | Connects to mail server's outbound port (25/587/465) | External app sends via SMTP | Sent emails appear in "Sent" folder |
| **From-Inbox (IMAP/API)** | Uses Gmail API or IMAP to inject messages into inbox | Messages appear as received emails | Emails appear in INBOX, then auto-archived/filtered |

### The Key Difference

- **SMTP**: Email goes OUT → Recipient receives → Shows in Sent folder
- **From-Inbox**: Email appears IN inbox → Auto-reply triggers → Creates thread in inbox

---

## 2. Technical Architecture

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     MAIL.AI WARMUP ENGINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐   │
│  │   Warmup     │────▶│   Gmail API  │────▶│  User Inbox  │   │
│  │   Engine     │     │   (IMAP)     │     │   (Gmail)    │   │
│  └──────────────┘     └──────────────┘     └──────────────┘   │
│         │                                          │           │
│         │                                          ▼           │
│         │                              ┌──────────────────┐   │
│         │                              │  Filter/Label    │   │
│         │                              │  "Warmup"        │   │
│         │                              │  (Auto-Archive)  │   │
│         │                              └──────────────────┘   │
│         │                                          │           │
│         ▼                                          ▼           │
│  ┌──────────────┐                       ┌──────────────────┐   │
│  │  Warmup      │◀──────Reply───────────│  Partner Inbox   │   │
│  │  Partner     │                       │  (Another user)  │   │
│  │  Network     │                       └──────────────────┘   │
│  └──────────────┘                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Core Components

1. **OAuth2 Authentication Layer**
   - Connects to user's Gmail/Outlook via OAuth2
   - Requires scopes: `https://www.googleapis.com/auth/gmail.modify`

2. **Gmail API Integration**
   - Uses `users.messages.insert()` to inject messages
   - Uses `users.drafts.create()` for draft-based sending
   - Uses `users.messages.send()` for actual sending

3. **IMAP Fallback**
   - For providers without API (Yahoo, custom domains)
   - Uses IMAP APPEND command to insert messages

4. **Filter/Label Management**
   - Creates hidden labels: `_warmup`, `_warmy_internal`
   - Auto-archives warmup emails
   - Creates Gmail filters to hide warmup threads

---

## 3. How From-Inbox Sending Works (Step-by-Step)

### Step 1: OAuth Connection
```python
# Pseudocode
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# User authorizes via OAuth2
creds = Credentials.from_authorized_user_file('token.json', 
    scopes=['https://www.googleapis.com/auth/gmail.modify'])
service = build('gmail', 'v1', credentials=creds)
```

### Step 2: Create Warmup Filter (Hidden from User)
```python
# Create a filter that auto-archives warmup emails
filter_body = {
    'criteria': {
        'from': 'warmup@partner-network.com',
        'subject': '[Warmup]'
    },
    'action': {
        'addLabelIds': ['Label_Warmup'],  # Hidden label
        'removeLabelIds': ['INBOX']  # Remove from inbox
    }
}
service.users().settings().filters().create(userId='me', body=filter_body).execute()
```

### Step 3: Inject Warmup Email via API
```python
import base64
from email.mime.text import MIMEText

def create_warmup_email(sender, to, subject, body):
    message = MIMEText(body)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

# Method A: Direct inbox injection (appears as received email)
message = create_warmup_email(
    sender='partner@warmup-network.com',
    to='user@gmail.com',
    subject='Re: [Warmup] Great to connect!',
    body='Thanks for reaching out! I saw your email...'
)

# Inject directly into inbox
service.users().messages().insert(
    userId='me',
    body=message,
    internalDateSource='dateHeader'
).execute()
```

### Step 4: Send Reply from User's Inbox
```python
# Method B: Create draft, then send (appears in Sent)
draft = service.users().drafts().create(
    userId='me',
    body={'message': message}
).execute()

# Send the draft
service.users().drafts().send(
    userId='me',
    body={'id': draft['id']}
).execute()
```

---

## 4. The "Long Email Chain" Concept

### What It Is

The "long email chain" is a technique where:
1. Initial warmup email is injected into inbox
2. User's account auto-replies (via API)
3. Partner account replies back
4. This creates a **thread** with 10-50+ replies
5. Each reply adds positive engagement signals

### Why It Works

```
Google/Outlook sees:
- 50+ emails in a thread
- Consistent back-and-forth
- No spam complaints
- Links being clicked (partner opens emails)
- Replying behavior (auto-replies count as engagement)
- Topic relevance (AI-generated contextual content)

Result: High sender reputation score
```

### Implementation

```python
class WarmupThread:
    def __init__(self, user_email, partner_email):
        self.user = user_email
        self.partner = partner_email
        self.thread_id = None
        self.message_count = 0
    
    def start_thread(self, subject):
        """Inject first message into user's inbox"""
        msg = self.create_message(
            from_addr=self.partner,
            to_addr=self.user,
            subject=subject,
            body=self.generate_warmup_content()
        )
        result = self.insert_to_inbox(msg)
        self.thread_id = result['threadId']
        return result
    
    def continue_thread(self):
        """Add reply to existing thread"""
        # Partner replies
        self.add_reply(self.partner, self.user)
        
        # User "replies" (auto-generated via API)
        self.add_reply(self.user, self.partner)
        
        self.message_count += 2
    
    def generate_warmup_content(self):
        """AI-generated contextual content"""
        topics = [
            "Thanks for the update on the project",
            "Great insights in your last email",
            "Looking forward to our call next week",
            "The proposal looks solid, let's discuss",
        ]
        return random.choice(topics) + self.generate_context()
```

---

## 5. Filtering Warmup Emails from User View

### Gmail Filter Creation

```python
def create_hidden_warmup_filter(service, user_id='me'):
    """
    Creates a filter that hides warmup emails from the user's inbox
    but keeps them in the account for reputation building.
    """
    
    # Create a special label (user can't easily find it)
    label = {
        'name': '_warmy_internal_do_not_delete',
        'labelListVisibility': 'labelHide',  # Hidden from label list
        'messageListVisibility': 'hide'     # Hidden from message list
    }
    label_result = service.users().labels().create(
        userId=user_id, body=label
    ).execute()
    label_id = label_result['id']
    
    # Create filter for incoming warmup emails
    filter_body = {
        'criteria': {
            'query': 'from:(@warmup-partner.net) OR subject:([Warmup])'
        },
        'action': {
            'addLabelIds': [label_id],
            'removeLabelIds': ['INBOX', 'UNREAD'],
            'forward': ''  # Don't forward
        }
    }
    
    service.users().settings().filters().create(
        userId=user_id, body=filter_body
    ).execute()
```

### Alternative: IMAP-based Filtering

For non-Gmail providers:

```python
import imaplib

def setup_imap_filter(email_account, password):
    """Setup IMAP-side filtering for non-Gmail providers"""
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_account, password)
    
    # Create a folder for warmup emails
    mail.create('Warmup_Internal')
    
    # Note: Actual server-side filtering requires 
    # Sieve scripts or provider-specific rules
```

---

## 6. Capacity Balancing Algorithm

### The Problem

If Gmail allows 500 emails/day, and you need:
- 50 warmup emails
- 450 outreach emails

How do you balance without hitting limits?

### Solution: Dynamic Capacity Allocation

```python
class CapacityBalancer:
    def __init__(self, daily_limit=500):
        self.daily_limit = daily_limit
        self.warmup_allocation = 0.10  # 10% default
        self.used_today = {
            'warmup': 0,
            'outreach': 0
        }
    
    def calculate_allocation(self, current_reputation_score):
        """
        Dynamically adjust warmup vs outreach allocation
        based on current domain reputation.
        """
        
        if current_reputation_score < 30:
            # New domain: 50% warmup, 50% outreach
            self.warmup_allocation = 0.50
        elif current_reputation_score < 60:
            # Building: 30% warmup, 70% outreach
            self.warmup_allocation = 0.30
        elif current_reputation_score < 80:
            # Established: 15% warmup, 85% outreach
            self.warmup_allocation = 0.15
        else:
            # Mature: 5% maintenance warmup
            self.warmup_allocation = 0.05
        
        return self.warmup_allocation
    
    def get_available_capacity(self, email_type='outreach'):
        """Returns how many emails of each type can be sent today"""
        
        warmup_capacity = int(self.daily_limit * self.warmup_allocation)
        outreach_capacity = self.daily_limit - warmup_capacity
        
        if email_type == 'warmup':
            return warmup_capacity - self.used_today['warmup']
        else:
            return outreach_capacity - self.used_today['outreach']
    
    def record_send(self, email_type, count=1):
        """Record that emails were sent"""
        self.used_today[email_type] += count
        
        # Safety check
        if self.used_today['warmup'] + self.used_today['outreach'] > self.daily_limit:
            raise Exception("Daily limit exceeded!")
```

### Example Usage

```python
balancer = CapacityBalancer(daily_limit=50)  # Conservative for new account

# Day 1: New domain, reputation = 10
balancer.calculate_allocation(10)
# warmup_allocation = 0.50

# Available: 25 warmup, 25 outreach
print(balancer.get_available_capacity('warmup'))   # 25
print(balancer.get_available_capacity('outreach')) # 25

# Day 30: Reputation improved to 60
balancer.calculate_allocation(60)
# warmup_allocation = 0.15

# Available: 7 warmup, 43 outreach
print(balancer.get_available_capacity('warmup'))   # 7
print(balancer.get_available_capacity('outreach')) # 43
```

---

## 7. APIs and Methods Required to Replicate

### Gmail API (Primary)

| Endpoint | Purpose | OAuth Scope |
|----------|---------|-------------|
| `users.messages.send` | Send email | `gmail.send` |
| `users.messages.insert` | Inject into inbox | `gmail.modify` |
| `users.drafts.create` | Create draft | `gmail.compose` |
| `users.drafts.send` | Send draft | `gmail.compose` |
| `users.labels.create` | Create hidden labels | `gmail.modify` |
| `users.settings.filters.create` | Create auto-archive filter | `gmail.settings.basic` |

### Microsoft Graph API (Outlook)

| Endpoint | Purpose |
|----------|---------|
| `/me/messages` | Create message |
| `/me/sendMail` | Send email |
| `/me/mailFolders/inbox/messages` | Access inbox |
| `/me/messageRules` | Create filtering rules |

### IMAP (Fallback)

```
Commands needed:
- APPEND (inject message into folder)
- STORE (modify flags like \Seen)
- EXPUNGE (remove messages)
- CREATE (create folders)
```

---

## 8. Code Snippets

### Complete Warmup Engine (Pseudocode)

```python
"""
Mails.ai-style Email Warmup Engine
Replicates the from-inbox sending mechanism
"""

import base64
import json
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailWarmupEngine:
    def __init__(self, oauth_credentials):
        self.creds = Credentials.from_authorized_user_info(
            json.loads(oauth_credentials),
            scopes=['https://www.googleapis.com/auth/gmail.modify']
        )
        self.service = build('gmail', 'v1', credentials=self.creds)
        self.warmup_label_id = None
        
    def initialize(self):
        """Setup: Create hidden label and filter"""
        self._create_hidden_label()
        self._create_warmup_filter()
    
    def _create_hidden_label(self):
        """Create a label that's hidden from the user's view"""
        label_body = {
            'name': '_warmup_system',
            'labelListVisibility': 'labelHide',
            'messageListVisibility': 'hide'
        }
        result = self.service.users().labels().create(
            userId='me', body=label_body
        ).execute()
        self.warmup_label_id = result['id']
    
    def _create_warmup_filter(self):
        """Auto-archive warmup emails"""
        filter_body = {
            'criteria': {
                'query': 'from:(warmup-partner.net)'
            },
            'action': {
                'addLabelIds': [self.warmup_label_id],
                'removeLabelIds': ['INBOX']
            }
        }
        self.service.users().settings().filters().create(
            userId='me', body=filter_body
        ).execute()
    
    def inject_warmup_email(self, partner_email, subject, body):
        """
        Inject a warmup email that appears as if it was received
        from a partner in the warmup network.
        """
        message = MIMEText(body)
        message['to'] = 'me'  # Current authenticated user
        message['from'] = partner_email
        message['subject'] = subject
        message['date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
        
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Insert into inbox (appears as received email)
        return self.service.users().messages().insert(
            userId='me',
            body={'raw': raw},
            internalDateSource='dateHeader'
        ).execute()
    
    def send_warmup_reply(self, thread_id, to_email, body):
        """
        Send a reply from the user's account as part of warmup thread.
        """
        message = MIMEText(body)
        message['to'] = to_email
        message['subject'] = 'Re: Warmup thread'
        
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        return self.service.users().messages().send(
            userId='me',
            body={'raw': raw, 'threadId': thread_id}
        ).execute()
    
    def run_daily_warmup(self, target_count=20):
        """
        Execute daily warmup routine.
        """
        partners = self._get_warmup_partners()
        
        for i in range(target_count):
            partner = partners[i % len(partners)]
            
            # Inject received email
            result = self.inject_warmup_email(
                partner_email=partner['email'],
                subject=partner['subject'],
                body=partner['body']
            )
            
            # Auto-reply
            self.send_warmup_reply(
                thread_id=result['threadId'],
                to_email=partner['email'],
                body=self._generate_reply()
            )
    
    def _get_warmup_partners(self):
        """Returns list of partner accounts in warmup network"""
        # In production, this would query the warmup network database
        return [
            {'email': 'partner1@warmup-network.com', 'subject': 'Re: Project update', 'body': 'Thanks!'},
            {'email': 'partner2@warmup-network.com', 'subject': 'Re: Meeting notes', 'body': 'Great points!'},
        ]
    
    def _generate_reply(self):
        """Generate contextual reply content"""
        templates = [
            "Thanks for sharing this, very helpful!",
            "Great insights, let's discuss further.",
            "I appreciate you following up on this.",
        ]
        return templates[hash(datetime.now()) % len(templates)]
```

---

## 9. Alternatives & Competitors

If Mails.ai information is unavailable, consider these alternatives:

| Service | From-Inbox Method | Capacity Balancing | Special Features |
|---------|-------------------|-------------------|------------------|
| **Warmy.io** | Gmail API + IMAP | AI-adjusted | Google Postmaster integration |
| **Mailwarm** | SMTP + API hybrid | Fixed allocation | Simple dashboard |
| **Mailreach** | IMAP-based | Manual | SPF/DKIM checker |
| **Lemwarm** | Gmail API | Smart scaling | Integrates with Lemlist |
| **Quickmail** | SMTP-based | Per-account | Sequences included |

### Open Source Alternative

```bash
# Self-hosted warmup (requires multiple email accounts)
git clone https://github.com/email-warmup-toolkit/self-warmup
# Requires: 5+ Gmail accounts, Python 3.9+, OAuth credentials
```

---

## 10. Key Takeaways

1. **From-Inbox = Gmail API `messages.insert()`**: Emails appear as received, not sent
2. **Filtering = Hidden labels + auto-archive**: Users don't see warmup emails
3. **Capacity = Dynamic allocation**: Adjust warmup % based on reputation
4. **Long chains = Thread building**: 50+ replies = strong engagement signals
5. **OAuth required**: Must have Gmail API access with modify scope

---

## 11. Security & Compliance Notes

⚠️ **Important Considerations:**

1. **Gmail ToS**: Google may consider automated warmup as "misuse"
2. **OAuth tokens**: Must be stored securely (encrypted)
3. **Rate limits**: Gmail API has quota limits (1 billion quota units/day)
4. **Account risk**: Aggressive warmup can trigger account suspension
5. **Disclosure**: Users should know their inbox is being used for warmup

---

## Document Information

- **Created**: 2026-02-15
- **Research Sources**: Gmail API docs, Warmy.io website, competitor analysis
- **Status**: Technical documentation based on available information
- **Note**: Mails.ai specific implementation details are proprietary; this document represents inferred architecture based on industry patterns.

