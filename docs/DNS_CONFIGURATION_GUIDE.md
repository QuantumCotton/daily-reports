# DNS Configuration Guide for kmjk.pro

## Required DNS Records

### 1. SPF Record (REQUIRED)
```
Type: TXT
Host: @
Value: v=spf1 ip4:107.172.20.181 ~all
```

**What it does:** Authorizes your VPS IP (107.172.20.181) to send emails for kmjk.pro domain

**How to add:**
- Log into your DNS provider (e.g., Cloudflare, Namecheap, etc.)
- Add a new TXT record
- Leave Host field empty or use `@`
- Paste the value exactly as shown above

---

### 2. Reverse DNS (PTR Record) - REQUIRED
**Contact RackNerd Support** to set this up.

**Request details to send:**
```
IP Address: 107.172.20.181
PTR Record: mail.kmjk.pro
```

**How to request:**
1. Login to RackNerd client area
2. Open a support ticket
3. Or use their live chat
4. Provide the IP and desired hostname above

**Note:** PTR records are managed by your hosting provider (RackNerd), not your DNS provider.

---

## Optional Records (For Future Enhancement)

### 3. DKIM Record (Add Later)
**After setting up DKIM:**
```
Type: TXT
Host: default._domainkey
Value: [DKIM public key from opendkim-genkey]
```

### 4. DMARC Record (Add Later)
```
Type: TXT
Host: _dmarc
Value: v=DMARC1; p=none; rua=mailto:dmarc@kmjk.pro
```

**Policy explanation:**
- `p=none` - Monitor only, don't reject mail (good for initial warming)
- `p=quarantine` - Move suspicious mail to spam
- `p=reject` - Reject suspicious mail (use after reputation is built)

---

## Verification Commands

### Check SPF Record
```bash
dig txt kmjk.pro +short
```

**Expected output:**
```
"v=spf1 ip4:107.172.20.181 ~all"
```

### Check Reverse DNS (PTR)
```bash
dig -x 107.172.20.181 +short
```

**Expected output:**
```
mail.kmjk.pro.
```

### Check All Records
```bash
# SPF
dig txt kmjk.pro +short

# MX (mail exchange)
dig mx kmjk.pro +short

# A record
dig kmjk.pro +short

# Reverse DNS
dig -x 107.172.20.181 +short
```

---

## Testing After DNS Setup

### 1. Wait for Propagation
DNS changes can take 10 minutes to 24 hours to propagate globally.

### 2. Verify DNS Records
Run the verification commands above.

### 3. Send Test Email
```bash
echo "Test warming email - SPF and PTR configured" | mail -s "Warming Test Final" chris.cotton@kmjk.pro
```

### 4. Check Mail Logs
```bash
sudo tail -f /var/log/mail.log
```

### 5. Check Mail Queue
```bash
sudo mailq
```

---

## Common Issues

### Issue: SPF Record Not Propagating
**Solution:**
- Wait up to 24 hours
- Clear local DNS cache: `sudo systemd-resolve --flush-caches`

### Issue: Reverse DNS Not Working
**Solution:**
- Contact RackNerd support
- Verify they've set the PTR record correctly
- Wait 24-48 hours for global propagation

### Issue: Email Still Bouncing
**Check:**
1. SPF record is correct
2. Reverse DNS is set to mail.kmjk.pro
3. Postfix hostname is set to mail.kmjk.pro (`postconf myhostname`)
4. Server IP matches SPF record (`ip addr show`)

---

## Deliverability Checklist

- [ ] SPF record added to DNS
- [ ] SPF record verified with dig command
- [ ] Reverse DNS requested from RackNerd
- [ ] Reverse DNS verified with dig -x command
- [ ] Test email sent successfully
- [ ] Email received in inbox (not spam folder)
- [ ] Monitor mail logs for 24 hours
- [ ] Start gradual email warming (5-10 emails/day)

---

**Setup Date:** 2026-02-15
**VPS IP:** 107.172.20.181
**Domain:** kmjk.pro
