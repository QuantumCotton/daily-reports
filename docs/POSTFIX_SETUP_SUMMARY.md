# Postfix Mail Server Setup - kmjk.pro
## VPS: 107.172.20.181
## Date: 2026-02-15

---

## ✅ COMPLETED TASKS

### 1. Postfix Installation
```bash
sudo apt update
sudo apt install postfix -y
```
- Postfix version 3.8.6 installed successfully
- Service is running (PID: 1249288)

### 2. Domain Configuration
**Files Modified:**
- `/etc/mailname` - Set to `kmjk.pro`
- `/etc/postfix/main.cf` - Configured for send-only operation

**Key Configuration Settings:**
```
myhostname = mail.kmjk.pro
myorigin = /etc/mailname  (reads kmjk.pro)
mydestination = localhost  (send-only)
inet_interfaces = loopback-only  (security)
inet_protocols = ipv4
relayhost =  (empty - direct delivery)
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
```

### 3. Virtual Mailboxes Created
Created virtual aliases for 5 test email accounts in `/etc/postfix/virtual`:
```
warming1@kmjk.pro → root
warming2@kmjk.pro → root
warming3@kmjk.pro → root
warming4@kmjk.pro → root
warming5@kmjk.pro → root
```

### 4. Sender Canonical Mapping
Created `/etc/postfix/sender_canonical` to map local senders to domain addresses:
```
chris@racknerd-64cdeba → warming1@kmjk.pro
root@racknerd-64cdeba → root@kmjk.pro
```

### 5. Postfix Database Files Created
```bash
sudo postmap /etc/postfix/virtual
sudo postmap /etc/postfix/sender_canonical
```

### 6. Mailutils Installed
```bash
sudo apt install mailutils -y
```

### 7. Email Test Performed
Test command executed:
```bash
echo "Test warming email #2 - sender should now be warming1@kmjk.pro" | mail -s "Warming Test #2" chris.cotton@kmjk.pro
```

**Result:**
- ✅ Sender address correctly shows as `warming1@kmjk.pro`
- ❌ Email rejected by Zoho MX server (expected - see below)

---

## ⚠️ CURRENT ISSUES

### Email Rejection (Expected)
The test email was rejected by Zoho's MX server with error:
```
541 5.7.1 Mail rejected due to antispam policy
```

**This is expected because:**
1. SPF record not yet configured in DNS
2. Reverse DNS (PTR record) not set up for 107.172.20.181
3. No DKIM/DMARC configured yet (as requested, to be added later)

---

## 🔧 REQUIRED ACTIONS FOR CHRIS

### 1. DNS: Add SPF Record
Add this TXT record to kmjk.pro DNS zone:

**Record Type:** TXT
**Host:** @
**Value:**
```
v=spf1 ip4:107.172.20.181 ~all
```

**Explanation:**
- `v=spf1` - SPF version 1
- `ip4:107.172.20.181` - Authorizes this IP to send email for kmjk.pro
- `~all` - Soft fail for other IPs (allows mail to be received but marked as suspicious)

### 2. Request Reverse DNS (PTR Record)
Contact RackNerd support to set up reverse DNS for 107.172.20.181:

**Request:**
```
IP: 107.172.20.181
PTR: mail.kmjk.pro
```

**How to request:**
- Open a support ticket at RackNerd client area
- Or use their live chat
- Include both IP address and desired hostname

---

## 📋 TEST RESULTS

### Mail Log Analysis
```bash
tail -20 /var/log/mail.log
```

**Key Finding:**
```
from=<warming1@kmjk.pro>, size=392, nrcpt=1 (queue active)
```

✅ Sender canonical mapping working correctly - outgoing email shows proper domain

### Test Email Status
- **From:** warming1@kmjk.pro ✅
- **To:** chris.cotton@kmjk.pro
- **Status:** Bounced (antispam policy) ❌
- **Reason:** Missing SPF + PTR records

---

## 📁 FILES CREATED/MODIFIED

### Configuration Files
1. `/etc/mailname` - Domain name (kmjk.pro)
2. `/etc/postfix/main.cf` - Main Postfix configuration
3. `/etc/postfix/main.cf.backup` - Backup of original config
4. `/etc/postfix/virtual` - Virtual email aliases
5. `/etc/postfix/virtual.db` - Hash database for aliases
6. `/etc/postfix/sender_canonical` - Sender address mapping
7. `/etc/postfix/sender_canonical.db` - Hash database for sender mapping

### Test Accounts (Virtual)
- warming1@kmjk.pro → root
- warming2@kmjk.pro → root
- warming3@kmjk.pro → root
- warming4@kmjk.pro → root
- warming5@kmjk.pro → root

---

## 🔍 POST-SETUP VERIFICATION COMMANDS

### Check Postfix Status
```bash
sudo systemctl status postfix
sudo postfix status
```

### View Configuration
```bash
sudo postconf -n
```

### Check Mail Queue
```bash
sudo mailq
```

### View Mail Logs
```bash
sudo tail -f /var/log/mail.log
```

### Test Sending Email (after DNS/PTR is set up)
```bash
echo "Test email from warming1" | mail -s "Test 1" chris.cotton@kmjk.pro
echo "Test email from warming2" | mail -s "Test 2" external@example.com
```

---

## 🎯 NEXT STEPS (After DNS/PTR Setup)

1. **Verify SPF Record**
   ```bash
   dig txt kmjk.pro +short
   ```
   Should show: `"v=spf1 ip4:107.172.20.181 ~all"`

2. **Verify Reverse DNS**
   ```bash
   dig -x 107.172.20.181 +short
   ```
   Should show: `mail.kmjk.pro`

3. **Re-test Email Delivery**
   ```bash
   echo "Test warming email - SPF and PTR configured" | mail -s "Warming Test Final" chris.cotton@kmjk.pro
   ```

4. **Monitor Deliverability**
   ```bash
   sudo tail -f /var/log/mail.log
   ```

5. **Future: Add DKIM/DMARC**
   - Install opendkim
   - Generate DKIM keys
   - Add DKIM TXT record to DNS
   - Add DMARC policy to DNS

---

## 📝 NOTES

- Postfix is configured for **send-only** operation (loopback-only interface)
- No IMAP/POP3 server (Dovecot) installed (not needed for warming)
- Test emails are mapped to local root user via virtual aliases
- Sender canonical mapping ensures outgoing mail shows proper domain
- Server hostname is set to mail.kmjk.pro for proper reverse DNS

---

## 🚀 READY FOR EMAIL WARMING

Once SPF and PTR records are configured:
1. Start warming gradually (send 5-10 emails per day)
2. Gradually increase volume over 2-4 weeks
3. Monitor deliverability and reputation
4. Add DKIM/DMARC when ready for production use

---

**Setup Date:** 2026-02-15 23:08 UTC
**Setup By:** AI Coding Specialist Subagent
**VPS IP:** 107.172.20.181
**Domain:** kmjk.pro
