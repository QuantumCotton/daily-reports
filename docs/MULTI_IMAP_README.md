# Multi-IMAP Unified Inbox for Treasure Coast Emails

## Overview

This system provides a **unified inbox dashboard** that connects to ALL 10 Treasure Coast email accounts separately via IMAP. **No forwarding is used** — each email maintains its own reputation for proper email warming.

## Key Design Principle

✅ **CORRECT:** Dashboard reads from all 10 emails separately → Each warms independently  
❌ **WRONG:** All emails forward to one inbox → Defeats warming

## Components

### 1. Multi-IMAP Sync Script
**Location:** `/home/chris/.openclaw/bin/multi_imap_inbox.py`

Connects to all 10 Treasure Coast emails separately via IMAP and syncs to SQLite database.

### 2. Dashboard
**Location:** `/home/chris/.openclaw/workspace/reports/inbox.html`

Web interface showing unified view with:
- All messages from all 10 accounts
- Account filter dropdown
- Individual account cards
- Message detail view

## Email Accounts

All 10 Treasure Coast emails:
1. chris@kmjk.pro
2. projects-tc@kmjk.pro
3. estimates-tc@kmjk.pro
4. site-tc@kmjk.pro
5. office-tc@kmjk.pro
6. sales-tc@kmjk.pro
7. support-tc@kmjk.pro
8. billing-tc@kmjk.pro
9. info-tc@kmjk.pro
10. team-tc@kmjk.pro

## Setup

### Step 1: Configure Passwords

Create `/home/chris/.openclaw/config/email_accounts.json`:

```json
{
  "chris@kmjk.pro": "your_password_here",
  "projects-tc@kmjk.pro": "your_password_here",
  "estimates-tc@kmjk.pro": "your_password_here",
  "site-tc@kmjk.pro": "your_password_here",
  "office-tc@kmjk.pro": "your_password_here",
  "sales-tc@kmjk.pro": "your_password_here",
  "support-tc@kmjk.pro": "your_password_here",
  "billing-tc@kmjk.pro": "your_password_here",
  "info-tc@kmjk.pro": "your_password_here",
  "team-tc@kmjk.pro": "your_password_here"
}
```

**OR** use environment variables (one per account):
```bash
export CHRIS_KMJK_PRO_PASSWORD="your_password"
export PROJECTS_TC_KMJK_PRO_PASSWORD="your_password"
# ... etc for all 10 accounts
```

### Step 2: Run Initial Sync

```bash
python3 /home/chris/.openclaw/bin/multi_imap_inbox.py
```

This will:
- Connect to each account separately via IMAP
- Download recent messages (default: last 50 per account)
- Store in SQLite: `/home/chris/.openclaw/data/inbox.db`

### Step 3: Access Dashboard

Open `/home/chris/.openclaw/workspace/reports/inbox.html` in a browser.

## Usage

### Manual Sync

Run the sync script anytime:
```bash
python3 /home/chris/.openclaw/bin/multi_imap_inbox.py
```

### Automated Sync (Cron)

Add to crontab for regular syncing (e.g., every 15 minutes):
```bash
*/15 * * * * /home/chris/.openclaw/bin/multi_imap_inbox.py
```

## Database Schema

SQLite database at `/home/chris/.openclaw/data/inbox.db`:

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_source TEXT NOT NULL,        -- Which email account received this
    message_id TEXT UNIQUE,
    uid INTEGER,
    subject TEXT,
    from_addr TEXT,
    to_addr TEXT,
    cc_addr TEXT,
    date_sent TIMESTAMP,
    date_received TIMESTAMP,
    body_text TEXT,
    body_html TEXT,
    folder TEXT DEFAULT 'INBOX',
    flags TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Key field:** `account_source` — Tags which account received each message.

## IMAP Configuration

- **Server:** imap.zoho.com
- **Port:** 993 (SSL)
- **Protocol:** IMAP4 SSL

## Security Notes

1. **Config file permissions:** Set restrictive permissions:
   ```bash
   chmod 600 /home/chris/.openclaw/config/email_accounts.json
   ```

2. **Environment variables:** More secure than config file if set in a secure environment.

3. **No forwarding:** Each account connects independently → Proper warming behavior.

## Troubleshooting

### Script fails with "No credentials found"
- Check that config file exists at `/home/chris/.openclaw/config/email_accounts.json`
- Or verify environment variables are set (one per account)

### IMAP connection errors
- Verify IMAP credentials are correct
- Check internet connectivity
- Verify Zoho account IMAP is enabled

### Dashboard shows no messages
- Run sync script first
- Check database exists at `/home/chris/.openclaw/data/inbox.db`
- Verify messages were synced (check script output)

## Status

✅ Multi-IMAP sync script created  
✅ Dashboard HTML created  
✅ Configuration template provided  
✅ Each email connects separately (NO forwarding)  
✅ Dashboard shows unified view with account filtering  

Each email warms independently!
