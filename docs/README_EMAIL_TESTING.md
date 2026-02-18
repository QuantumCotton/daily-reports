# Email Testing Quick Start Guide

This guide helps you test all 400 email accounts by sending test emails to hercules71185@gmail.com.

---

## 🚀 QUICK START

### Step 1: Verify DNS Records
```bash
dig txt kmjk.pro +short
dig -x 107.172.20.181 +short
```

**Expected Output:**
- SPF: `"v=spf1 ip4:107.172.20.181 ~all"`
- PTR: `mail.kmjk.pro.`

### Step 2: Configure Email Aliases (One-Time Setup)
```bash
sudo bash setup_email_aliases.sh
```

This will configure all 360 email addresses in Postfix.

### Step 3: Test with Small Subset
```bash
# Preview what will be sent (dry-run)
python3 send_test_emails.py --test --dry-run

# Send 5 test emails
python3 send_test_emails.py --test
```

### Step 4: Monitor Deliverability
```bash
# Check mail logs
sudo tail -f /var/log/mail.log

# Check mail queue
sudo mailq
```

### Step 5: Send All Emails
```bash
# Preview all 360 emails
python3 send_test_emails.py --dry-run

# Send all 360 emails (will ask for confirmation)
python3 send_test_emails.py
```

---

## 📁 FILES IN THIS PACKAGE

### 1. `send_test_emails.py`
Test email sender script.

**Features:**
- Sends test email to hercules71185@gmail.com
- Subject: "wewillbelaunchingsoon"
- Body: "Test from [email address]"
- Configurable delay between sends
- Test mode and dry-run options
- Progress tracking and statistics

**Usage:**
```bash
python3 send_test_emails.py [OPTIONS]

Options:
  --test      Send only 5 emails (for testing)
  --delay N   Delay in seconds between sends (default: 3)
  --dry-run   Preview without sending
```

**Examples:**
```bash
# Test with 5 emails
python3 send_test_emails.py --test

# Dry-run to preview
python3 send_test_emails.py --dry-run

# Send all with 2 second delay
python3 send_test_emails.py --delay 2
```

### 2. `setup_email_aliases.sh`
One-time setup script to configure all 360 email addresses in Postfix.

**What it does:**
- Configures virtual aliases in `/etc/postfix/virtual`
- Configures sender canonical mappings in `/etc/postfix/sender_canonical`
- Rebuilds Postfix databases
- Reloads Postfix configuration

**Usage:**
```bash
sudo bash setup_email_aliases.sh
```

**Requirements:**
- Must run as root (sudo)
- Postfix must be installed
- Email list file must exist at `/home/chris/.openclaw/workspace/EMAIL-LIST.txt`

### 3. `EMAIL_CONFIGURATION_REPORT.md`
Comprehensive analysis report covering:
- Email configuration approach (Option A vs Option B)
- Current setup analysis
- Credentials analysis
- Step-by-step setup instructions
- Troubleshooting guide
- Next steps

### 4. `TASK_COMPLETION_SUMMARY.md`
Quick summary of what was accomplished and what's needed.

---

## 🔧 POSTFIX REFERENCE

### Key Files
- `/etc/postfix/virtual` - Virtual alias mappings
- `/etc/postfix/virtual.db` - Compiled alias database
- `/etc/postfix/sender_canonical` - Sender address rewriting
- `/etc/postfix/sender_canonical.db` - Compiled sender mapping

### Key Commands
```bash
# Reload Postfix
sudo systemctl reload postfix

# Rebuild databases
sudo postmap /etc/postfix/virtual
sudo postmap /etc/postfix/sender_canonical

# Check status
sudo systemctl status postfix

# View logs
sudo tail -f /var/log/mail.log

# Check queue
sudo mailq

# Flush queue
sudo postqueue -f

# Verify virtual alias mapping
sudo postmap -q 'warming1@kmjk.pro' /etc/postfix/virtual.db

# Verify sender canonical mapping
sudo postmap -q 'chris@hostname' /etc/postfix/sender_canonical.db
```

---

## ⚠️ IMPORTANT NOTES

### Email Configuration Approach
**Current Setup:** kmjk.pro uses self-hosted Postfix, NOT Zoho.

**Recommended Approach:** Virtual Aliases with Sender Canonical
- No SMTP credentials needed
- Perfect for email warming
- Simple to set up and maintain

### Current Limitations
- Only 5 warming emails (warming1-5@kmjk.pro) are currently configured
- 360 metro-specific aliases need to be configured before sending
- Run `setup_email_aliases.sh` to configure them

### DNS Records
Ensure SPF and PTR records are configured before sending:
- SPF: Authorizes your VPS IP to send emails for kmjk.pro
- PTR: Reverse DNS maps IP to hostname

Without proper DNS, emails will be rejected or marked as spam.

---

## 📊 TEST RESULTS

When you run the test script, you'll see:

```
============================================================
📧 Email Test Sender for kmjk.pro
============================================================
📋 Total emails to process: 360
📨 Recipient: hercules71185@gmail.com
⏱️  Delay between sends: 3 seconds
🔧 SMTP Server: localhost:25 (local Postfix)
🎯 Mode: LIVE
============================================================

🔍 Checking Postfix status...
✅ Postfix is running

[1/360] Sending from projects-tri@kmjk.pro...
   ✅ Sent successfully

[2/360] Sending from estimates-tri@kmjk.pro...
   ✅ Sent successfully

...

============================================================
📊 SEND SUMMARY
============================================================
✅ Successful: 360
❌ Failed: 0
⏱️  Total time: 1080.0 seconds
📈 Average: 3.0 seconds per email
============================================================

📬 Checking mail queue...
   Queue: Mail queue is empty
```

---

## 🐛 TROUBLESHOOTING

### Issue: Postfix is not running
**Solution:**
```bash
sudo systemctl start postfix
sudo systemctl enable postfix  # Start on boot
```

### Issue: Email bounces with "Sender address rejected"
**Cause:** Email not configured in virtual aliases

**Solution:**
```bash
sudo bash setup_email_aliases.sh
```

### Issue: Email goes to spam folder
**Cause:** DNS records (SPF/PTR) not configured

**Solution:**
- Verify SPF: `dig txt kmjk.pro +short`
- Verify PTR: `dig -x 107.172.20.181 +short`
- See `DNS_CONFIGURATION_GUIDE.md` for setup instructions

### Issue: "Permission denied" when accessing Postfix files
**Solution:** Run commands with `sudo`

### Issue: Script can't find email list file
**Cause:** EMAIL_LIST_FILE path incorrect

**Solution:**
```bash
# Verify file exists
ls -la /home/chris/.openclaw/workspace/EMAIL-LIST.txt

# If missing, copy it from workspace
cp EMAIL-LIST.txt /home/chris/.openclaw/workspace/
```

---

## 📝 EMAIL WARMING STRATEGY

### Recommended Schedule

**Week 1-2:** Ramp-up phase
- Send 5-10 emails/day
- Monitor for bounces
- Check spam folder placement

**Week 3-4:** Growth phase
- Send 20-50 emails/day
- Monitor engagement metrics
- Adjust based on results

**Week 5+:** Full production
- Send up to 100+ emails/day
- Maintain good deliverability
- Track reputation scores

### Monitoring

**What to track:**
- Bounce rate (target: <5%)
- Spam complaint rate (target: <0.3%)
- Open rate (target: >30%)
- Reply rate (target: >5% for warming emails)

**Tools:**
- Mail logs: `sudo tail -f /var/log/mail.log`
- Queue status: `sudo mailq`
- Deliverability: Gmail Postmaster Tools

---

## 🆘 NEED HELP?

**Documentation:**
- `EMAIL_CONFIGURATION_REPORT.md` - Full analysis and setup guide
- `DNS_CONFIGURATION_GUIDE.md` - DNS setup instructions
- `POSTFIX_SETUP_SUMMARY.md` - Postfix configuration details

**Quick Commands:**
```bash
# Check if script works
python3 send_test_emails.py --test --dry-run

# Verify Postfix is configured
sudo postconf | grep -E '(virtual|canonical)'

# Check if emails are configured
grep "@kmjk.pro" /etc/postfix/virtual | wc -l
```

---

**Last Updated:** 2026-02-16
**Generated By:** AI Coding Specialist Subagent
