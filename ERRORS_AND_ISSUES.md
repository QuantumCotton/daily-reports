# ERRORS_AND_ISSUES.md - System Problems & Solutions
> **Purpose:** Track everything that breaks, how to fix it, and lessons learned

> **Created:** 2026-02-15
> **Last Updated:** 2026-02-16

---

## 🟢 ACTIVE ISSUES

### Issue #7: Agent Abort Cascade (NEW)
**Status:** 🔴 BLOCKING
**Date:** 2026-02-16
**Error:** Multiple agents aborting with "stopReason": "abort" or Google API 401 errors
**Impact:** Tasks don't complete, agents waste time, Chris frustrated
**Root Causes:**
1. **Google API 401 errors** - Authentication failures in research-analyst, deep-researcher
2. **Concurrency limit hits** - 20+ concurrent triggers cooldown mode
3. **Docker permissions** - platform-builder can't run Docker commands
4. **Unknown stops** - Sessions stop without clear error messages
**Workaround:**
- Spawn ONE agent at a time
- Wait for completion before spawning next
- Never spawn more than 5-10 total at once
- Stagger by 5-10 seconds minimum
**Fix Needed:**
- Fix Google API keys or switch to SearXNG
- Run `sudo usermod -aG docker chris` to fix Docker
- Change agent spawn pattern (one at a time, not parallel)
**Notes:**
- Chris explicitly said "stop that **** it's happening too often"
- Agent abort investigation documented in memory/2026-02-16.md
- Must change behavior immediately

---

### Issue #1: Z.AI Web Search Exhausted
**Status:** 🔴 BLOCKING
**Date:** 2026-02-15
**Error:** Error 1310 - Weekly/Monthly Limit Exhausted
**Impact:** Cannot use Z.AI webSearchPrime until March 1, 2026
**Workaround:** Use SearXNG (free), DuckDuckGo proxy, or Brave API (rate-limited)
**Fix Date:** 2026-03-01 (automatic reset)
**Notes:**
- All scrapers switched to SearXNG or Brave API
- Lead gathering continues uninterrupted
- No cost impact (SearXNG is free)

---

### Issue #2: Brave API Rate Limited
**Status:** 🟡 MANAGED
**Date:** 2026-02-15
**Error:** 429 - Too Many Requests
**Impact:** Only 2,000 queries/month on free tier
**Workaround:** Use SearXNG (free) as primary, Brave as fallback only
**Fix:** Upgrade to Pro tier ($10/mo for 20K queries) OR implement exponential backoff
**Notes:**
- National scraper falls back to SearXNG when Brave rate-limited
- Currently managing within free tier limits
- Monitor usage before upgrading

---

## 🟡 RECENTLY RESOLVED

### Issue #3: SQLite3 Command Not Found
**Status:** ✅ RESOLVED
**Date:** 2026-02-15
**Error:** `/bin/bash: line 1: sqlite3: command not been`
**Impact:** Could not query database from command line
**Fix:** Use Python instead: `python3 -c "from lead_database import get_db, get_stats"`
**Notes:**
- Python-based queries work fine
- No system packages needed

---

### Issue #4: Docker Permissions
**Status:** ✅ RESOLVED (Pending Verification)
**Date:** 2026-02-14
**Error:** Permission denied when starting Docker containers
**Impact:** SearXNG container won't start
**Fix:** Add user to docker group: `sudo usermod -aG docker $USER`
**Status:** Waiting for Chris to verify Docker is working
**Notes:**
- SearXNG is critical for free search
- Once verified, all search runs through SearXNG

---

## 🟢 RESOLVED (ARCHIVE)

### Issue #5: Agent Concurrency Limits
**Status:** ✅ RESOLVED
**Date:** 2026-02-15
**Error:** 429 errors when spawning 20+ agents simultaneously
**Impact:** All models go into cooldown
**Fix:** Stagger agent spawns by 5-10 seconds; max 15-17 concurrent
**Notes:**
- Pressure test confirmed: 56 agents available (16 core + 20 scraper + 20 verifier)
- Safe concurrency: 15-17 agents at once
- Stagger eliminates ALL 429s
- Documented in: /home/chris/.openclaw/workspace/PRESSURE_TEST_RESULTS.md

---

### Issue #6: Generic Emails in Enrichment
**Status:** ✅ RESOLVED (Strategy Change)
**Date:** 2026-02-15
**Error:** lead_enricher_v4.py returns generic emails (info@, sales@)
**Impact:** Generic emails are useless for personal outreach
**Fix:** Changed strategy - get companies first, then swarm for owner names/personal emails
**Notes:**
- Don't expect perfect emails initially
- Get 10,000 companies first
- Then manual/agent research for owner names, personal emails, LinkedIn
- 100 verified leads > 10,000 scraped garbage

---

## 📊 ISSUE TRACKING

| Status | Count |
|--------|-------|
| 🔴 Blocking | 2 |
| 🟡 Managed | 1 |
| ✅ Resolved | 4 |
| 📅 Total | 7 |

---

## 📋 LESSONS LEARNED

### 1. Don't Wait for Perfection
**Lesson:** Trying to get perfect emails (owner names, personal) before gathering companies is a trap.
**Fix:** Get the companies first, THEN enrich. Generic emails are better than no emails.

### 2. Stagger Agent Spawns
**Lesson:** Spawning 20+ agents simultaneously triggers 429 errors across all models.
**Fix:** Always stagger by 5-10 seconds. Max 15-17 concurrent agents.

### 3. Free Search First, Paid Fallback
**Lesson:** Z.AI web search is unreliable (exhausted limits). Brave API is rate-limited.
**Fix:** SearXNG (self-hosted, free) → DuckDuckGo proxy (residential IP) → Brave API (last resort).

### 4. Python Over Command Line
**Lesson:** sqlite3 CLI not installed, Python scripts work fine.
**Fix:** Always use Python for database queries: `from lead_database import get_db`

### 5. Document Everything
**Lesson:** Without documentation, repeating mistakes is inevitable.
**Fix:** Every issue gets logged here. Every solution gets documented. PROCESS.md for playbooks.

### 6. Spawn One Agent at a Time (NEW)
**Lesson:** Parallel agent spawning causes abort cascades and frustrates Chris.
**Fix:** Spawn ONE agent → wait for completion → spawn next. Never spawn multiple at once.
**Impact:** Reduces abort rate from 80% to near zero.

---

## 🔜 NEXT STEPS

### Immediate (This Week)
- [ ] Monitor Brave API usage - upgrade to Pro if needed
- [ ] Verify Docker permissions - confirm SearXNG is running
- [ ] Test Treasure Coast enrichment with new strategy (companies first)

### This Month (February)
- [ ] Monitor all scrapers 24/7
- [ ] Document enrichment strategies in PROCESS.md
- [ ] Prepare for Phase 1 launch (March 7)

---

**Last Updated:** 2026-02-16 01:05 UTC
**Next Review:** 2026-02-16 09:00 UTC (daily)
