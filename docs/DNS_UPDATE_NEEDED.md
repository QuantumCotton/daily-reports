# DNS UPDATE REQUIRED - kmjk.pro

## Current SPF Record Found
```
"v=spf1 include:zohomail.com ~all"
```

**Current Status:** Zoho Mail is configured to handle email for kmjk.pro

---

## REQUIRED UPDATE

### 1. Update SPF Record (MUST UPDATE)
Replace the existing SPF record with this one:

**Type:** TXT
**Host:** @
**Value:**
```
v=spf1 ip4:107.172.20.181 include:zohomail.com ~all
```

**What changed:**
- Added `ip4:107.172.20.181` to authorize your VPS IP
- Kept `include:zohomail.com` to maintain Zoho email functionality
- This allows BOTH your VPS and Zoho to send emails for kmjk.pro

---

## DNS PROVIDER SPECIFICS

### If using Cloudflare:
1. Go to DNS > kmjk.pro > TXT records
2. Find the existing SPF record (starts with `v=spf1`)
3. Edit it and add `ip4:107.172.20.181` before `include:zohomail.com`
4. Save changes

### If using Namecheap:
1. Go to Advanced DNS
2. Find the TXT record with SPF
3. Edit the value to include your IP
4. Save

### If using another provider:
Look for the existing SPF TXT record and update it to include your VPS IP.

---

## Verification

### After Updating DNS (Wait 10-30 minutes)
```bash
dig txt kmjk.pro +short
```

**Expected output:**
```
"zoho-verification=zb44884044.zmverify.zoho.com"
"v=spf1 ip4:107.172.20.181 include:zohomail.com ~all"
```

---

## Still Required

### 2. Request Reverse DNS (PTR) from RackNerd
**This is still needed and unchanged:**

**Request to RackNerd support:**
```
IP Address: 107.172.20.181
PTR Record: mail.kmjk.pro
```

---

## Testing After Both Are Set Up

1. **Verify SPF updated:**
   ```bash
   dig txt kmjk.pro +short
   ```

2. **Verify reverse DNS:**
   ```bash
   dig -x 107.172.20.181 +short
   ```

3. **Send test email:**
   ```bash
   echo "Test warming email - SPF and PTR configured" | mail -s "Warming Test Final" chris.cotton@kmjk.pro
   ```

4. **Check logs:**
   ```bash
   sudo tail -f /var/log/mail.log
   ```

---

## Summary

**Status:**
- ✅ SPF record exists for kmjk.pro
- ❌ SPF record needs UPDATE to include VPS IP (107.172.20.181)
- ❌ Reverse DNS (PTR) needs to be requested from RackNerd

**Two actions required:**
1. Update SPF record at your DNS provider (add `ip4:107.172.20.181`)
2. Request reverse DNS (PTR) from RackNerd support

**Current SPF:** `v=spf1 include:zohomail.com ~all`
**Updated SPF:** `v=spf1 ip4:107.172.20.181 include:zohomail.com ~all`

---

**Date:** 2026-02-15
**VPS IP:** 107.172.20.181
**Domain:** kmjk.pro
