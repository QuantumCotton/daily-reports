# PARALLEL EXECUTION ITINERARY
# Created: 2026-02-16 06:45 UTC
# Status: ALL SYSTEMS GO

## TASKS (ALL RUNNING SIMULTANEOUSLY)

### TASK 1: Email Warm-Up (400 emails)
**Agent:** platform-builder
**Status:** 🟢 Spawning
**Actions:**
- Configure 400 email aliases in Postfix
- Set up automated warm-up sequence
- Send test emails to hercules71185@gmail.com
- Subject: "wewillbelaunchingsoon"
- Track reputation metrics

### TASK 2: War Room Fix
**Agent:** coding-specialist
**Status:** 🟢 Spawning
**Actions:**
- Gateway restart (fixes advisor spawning)
- Test all 4 advisors (Musk, Thiel, Carmack, Jensen)
- Verify JSON responses with actual answers
- Update conversation threading

### TASK 3: Treasure Coast Enrichment (403 more needed)
**Agent:** lead-scout
**Status:** 🟢 Spawning
**Actions:**
- Scrape company websites for owner names
- Find personal emails (NOT info@, sales@, etc.)
- Verify via SMTP
- Update database with complete leads
- Target: 200+ by end of session

### TASK 4: National Lead Scraping (other metros)
**Agent:** lead-generator
**Status:** 🟢 Spawning
**Actions:**
- Continue Job Board scraper (24/7 via cron)
- Continue Craigslist scraper (24/7 via cron)
- Scrape San Jose, Dallas, SF, etc.
- Add to national database

### TASK 5: Unified Inbox Dashboard
**Agent:** coding-specialist
**Status:** 🟢 Spawning
**Actions:**
- Build multi-IMAP dashboard (NO forwarding)
- Connect to all 10 Treasure Coast emails separately
- Each email warms independently
- Aggregate view in dashboard

---

## AGENT ALLOCATION

| Agent | Task | Model | Priority |
|-------|------|-------|----------|
| platform-builder | Email warm-up | glm-4.7 | HIGH |
| coding-specialist-1 | War room fix | glm-4.5 | HIGH |
| lead-scout | Treasure Coast enrichment | glm-4.5 | HIGH |
| lead-generator | National scraping | glm-4.5 | MEDIUM |
| coding-specialist-2 | Inbox dashboard | glm-4.5 | HIGH |

**Total:** 5 agents running simultaneously
**Stagger:** 5-10 seconds between spawns
**Concurrency:** Safe (5 << 15 limit)

---

## DEPENDENCIES

**None.** All tasks can run in parallel.

---

## SUCCESS METRICS

- ✅ 400 emails configured + tests sent
- ✅ War room advisors answering (not session metadata)
- ✅ 200+ Treasure Coast complete leads
- ✅ 5,000+ national leads scraped
- ✅ Inbox dashboard live at http://107.172.20.181:8181/inbox.html

---

## BLOCKERS

**Email setup requires sudo** - Chris will run:
```bash
sudo bash /home/chris/.openclaw/bin/setup_email_aliases.sh
```

**Gateway restart required** for war room - Chris will run:
```bash
openclaw gateway restart
```

**Everything else:** Agents handle autonomously.

---

**EXECUTION START:** NOW
**ESTIMATED COMPLETION:** 30-60 minutes (all tasks in parallel)
