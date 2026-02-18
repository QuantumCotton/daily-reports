# QUICK START - Multi-IMAP Unified Inbox

## Status: ✅ READY TO USE

All files are in place. Follow these steps to get started.

---

## STEP 1: Configure Email Passwords (5 minutes)

### Option A: Config File (Recommended)

Create `/home/chris/.openclaw/config/email_accounts.json`:

```bash
cat > /home/chris/.openclaw/config/email_accounts.json << 'EOF'
{
  "chris@kmjk.pro": "YOUR_PASSWORD",
  "projects-tc@kmjk.pro": "YOUR_PASSWORD",
  "estimates-tc@kmjk.pro": "YOUR_PASSWORD",
  "site-tc@kmjk.pro": "YOUR_PASSWORD",
  "office-tc@kmjk.pro": "YOUR_PASSWORD",
  "sales-tc@kmjk.pro": "YOUR_PASSWORD",
  "support-tc@kmjk.pro": "YOUR_PASSWORD",
  "billing-tc@kmjk.pro": "YOUR_PASSWORD",
  "info-tc@kmjk.pro": "YOUR_PASSWORD",
  "team-tc@kmjk.pro": "YOUR_PASSWORD"
}
EOF
```

Secure the file:
```bash
chmod 600 /home/chris/.openclaw/config/email_accounts.json
```

### Option B: Environment Variables

```bash
# Add these to your ~/.bashrc or run before sync
export CHRIS_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export PROJECTS_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export ESTIMATES_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export SITE_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export OFFICE_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export SALES_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export SUPPORT_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export BILLING_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export INFO_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
export TEAM_TC_KMJK_PRO_PASSWORD="YOUR_PASSWORD"
```

---

## STEP 2: Run Initial Sync (2 minutes)

```bash
python3 /home/chris/.openclaw/bin/multi_imap_inbox.py
```

**Expected output:**
```
============================================================
Multi-IMAP Inbox Sync for Treasure Coast Emails
============================================================
Server: imap.zoho.com:993
Accounts: 10
Loaded config from /home/chris/.openclaw/config/email_accounts.json

============================================================
Syncing: chris@kmjk.pro
============================================================
Found X messages (limit: 50)
  [1/X] Added: Subject...
  [2/X] Added: Subject...
...
✓ Sync complete: X added, Y updated

... (repeats for all 10 accounts)

============================================================
SYNC COMPLETE
Total messages processed: XX
Database: /home/chris/.openclaw/data/inbox.db
============================================================
```

---

## STEP 3: Access Dashboard

### Option A: Start API Server (Recommended for full features)

```bash
# Terminal 1: Start API server
python3 /home/chris/.openclaw/bin/inbox_api_server.py
```

Then open in browser: **http://localhost:8080**

### Option B: Direct HTML File (Simpler, no API)

Open directly in browser:
```bash
firefox /home/chris/.openclaw/workspace/reports/inbox.html
# or
chromium /home/chris/.openclaw/workspace/reports/inbox.html
```

**Note:** Direct HTML won't show messages until you implement a static data export feature.

---

## Files Created

| File | Purpose | Location |
|------|---------|----------|
| `multi_imap_inbox.py` | Sync script - connects to all 10 emails separately | `/home/chris/.openclaw/bin/` |
| `inbox_api_server.py` | HTTP API server for dashboard | `/home/chris/.openclaw/bin/` |
| `inbox.html` | Dashboard web interface | `/home/chris/.openclaw/workspace/reports/` |
| `email_accounts.json.example` | Config template | `/home/chris/.openclaw/config/` |

---

## How It Works

### The Multi-IMAP Approach (CORRECT)

```
┌─────────────────┐
│   Dashboard     │
│  (Unified View) │
└────────┬────────┘
         │
         │ Reads from database
         │
┌────────▼────────┐
│   SQLite DB     │
│  inbox.db       │
└────────┬────────┘
         │
         │ Populated by sync script
         │
┌────────▼─────────────────────────────────────────────┐
│  multi_imap_inbox.py                                  │
│  ┌─────────────┐  ┌─────────────┐  ...  ┌───────────┐│
│  │  chris@     │  │ projects@   │  ...  │ team@    ││
│  │  kmjk.pro   │  │ kmjk.pro    │  ...  │ kmjk.pro ││
│  └─────────────┘  └─────────────┘  ...  └───────────┘│
│       │                │                     │      │
│       └────────────────┴─────────────────────┘      │
│                       │                               │
│               IMAP Connections                        │
│               (Separate for each)                     │
└───────────────────────┼───────────────────────────────┘
                        │
                imap.zoho.com:993
```

**Key Points:**
- ✅ Each email connects via IMAP separately
- ✅ Each email warms independently (maintains own reputation)
- ✅ Dashboard just aggregates the view
- ✅ NO forwarding involved

---

## Automated Sync (Optional)

Add to crontab to sync every 15 minutes:

```bash
crontab -e
```

Add this line:
```
*/15 * * * * /home/chris/.openclaw/bin/multi_imap_inbox.py >> /var/log/inbox-sync.log 2>&1
```

---

## Troubleshooting

### "No credentials found"
→ Create `/home/chris/.openclaw/config/email_accounts.json` with passwords

### "IMAP error"
→ Check password is correct for that email account
→ Verify IMAP is enabled in Zoho settings

### Dashboard shows no messages
→ Run `multi_imap_inbox.py` first to sync
→ Check `/home/chris/.openclaw/data/inbox.db` exists and has data

### API server won't start
→ Port 8080 might be in use. Edit `inbox_api_server.py` to change PORT variable

---

## Next Steps

1. **Configure passwords** (STEP 1)
2. **Run initial sync** (STEP 2)
3. **Start API server** and access dashboard at http://localhost:8080
4. **Set up cron** for automated sync (optional)

Each of the 10 Treasure Coast emails will now warm independently! 🎉
