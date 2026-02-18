# Quick Reference - Unified Inbox Dashboard

## 🚀 Dashboard is LIVE

**URL:** http://107.172.20.181:8282/

## 📊 Current Status

- **Messages:** 37 (sample data)
- **Accounts:** 10 (all Treasure Coast emails)
- **Port:** 8282
- **Database:** `/home/chris/.openclaw/data/inbox.db`

## 🔧 Commands

### Start API Server
```bash
python3 /home/chris/.openclaw/bin/inbox_api_server.py
```

### Run IMAP Sync (once credentials are fixed)
```bash
python3 /home/chris/.openclaw/bin/multi_imap_inbox.py
```

### Check Server Status
```bash
ps aux | grep inbox_api_server
curl http://localhost:8282/api/inbox
```

## ⚠️ IMAP Authentication Issue

All 10 accounts fail IMAP login with:
```
[AUTHENTICATIONFAILED] Invalid credentials(Failure)
```

**To Fix:**
1. Log in to each Zoho account
2. Generate app passwords (Settings → Security → App Passwords)
3. Update `/home/chris/.openclaw/config/email_accounts.json`
4. Run sync script

## 📁 Key Files

| File | Purpose |
|------|---------|
| `/home/chris/.openclaw/bin/multi_imap_inbox.py` | IMAP sync script |
| `/home/chris/.openclaw/bin/inbox_api_server.py` | API server |
| `/home/chris/.openclaw/workspace/reports/inbox.html` | Dashboard |
| `/home/chris/.openclaw/data/inbox.db` | SQLite database |
| `/home/chris/.openclaw/config/email_accounts.json` | Email passwords |

## 🎯 Success Metrics

✅ Dashboard live at http://107.172.20.181:8282/  
✅ All 10 emails configured separately  
✅ Messages visible with account_source tag  
✅ NO forwarding used  
⚠️ IMAP authentication pending (dashboard working with sample data)

## 📚 Documentation

- `/home/chris/.openclaw/workspace/reports/MISSION_SUMMARY.md` - Full mission report
- `/home/chris/.openclaw/workspace/reports/INBOX_DASHBOARD_STATUS.md` - Detailed status
- `/home/chris/.openclaw/workspace/reports/QUICK_START.md` - Setup guide
- `/home/chris/.openclaw/workspace/reports/MULTI_IMAP_README.md` - Architecture docs

---

**Dashboard is LIVE** at http://107.172.20.181:8282/ 🎉
