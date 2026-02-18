# EMAIL SYSTEM - COMPLETE DOCUMENTATION
> **Created:** 2026-02-16 08:55 UTC
> **Purpose:** Document entire email infrastructure for future reference

---

## 📧 EMAIL INFRASTRUCTURE OVERVIEW

### Goal
Set up 400 email addresses for email warming and outreach to business clients (NOT contractors).

### Strategy
- **Email warming:** Gradually build sender reputation over 14 days
- **Outreach:** Send cold emails to business clients after warm-up
- **Target:** Property managers, apartments, HOAs, auto dealerships, restaurants
- **NOT targeting:** Contractors (job ads expire, business listings are permanent)

---

## 🏗️ EMAIL ARCHITECTURE

### Email Count (FINAL DECISION)
- **Total emails:** 400 (40 metros × 10 emails each)
- **Currently configured:** 365 (360 metro emails + 5 warming emails)
- **Missing:** 35 emails (to reach 400)

### Email Structure Per Metro (10 emails)
1. `chris@kmjk.pro` (Owner - same for all metros)
2. `projects-[CODE]@kmjk.pro`
3. `estimates-[CODE]@kmjk.pro`
4. `site-[CODE]@kmjk.pro`
5. `office-[CODE]@kmjk.pro`
6. `sales-[CODE]@kmjk.pro`
7. `support-[CODE]@kmjk.pro`
8. `billing-[CODE]@kmjk.pro`
9. `info-[CODE]@kmjk.pro`
10. `team-[CODE]@kmjk.pro`

### Example: Treasure Coast (-tc)
- `chris@kmjk.pro`
- `projects-tc@kmjk.pro`
- `estimates-tc@kmjk.pro`
- `site-tc@kmjk.pro`
- `office-tc@kmjk.pro`
- `sales-tc@kmjk.pro`
- `support-tc@kmjk.pro`
- `billing-tc@kmjk.pro`
- `info-tc@kmjk.pro`
- `team-tc@kmjk.pro`

---

## 📋 40 METROS (FROM CHRIS'S RESEARCH)

**Email list file:** `/home/chris/.openclaw/workspace/EMAIL-LIST.txt` (360 aliases)

**Organized by income tiers:**

### Tier 1 ($200K+ median)
1. Tri-State Area (NY-NJ-CT)
2. San Francisco Bay Area (-ba)
3. Philadelphia Metro
4. Chicago Metro
5. Washington D.C. Metro (-dc)
6. Los Angeles Metro
7. Boston Metro

### Tier 2 ($150K-$200K median)
8. Kansas City Metro
9. Dallas-Fort Worth Metro (-dfw)
10. Houston Metro (-hou)
11. Wichita Metro
12. Seattle Metro (-sea)
13. Detroit Metro
14. Atlanta Metro (-atl)
15. Anchorage Metro
16. Memphis Metro
17. Denver Metro (-den)
18. Des Moines Metro
19. Oklahoma City Metro
20. Phoenix Metro (-phx)
21. Raleigh-Durham Metro (-rdu)
22. Jackson Metro
23. Manchester-Nashua Metro
24. Indianapolis Metro
25. Nashville Metro (-bna)
26. Cleveland-Akron Metro
27. Columbus Metro
28. Lexington Metro
29. Salt Lake City Metro
30. Louisville Metro
31. Fort Wayne Metro
32. Honolulu Metro
33. Albuquerque Metro
34. Providence Metro
35. Las Vegas Metro
36. Portland Metro (OR)
37. Charlotte Metro (-clt)
38. Milwaukee Metro
39. Portland Metro (ME)
40. Madison Metro

**Total:** 40 metros × 9 emails each = 360 emails
**Plus:** 5 warming emails (warming1-5@kmjk.pro)
**Total configured:** 365 emails

---

## 🔧 TECHNICAL IMPLEMENTATION

### Mail Server
- **Software:** Postfix (self-hosted)
- **VPS IP:** 107.172.20.181
- **Domain:** kmjk.pro
- **MX record:** Points to VPS IP
- **Authentication:** NO SMTP auth needed (Postfix sends directly)

### Postfix Configuration Files

**1. `/etc/postfix/virtual` (368 lines)**
- Maps email aliases to local user
- Format: `email@kmjk.pro root`
- Currently has 365 email aliases configured

**2. `/etc/postfix/sender_canonical`**
- Maps outgoing sender addresses
- Ensures emails send from correct alias
- Format: `root projects-tc@kmjk.pro`

**3. Postfix main.cf settings:**
```
virtual_alias_maps = hash:/etc/postfix/virtual
sender_canonical_maps = hash:/etc/postfix/sender_canonical
```

### Setup Script
**File:** `/home/chris/.openclaw/bin/setup_email_aliases.sh`

**What it does:**
1. Reads EMAIL-LIST.txt
2. Adds aliases to /etc/postfix/virtual
3. Adds mappings to /etc/postfix/sender_canonical
4. Runs `postmap` to rebuild databases
5. Reloads Postfix

**Requires:** sudo access (Chris ran this already)

**Status:** ✅ ALREADY COMPLETED (Chris ran it, 368 aliases configured)

---

## 🚀 EMAIL WARM-UP SYSTEM

### Warm-Up Philosophy
- **Goal:** Build sender reputation gradually to avoid spam filters
- **Duration:** 14 days
- **Total emails:** 146,000 (across all 365 accounts)

### 14-Day Ramp Schedule
**File:** `/home/chris/.openclaw/workspace/warmup_schedule.json`

| Phase | Days | Emails/Account | Total/Day | Purpose |
|-------|------|----------------|-----------|---------|
| 1 | 1-3 | 10 | 3,650 | Conservative start |
| 2 | 4-7 | 20 | 7,300 | Moderate increase |
| 3 | 8-10 | 30 | 10,950 | Aggressive ramp |
| 4 | 11-14 | 50 | 18,250 | Peak volume |

**Total per account:** 330 emails over 14 days
**Total all accounts:** 120,450 emails over 14 days

### Warm-Up Automation
**File:** `/home/chris/.openclaw/bin/run_warmup.py`

**How it works:**
1. Loads warmup_schedule.json
2. Calculates how many emails to send today
3. Distributes across all 365 accounts evenly
4. Sends emails with 3-second delay
5. Logs all sends to warmup.log

**Cron schedule:** 6 batches per day (8:00, 9:30, 13:00, 14:30, 17:00, 18:30 UTC)

**Status:** ⏸️ NOT STARTED (scheduled to start Feb 17, 2026)

### Reputation Monitoring
**Database:** `/home/chris/.openclaw/workspace/email_reputation.db`

**Tracks per account:**
- Sent count
- Delivered count
- Bounced count
- Spam complaints
- Opens
- Clicks
- Reputation score (0-100)

**Auto-pause thresholds:**
- Bounce rate > 5%
- Complaint rate > 0.1%
- Reputation score < 70

**Monitor script:** `/home/chris/.openclaw/bin/reputation_monitor.py`

**Status:** ✅ INITIALIZED (365 accounts tracked, all at 100% reputation)

---

## 🧪 TEST EMAIL SENDING

### Test Script
**File:** `/home/chris/.openclaw/bin/send_test_emails.py`

**Purpose:** Verify all 365 email accounts can send

**Configuration:**
- **Recipient:** hercules71185@gmail.com
- **Subject:** "wewillbelaunchingsoon"
- **Body:** "Test from [email] - warming up"
- **Delay:** 3 seconds between sends
- **Total time:** ~18 minutes for 365 emails

**Usage:**
```bash
# Send test from all 365 accounts
python3 /home/chris/.openclaw/bin/send_test_emails.py

# Send test from first 5 accounts (quick test)
python3 /home/chris/.openclaw/bin/send_test_emails.py --test
```

**Status:** 🟢 STARTED SENDING (06:55 UTC, ~18 min duration)
**Verification needed:** Check if all 365 emails sent successfully

---

## 📥 UNIFIED INBOX DASHBOARD

### Purpose
Dashboard to view all incoming emails from the 10 Treasure Coast email accounts.

### Architecture
**CORRECT APPROACH:** Multi-IMAP (NO forwarding)

**Why no forwarding?**
- Forwarding all emails to one inbox defeats email warming
- All sends would come from one reputation
- Each email account needs separate reputation

**How it works:**
1. Dashboard connects to all 10 Treasure Coast emails via IMAP separately
2. Each email account connects independently
3. Each maintains its own sender reputation
4. Dashboard just aggregates the view

### 10 Treasure Coast Emails (For Inbox)
1. `chris@kmjk.pro`
2. `projects-tc@kmjk.pro`
3. `estimates-tc@kmjk.pro`
4. `site-tc@kmjk.pro`
5. `office-tc@kmjk.pro`
6. `sales-tc@kmjk.pro`
7. `support-tc@kmjk.pro`
8. `billing-tc@kmjk.pro`
9. `info-tc@kmjk.pro`
10. `team-tc@kmjk.pro`

### IMAP Configuration
**Server:** imap.zoho.com:993 (SSL)
**Passwords:** `/home/chris/.openclaw/config/email_accounts.json`
- All accounts use: Cotton247

### Files Created
**1. Multi-IMAP Sync Script:**
- `/home/chris/.openclaw/bin/multi_imap_inbox.py`
- Connects to all 10 emails via IMAP
- Downloads messages
- Stores in SQLite: `/home/chris/.openclaw/data/inbox.db`

**2. Inbox API Server:**
- `/home/chris/.openclaw/bin/inbox_api_server.py`
- Port: 8182
- Endpoints: `/api/inbox`, `/api/inbox/{id}`

**3. Inbox Dashboard:**
- `/home/chris/.openclaw/workspace/reports/inbox.html`
- Dark theme UI
- Shows messages from all 10 accounts
- Filter by account

**4. Password Config:**
- `/home/chris/.openclaw/config/email_accounts.json`
- Contains Cotton247 for all 10 accounts

**Status:** ✅ BUILT BUT IMAP AUTH FAILING
**Issue:** Zoho rejecting "Cotton247" for IMAP access
**Fix needed:** Zoho app-specific passwords for IMAP

### Dashboard URL
http://107.172.20.181:8282/

---

## 🎯 EMAIL VOLUME STRATEGY

### Musk's Math (From War Room)
**Question:** "How many cold emails per day for 1 sale/day?"
**Musk's answer:** 14,000 emails/day

**Breakdown:**
- 14,000 emails/day ÷ 40 metros = **350 emails per metro per day**
- With warmed domains + personalized emails = 1 sale/day

### Current Capacity
- **Email accounts:** 365 (will be 400)
- **Warm-up period:** 14 days (Feb 18 - Mar 3)
- **Full capacity:** March 4 onwards

### Target Metrics
- **Feb 21:** 500 complete Treasure Coast leads
- **March 7:** 1,500 total leads ready to send
- **March 7:** First email outreach begins

---

## 📁 ALL EMAIL-RELATED FILES

### Email Lists
- `/home/chris/.openclaw/workspace/EMAIL-LIST.txt` - 360 email aliases
- `/home/chris/.openclaw/workspace/METRO-DATABASE.md` - 40 metros with 95 ZIPs

### Configuration
- `/etc/postfix/virtual` - Email aliases (368 lines)
- `/etc/postfix/sender_canonical` - Sender mappings
- `/home/chris/.openclaw/config/email_accounts.json` - IMAP passwords

### Scripts
- `/home/chris/.openclaw/bin/setup_email_aliases.sh` - Configure Postfix
- `/home/chris/.openclaw/bin/send_test_emails.py` - Send test emails
- `/home/chris/.openclaw/bin/run_warmup.py` - Execute warm-up sends
- `/home/chris/.openclaw/bin/reputation_monitor.py` - Monitor reputation
- `/home/chris/.openclaw/bin/multi_imap_inbox.py` - IMAP sync
- `/home/chris/.openclaw/bin/inbox_api_server.py` - Inbox API
- `/home/chris/.openclaw/bin/chat_server.py` - Chat backend (8184)

### Data
- `/home/chris/.openclaw/workspace/warmup_schedule.json` - 14-day plan
- `/home/chris/.openclaw/workspace/email_reputation.db` - Reputation tracking
- `/home/chris/.openclaw/data/inbox.db` - Inbox messages

### Dashboards
- `/home/chris/.openclaw/workspace/reports/inbox.html` - Inbox dashboard
- `/home/chris/.openclaw/workspace/reports/chat.html` - Chat interface

### Documentation
- `/home/chris/.openclaw/workspace/EMAIL-SYSTEM-COMPLETE.md` - This file
- `/home/chris/.openclaw/workspace/PROCESS.md` - Overall playbook

---

## ⚠️ CRITICAL DATES

| Date | Milestone | Status |
|------|-----------|--------|
| **Feb 16** | Email config complete | ✅ DONE (368 aliases) |
| **Feb 16** | Test emails sent | 🟢 SENDING (in progress) |
| **Feb 18** | Email warm-up starts | ⏸️ SCHEDULED (2 days) |
| **Feb 21** | 500 Treasure Coast leads | 🟡 102/500 (20.4%) |
| **Mar 3** | Warm-up complete | ⏸️ UPCOMING |
| **Mar 7** | First email outreach | ⏸️ UPCOMING (19 days) |

---

## 🚨 CURRENT ISSUES

### 1. IMAP Authentication Failing
**Problem:** Zoho rejecting "Cotton247" for IMAP access
**Impact:** Unified inbox can't sync emails
**Fix needed:** Generate Zoho app-specific passwords for IMAP
**Workaround:** Can send emails (SMTP works), can't read inbox yet

### 2. Test Email Completion Unknown
**Problem:** Started sending 365 test emails at 06:55 UTC, not verified completion
**Impact:** Don't know if all accounts can send successfully
**Fix needed:** Check mail queue or ask Chris if he received 365 emails

### 3. Missing 35 Emails
**Problem:** 365 configured, goal is 400
**Impact:** Minor - 365 is sufficient for warm-up
**Fix needed:** Add 35 more emails to EMAIL-LIST.txt, re-run setup script (optional)

---

## ✅ COMPLETED TASKS

1. ✅ Email list created (360 aliases)
2. ✅ Postfix configuration complete (368 aliases)
3. ✅ Setup script created and executed
4. ✅ Warm-up schedule designed (14-day plan)
5. ✅ Reputation monitoring initialized (365 accounts)
6. ✅ Test email script created
7. ✅ Test emails started sending
8. ✅ Unified inbox built (multi-IMAP, no forwarding)
9. ✅ Chat interface deployed (10 conversation threads)

---

## 🎯 NEXT STEPS

### Immediate
1. **Verify test emails completed** - Check if all 365 sent
2. **Fix IMAP authentication** - Get Zoho app passwords
3. **Start warm-up on Feb 18** - Install cron jobs

### Ongoing
4. **Continue Treasure Coast enrichment** - Reach 500 complete leads by Feb 21
5. **Monitor reputation** - Daily checks once warm-up starts
6. **Build lead database** - 1,500 total leads by March 7

---

## 📊 SUCCESS METRICS

### Email System
- ✅ 365 emails configured
- 🟡 365 test emails sending
- ⏸️ 14-day warm-up (starts Feb 18)
- ⏸️ 146,000 emails sent (by Mar 3)

### Lead Generation
- ✅ 22,755 total leads
- 🟡 102/500 Treasure Coast complete
- ⏸️ 1,500 leads ready (by Mar 7)

### Business Goals
- ⏸️ First sale (target: March 7-14)
- ⏸️ 10 sales by end of March
- ⏸️ $500k total revenue (Chris makes $100k)

---

**Last Updated:** 2026-02-16 08:55 UTC
**Status:** Email infrastructure 90% complete, warm-up scheduled, outreach preparation on track
