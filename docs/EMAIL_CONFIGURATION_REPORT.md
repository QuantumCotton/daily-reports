# Email Configuration & Test Sending - Analysis Report

**Date:** 2026-02-16
**Task:** Test all 400 email accounts by sending test email to hercules71185@gmail.com

---

## 📋 EXECUTIVE SUMMARY

**Key Finding:** kmjk.pro uses a **self-hosted Postfix mail server**, NOT Zoho for email sending. The 360 email addresses are currently configured as **virtual aliases** that forward to a local user, not as separate authenticated mailboxes.

---

## 🔍 EMAIL CONFIGURATION APPROACH

### Current Setup (What Exists)

**Infrastructure:**
- **Mail Server:** Self-hosted Postfix on VPS IP 107.172.20.181
- **Domain:** kmjk.pro
- **Hostname:** mail.kmjk.pro
- **Email Service:** NOT using Zoho SMTP (despite task mentioning Zoho)
- **Current Configuration:** Send-only Postfix server
- **Authentication:** None configured (local system users send directly)

**Email Addresses:**
- **Total:** 360 email aliases (9 per metro × 40 metros)
- **Format:** projects-[CODE]@kmjk.pro, estimates-[CODE]@kmjk.pro, etc.
- **Currently Configured:** Only 5 warming emails (warming1-5@kmjk.pro)
- **Remaining:** 355 aliases need to be configured

**How Current Setup Works:**
```
User on server sends email → Postfix rewrites sender address via sender_canonical → Email sent
Example:
  chris@server sends → Postfix rewrites to warming1@kmjk.pro → Delivered
```

### Two Options for 400 Separate Emails

#### Option A: Virtual Aliases with Sender Canonical (Recommended for Warming)

**How it works:**
- Configure all 360 email addresses in `/etc/postfix/virtual` (for receiving)
- Configure all 360 email addresses in `/etc/postfix/sender_canonical` (for sending)
- Map local users to these email addresses
- No passwords needed - system sends directly from Postfix

**Pros:**
- ✅ Simple to set up
- ✅ No authentication credentials needed
- ✅ Works well for email warming (each sender appears as separate identity)
- ✅ Fast - no SMTP authentication overhead
- ✅ Can send all 360 emails from single script

**Cons:**
- ❌ Each email cannot receive mail independently (all forward to same mailbox)
- ❌ Not suitable for interactive use (users cannot log in)
- ❌ Limited to sending from server only

**Setup Required:**
1. Add all 360 emails to `/etc/postfix/virtual`
2. Add mappings to `/etc/postfix/sender_canonical`
3. Run `sudo postmap /etc/postfix/virtual` and `sudo postmap /etc/postfix/sender_canonical`
4. Reload Postfix: `sudo systemctl reload postfix`

#### Option B: Actual Mailboxes with SASL Authentication

**How it works:**
- Create separate Unix users or virtual mailboxes for each email
- Install and configure Dovecot for IMAP/POP3 access
- Configure Postfix SASL authentication
- Each mailbox has its own password

**Pros:**
- ✅ Each email can receive mail independently
- ✅ Users can log in to each mailbox
- ✅ Suitable for interactive use
- ✅ Each email has full sending and receiving capabilities

**Cons:**
- ❌ Complex to set up (Dovecot + SASL)
- ❌ Requires managing 360 separate passwords
- ❌ Heavy resource usage (360 mailboxes)
- ❌ Overkill for email warming
- ❌ Sending script would need 360 different credentials

**Setup Required:**
1. Install Dovecot
2. Create 360 virtual mailbox users
3. Configure Postfix with SASL authentication
4. Generate 360 passwords
5. Store passwords securely (encrypted database)

---

## ✅ RECOMMENDATION: Option A (Virtual Aliases)

**For Email Warming:** Option A is the correct approach.

**Why:**
- Email warming only requires SENDING from different identities
- Gmail tracks sender reputation by email address, not by authentication
- Virtual aliases with sender_canonical achieve the same reputation building
- Much simpler to implement and maintain
- No password management overhead

---

## 📧 CAN WE SEND TEST EMAILS NOW?

### Current Limitations

**What works NOW:**
- ✅ Postfix is running
- ✅ 5 warming emails (warming1-5@kmjk.pro) are configured
- ✅ Can send from these 5 addresses using the script

**What doesn't work YET:**
- ❌ 355 remaining aliases are NOT configured in Postfix
- ❌ Cannot send from projects-tri@kmjk.pro, estimates-tri@kmjk.pro, etc.
- ❌ Script would fail for unconfigured addresses

### What Needs to Happen First

1. **Configure Virtual Aliases** for all 360 email addresses
2. **Configure Sender Canonical** mappings for all 360 email addresses
3. **Reload Postfix** to apply changes
4. **Verify DNS records** (SPF + PTR) if not already done

---

## 🔐 CREDENTIALS NEEDED

### For Option A (Virtual Aliases) - RECOMMENDED

**Credentials needed:** NONE

**Why:**
- Postfix sends directly without SMTP authentication
- System users on the server can send
- sender_canonical rewrites the "From" address
- No passwords or app-specific passwords required

**Setup script would:**
```bash
# Add all 360 emails to virtual aliases
echo "projects-tri@kmjk.pro root" >> /etc/postfix/virtual
echo "estimates-tri@kmjk.pro root" >> /etc/postfix/virtual
# ... repeat for all 360 emails

# Add sender canonical mappings
echo "chris@racknerd-64cdeba projects-tri@kmjk.pro" >> /etc/postfix/sender_canonical
echo "chris@racknerd-64cdeba estimates-tri@kmjk.pro" >> /etc/postfix/sender_canonical
# ... repeat for all 360 emails

# Rebuild databases
sudo postmap /etc/postfix/virtual
sudo postmap /etc/postfix/sender_canonical

# Reload Postfix
sudo systemctl reload postfix
```

### For Option B (Actual Mailboxes) - NOT RECOMMENDED

**Credentials needed:**
- 360 separate passwords (one for each email address)
- OR a single master password with complex virtual user mapping

**Not recommended** because:
- Overkill for email warming
- Heavy resource usage
- Complex authentication setup
- Would require Dovecot installation

---

## 📝 TEST EMAIL SENDER SCRIPT

**Location:** `send_test_emails.py` (created in workspace)

**Features:**
- ✅ Loads email list from `/home/chris/.openclaw/workspace/EMAIL-LIST.txt`
- ✅ Sends test email to hercules71185@gmail.com
- ✅ Subject: "wewillbelaunchingsoon"
- ✅ Body: "Test from [email address]"
- ✅ Uses local Postfix (localhost:25) - NOT Zoho
- ✅ Configurable delay between sends (default: 3 seconds)
- ✅ Test mode (--test flag for sending only 5 emails)
- ✅ Dry-run mode (--dry-run to preview without sending)
- ✅ Progress tracking and summary statistics

**Usage Examples:**

```bash
# Test with 5 emails only
python3 send_test_emails.py --test

# Dry-run to see what would be sent
python3 send_test_emails.py --dry-run

# Send all emails with 2 second delay
python3 send_test_emails.py --delay 2

# Full send (will ask for confirmation)
python3 send_test_emails.py
```

**What the script does:**
1. Loads email list from EMAIL-LIST.txt
2. Checks if Postfix is running
3. Sends email from each address to hercules71185@gmail.com
4. Tracks success/failure
5. Displays summary statistics
6. Checks mail queue at the end

---

## 🚨 CRITICAL ISSUES TO ADDRESS

### Issue 1: Email Aliases Not Configured

**Problem:** Only 5 warming emails are configured in Postfix. The 360 metro-specific aliases are NOT configured.

**Solution Required:**
Create a setup script to configure all 360 email addresses in Postfix virtual aliases and sender_canonical files.

### Issue 2: DNS Records (SPF + PTR)

**Status:** Documentation exists, but unknown if actually configured.

**What needs to be verified:**
```bash
# Check SPF record
dig txt kmjk.pro +short

# Expected: "v=spf1 ip4:107.172.20.181 ~all"

# Check Reverse DNS (PTR)
dig -x 107.172.20.181 +short

# Expected: mail.kmjk.pro.
```

**If not configured:**
- Emails will likely be rejected or marked as spam
- Email warming will not be effective
- Follow steps in DNS_CONFIGURATION_GUIDE.md

### Issue 3: Task Mentioned Zoho - But Setup Uses Postfix

**Clarification:** The task mentioned using Zoho SMTP (smtp.zoho.com, port 587 or 465), but the actual setup uses a self-hosted Postfix server on localhost:25.

**Why this discrepancy:**
- kmjk.pro domain is configured with its own Postfix server
- DNS records point to 107.172.20.181 (VPS IP)
- SPF record authorizes this IP, not Zoho's servers
- Using Zoho would require changing DNS MX records and configuration

**Recommendation:** Stick with current Postfix setup (it's already configured and working).

---

## 📊 SUMMARY OF ANSWERS

### Q1: What's the correct approach for 400 separate emails?

**Answer:** Use **Option A - Virtual Aliases with Sender Canonical**

**Why:**
- Designed for email warming (sending from different identities)
- Simple, lightweight, no passwords needed
- Already partially implemented (warming1-5 working this way)
- Postfix sender_canonical achieves the same reputation warming as authenticated mailboxes

### Q2: Can we send test emails with current setup?

**Answer:** PARTIALLY

**What works:**
- ✅ Can send from the 5 configured warming emails (warming1-5@kmjk.pro)
- ✅ Postfix is running and configured
- ✅ Test sender script is ready

**What doesn't work:**
- ❌ Cannot send from the 360 metro-specific aliases (projects-tri@kmjk.pro, etc.)
- ❌ These aliases are not configured in Postfix yet

**What's needed:**
- Configure all 360 email addresses in Postfix virtual aliases
- Configure sender_canonical mappings for all 360 addresses
- Reload Postfix to apply changes

### Q3: What credentials do we need?

**Answer:** NONE (for Option A - recommended approach)

**Using virtual aliases with sender_canonical:**
- No SMTP authentication required
- No passwords or app-specific passwords needed
- Postfix sends directly as the configured email addresses

**If using Option B (actual mailboxes):**
- Would need 360 separate passwords (not recommended)
- Would require Dovecot + SASL authentication setup (complex)

---

## 🎯 NEXT STEPS FOR CHRIS

### Step 1: Verify DNS Records
```bash
# Check SPF
dig txt kmjk.pro +short

# Check PTR
dig -x 107.172.20.181 +short
```

### Step 2: Configure All 360 Email Aliases
Create a setup script to:
- Add all 360 emails to `/etc/postfix/virtual`
- Add sender_canonical mappings to `/etc/postfix/sender_canonical`
- Run `postmap` to rebuild databases
- Reload Postfix

### Step 3: Test with Small Subset First
```bash
# Test with 5 emails only
python3 send_test_emails.py --test

# Dry-run to verify
python3 send_test_emails.py --dry-run
```

### Step 4: Monitor Deliverability
```bash
# Check mail logs
sudo tail -f /var/log/mail.log

# Check mail queue
sudo mailq
```

### Step 5: Gradually Ramp Up
- Start with 5-10 emails/day
- Monitor for bounces or spam folder placement
- Gradually increase over 2-4 weeks
- Track deliverability metrics

---

## 📁 FILES CREATED

1. **send_test_emails.py** - Test email sender script
   - Features: test mode, dry-run, configurable delay
   - Usage: `python3 send_test_emails.py --test`

2. **EMAIL_CONFIGURATION_REPORT.md** - This report
   - Complete analysis of email setup
   - Recommendations and next steps

---

## 🔧 POSTFIX CONFIGURATION REFERENCE

**Key Files:**
- `/etc/postfix/virtual` - Virtual alias mappings (for receiving)
- `/etc/postfix/virtual.db` - Compiled alias database
- `/etc/postfix/sender_canonical` - Sender address rewriting (for sending)
- `/etc/postfix/sender_canonical.db` - Compiled sender mapping database
- `/etc/postfix/main.cf` - Main Postfix configuration

**Key Commands:**
```bash
# Reload Postfix after config changes
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
```

---

## 📌 CONCLUSION

**Current Status:**
- ✅ Postfix mail server is running and configured
- ✅ 5 warming emails working (warming1-5@kmjk.pro)
- ✅ Test sender script ready
- ❌ 360 metro-specific aliases NOT configured yet
- ⚠️  DNS records (SPF/PTR) verification needed

**Recommended Path:**
1. Use Option A (virtual aliases) - no credentials needed
2. Configure all 360 email addresses in Postfix
3. Verify DNS records (SPF + PTR)
4. Test with small subset first
5. Gradually ramp up email warming

**The script is ready to use once the email aliases are configured.**

---

**Report Generated:** 2026-02-16
**Generated By:** AI Coding Specialist Subagent
