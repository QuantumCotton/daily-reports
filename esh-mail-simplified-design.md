# ESH Mail — Simplified Design (No Docker Required)
**Date:** 2026-02-14
**Status:** Ready to build
**Approach:** External SMTP (AWS SES, SendGrid) instead of self-hosted

---

## Why This Approach?

**Full ESH Mail (Self-Hosted) — REQUIRES DOCKER:**
- Docker containers for SMTP servers
- Docker Compose for orchestration
- Docker for testing
- Blocked by Docker permissions

**Simplified ESH Mail (External SMTP) — NO DOCKER:**
- Uses third-party SMTP (AWS SES, SendGrid, Mailgun)
- Python scripts for email sending
- No Docker required
- Can build TONIGHT

---

## Tradeoffs

| Feature | Self-Hosted (Full) | External SMTP (Simplified) |
|---------|-------------------|---------------------------|
| **Docker Required** | YES ❌ | NO ✅ |
| **Build Time** | 4-6 hours | 2-3 hours |
| **Cost (per 10k emails)** | $1 (AWS SES) | $10-100 (SendGrid/Mailgun) |
| **Control** | Full control | Limited control |
| **Self-Healing** | Custom implementation | Provider handles |
| **Setup Complexity** | High (Docker) | Low (API keys) |

---

## Simplified ESH Mail Architecture

### Core Components (Python Scripts)

#### 1. Email Sender (`esh_mail_sender.py`)
```python
# Uses AWS SES or SendGrid API
# Functions:
# - send_email(to, subject, body, template_id)
# - send_bulk(lead_list, template_id, daily_limit)
# - track_sent(email_id, status)
# - get_stats(email_id)
```

**Features:**
- Rate limiting (per-sender limits)
- Template management
- Sent tracking
- Bounce handling
- Unsubscribe management

---

#### 2. Reputation Monitor (`reputation_monitor.py`)
```python
# Checks Google Postmaster API
# Checks Microsoft SNDS API
# Functions:
# - check_reputation(domain)
# - check_spam_score(domain)
# - get_blocklist_status(domain)
# - alert_if_degraded(domain)
```

**Features:**
- Daily reputation checks
- Blocklist monitoring
- Degradation alerts (Telegram)
- Trend tracking

---

#### 3. Warmup Scheduler (`warmup_scheduler.py`)
```python
# Manages email warmup schedule
# Functions:
# - get_daily_limit(day)
# - schedule_emails(sending_domain, day)
# - track_warmup_progress(domain, day)
# - complete_warmup(domain)
```

**Warmup Schedule:**
- Week 1: 20-30 emails/day
- Week 2: 50-75 emails/day
- Week 3: 100-150 emails/day
- Week 4: 200-300 emails/day
- Week 5+: 500+ emails/day

---

#### 4. Dashboard (`esh_mail_dashboard.html`)
```python
# Web dashboard for monitoring
# Features:
# - Real-time email stats (sent, opened, replied)
# - Reputation scores (Google, Microsoft)
# - Blocklist status
# - Warmup progress
# - Campaign performance
```

**Metrics:**
- Emails sent today/week/month
- Open rate
- Reply rate
- Conversion rate
- Reputation score (0-100)
- Blocklist count

---

#### 5. Campaign Manager (`campaign_manager.py`)
```python
# Manages outreach campaigns
# Functions:
# - create_campaign(name, template_id, lead_list)
# - run_campaign(campaign_id, daily_limit)
# - pause_campaign(campaign_id)
# - get_campaign_stats(campaign_id)
```

**Campaign Workflow:**
1. Create campaign (select template, upload leads)
2. Set daily limit (e.g., 50 emails/day)
3. Run campaign (auto-send, rate-limited)
4. Monitor performance (dashboard)
5. Adjust (pause, resume, modify)

---

## Database Schema (SQLite)

### Email Tracking Table
```sql
CREATE TABLE email_logs (
    id INTEGER PRIMARY KEY,
    campaign_id INTEGER,
    lead_id INTEGER,
    email TEXT,
    subject TEXT,
    template_id TEXT,
    sent_at TIMESTAMP,
    opened_at TIMESTAMP,
    replied_at TIMESTAMP,
    status TEXT, -- sent, opened, replied, bounced
    tracking_id TEXT,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id),
    FOREIGN KEY (lead_id) REFERENCES leads(id)
);
```

### Reputation Log Table
```sql
CREATE TABLE reputation_logs (
    id INTEGER PRIMARY KEY,
    domain TEXT,
    google_score INTEGER, -- 0-100
    microsoft_score INTEGER, -- 0-100
    blocklist_count INTEGER,
    checked_at TIMESTAMP
);
```

### Warmup Progress Table
```sql
CREATE TABLE warmup_progress (
    id INTEGER PRIMARY KEY,
    domain TEXT,
    day INTEGER,
    sent_today INTEGER,
    target INTEGER,
    status TEXT, -- warming, complete, paused
    updated_at TIMESTAMP
);
```

### Campaigns Table
```sql
CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    template_id TEXT,
    daily_limit INTEGER,
    status TEXT, -- active, paused, completed
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

---

## File Structure

```
~/.openclaw/
├── workspace/
│   ├── esh-mail/
│   │   ├── esh_mail_sender.py
│   │   ├── reputation_monitor.py
│   │   ├── warmup_scheduler.py
│   │   ├── campaign_manager.py
│   │   └── esh_mail_dashboard.html
│   ├── database/
│   │   └── esh_mail.db
│   ├── templates/
│   │   ├── pm_dashboard.md
│   │   ├── apartment.md
│   │   ├── auto_shop.md
│   │   ├── restaurant.md
│   │   └── hoa.md
│   └── logs/
│       └── esh_mail.log
```

---

## API Providers (Choose One)

### Option 1: AWS SES (Recommended)
- Cost: $0.10 per 10,000 emails
- Setup: AWS account, SES verified domain
- Pros: Cheap, reliable, good deliverability
- Cons: Requires AWS setup

### Option 2: SendGrid
- Cost: $20-100 per month (depending on plan)
- Setup: SendGrid account, API key
- Pros: Easy setup, good dashboard
- Cons: More expensive

### Option 3: Mailgun
- Cost: $35-85 per month
- Setup: Mailgun account, API key
- Pros: Good analytics
- Cons: More expensive

---

## Implementation Plan

### Phase 1: Core Email Sender (1 hour)
1. Set up AWS SES account (you do this)
2. Create `esh_mail_sender.py`
3. Implement `send_email()` function
4. Implement `send_bulk()` function
5. Test with single email

### Phase 2: Reputation Monitor (30 minutes)
1. Create `reputation_monitor.py`
2. Implement Google Postmaster API check
3. Implement Microsoft SNDS API check
4. Test reputation checking
5. Set up Telegram alerts

### Phase 3: Warmup Scheduler (30 minutes)
1. Create `warmup_scheduler.py`
2. Implement warmup schedule logic
3. Create `warmup_progress` table
4. Track warmup progress
5. Set up daily warmup cron job

### Phase 4: Campaign Manager (30 minutes)
1. Create `campaign_manager.py`
2. Implement campaign creation
3. Implement campaign execution
4. Implement campaign tracking
5. Test with small campaign

### Phase 5: Dashboard (30 minutes)
1. Create `esh_mail_dashboard.html`
2. Connect to SQLite database
3. Display real-time stats
4. Add reputation monitoring
5. Add campaign tracking

### Phase 6: Integration (30 minutes)
1. Connect to lead database
2. Import email templates
3. Set up cron jobs
4. Test end-to-end

---

## Total Time Estimate: 3.5 hours

**Tonight:**
- Phase 1: Core Email Sender (1 hour)
- Phase 2: Reputation Monitor (30 minutes)
- Phase 3: Warmup Scheduler (30 minutes)

**Tomorrow:**
- Phase 4: Campaign Manager (30 minutes)
- Phase 5: Dashboard (30 minutes)
- Phase 6: Integration (30 minutes)

---

## What You Need to Do

### Before Tonight:
1. **Set up AWS SES account** (if using AWS SES)
2. **Verify domain** in AWS SES (kmjk.pro or new domain)
3. **Get SMTP credentials** (user, password, server)
4. **Send me the credentials** (or store in config file)

### Alternative: Use SendGrid (Easier Setup)
1. **Create SendGrid account** (free trial available)
2. **Get API key**
3. **Send me the API key**
4. **I build the rest**

---

## What I Can Do Without Docker

✅ **YES, I can build:**
- Email sender (Python script)
- Reputation monitor (API calls)
- Warmup scheduler (Python script)
- Campaign manager (Python script)
- Dashboard (HTML/JS)
- Database (SQLite)
- All core functionality

❌ **NO, I cannot build:**
- Self-hosted SMTP servers (requires Docker)
- Docker Compose orchestration
- Containerized email services

---

## Recommendation

**Option A: Build Simplified ESH Mail Tonight**
- Uses external SMTP (AWS SES or SendGrid)
- No Docker required
- Time: 3.5 hours total (2 hours tonight)
- Cost: $0.10-100 per 10,000 emails
- Can start outreach campaigns immediately

**Option B: Wait for Docker Fix**
- Fix Docker: `sudo usermod -aG docker chris`
- Then build full ESH Mail
- Uses self-hosted SMTP
- Lower cost ($1 per 10,000 emails)
- More control, but longer timeline

---

## My Recommendation

**Build Simplified ESH Mail TONIGHT.**

**Why:**
- Can start outreach immediately
- No waiting for Docker fix
- Higher initial cost, but faster time-to-market
- Can switch to self-hosted SMTP later (after Docker fixed)

**Action Item:** Set up AWS SES or SendGrid account, get credentials, send to me.

---

_Ready to build when you provide SMTP credentials._
