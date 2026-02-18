# HEARTBEAT.md - Treasure Coast Focus
# Updated: 2026-02-17 16:55 UTC
# Priority: TREASURE COAST ONLY

## 🎯 PRIMARY OBJECTIVE
**CURRENT FOCUS: Treasure Coast ONLY (Josue/KMJK Group)**

**Target Cities:**
- Stuart, FL
- Jensen Beach, FL
- Port St. Lucie, FL
- Vero Beach, FL
- Sebastian, FL
- Palm City, FL
- Hobe Sound, FL
- Fort Pierce, FL

**MILESTONE FOR NATIONAL EXPANSION:**
- **Goal:** 500 TC leads with personal emails + business names
- **Current:** 424 TC person emails
- **Remaining:** 76 more needed
- **Once hit:** Begin national expansion

**Email Rules:**
- ✅ Personal emails (chris@company.com, john@business.com)
- ❌ No generic (info@, sales@, contact@, support@, admin@)

**Priority:**
1. **Website Revamp** - Specialize in high-quality paints & epoxy with microspheres/silane infusion
2. **Become the experts** - Position Josue/KMJK as THE authority on advanced coating tech
3. **TC Enrichment** - Get 76 more personal emails to hit 500 milestone
4. **NO NATIONAL EXPANSION** - Until 500 TC person emails reached

---

## 🌐 WEBSITE REVAMP PROJECT (NEW - 2026-02-17 17:26 UTC)

**Goal:** Reposition KMJK as experts in advanced coating technology

**Key Differentiators:**
- **Microspheres technology** - Superior durability and coverage
- **Silane infusion** - Advanced chemical bonding for longer life
- **High-quality paints** - Professional-grade, contractor-exclusive products

**Deliverables:**
1. [ ] Content creation - Technical articles on microspheres/silane tech
2. [ ] Service pages - Dedicated epoxy and coating specialty pages
3. [ ] Before/after gallery - Showcase advanced coating results
4. [ ] Expert positioning - "The Science Behind Our Coatings" section
5. [ ] Lead magnets - Free guides on coating technology for property managers

**Status:** 🆕 Just added - awaiting Chris's detailed requirements

**Status:**
- TC leads: 2,107 total
- TC emails: 850 (40%)
- TC person emails: 151 (for Josue's targets)
- TC enrichment: ✅ WORKING (16% rate)

---

## 📊 RATE LIMIT INTEL (FROM CHRIS)

- **Reset time:** Few minutes to 15 minutes
- **Time to hit cap:** 4h 45m of continuous use
- **When hit:** Wait 15 min, then resume
- **Two routers:** zai (87bb...) + openai (99a0...)
- **Tokens:** UNLIMITED (if error >5h, it's NOT tokens)

---

## ⏰ TREASURE COAST OPERATIONS (24/7)

### Active Scrapers (TC Focused):
- **TC Enricher**: Every 30 min (finding emails on TC business websites)
- **Job Board scraper**: Every 20 min (filtering for TC cities)
- **Craigslist scraper**: Every 20 min (filtering for TC cities)
- **Treasure Coast scraper**: Hourly (dedicated TC search)

### Priority Tasks:
1. **TC Enrichment** - Run tc_enricher.py continuously
2. **TC Lead Quality** - Verify emails are valid TC businesses
3. **Email Campaign Prep** - Prepare 151 TC person emails for Josue

### Next Week (Feb 22-28)
- Refine email templates per business type
- Test templates with small batch (50 emails)

---

## 🤖 AGENT ALLOCATION (15 CONCURRENT)

| Role | Count | Model | Task |
|------|-------|-------|------|
| Job Board Scrapers | 4 | glm-4.5 | Every 20 min, slow-roll |
| Craigslist Scrapers | 4 | glm-4.5 | Every 20 min, alternates |
| Lead Enrichers | 5 | glm-4.5 | Deep enrichment (names, personal emails) |
| Email Verifiers | 2 | glm-4.5 | SMTP verification |
| Coordinators | 2 | glm-4.6 | Monitoring, reporting |

**Total:** 17 agents (2 over, but staggered = safe)

---

## 📅 CRON SCHEDULE (36 HOURS)

```bash
# Every 30 min: Check rate limits and agent status
*/30 * * * * /home/chris/.openclaw/bin/check_agents.sh

# Every 20 min: Job Board scraper
*/20 * * * * python3 /home/chris/.openclaw/bin/job_board_scraper.py --cycle

# Every 20 min: Craigslist scraper (offset by 10 min)
10,30,50 * * * * python3 /home/chris/.openclaw/bin/craigslist_scraper.py --cycle

# Every 8 hours: Directory scraper
0 */8 * * * python3 /home/chris/.openclaw/bin/directory_scraper.py --max-metros 3

# Every 2 hours: Lead enrichment batch
0 */2 * * * python3 /home/chris/.openclaw/bin/lead_enricher_v4.py 50

# Every 2 hours: Email verification
30 */2 * * * python3 /home/chris/.openclaw/bin/apollo_guesser.py

# Daily 3 AM: Bulk verification
0 3 * * * python3 /home/chris/.openclaw/bin/bulk_verifier.py

# Every 30 min: Dashboard rebuild
*/30 * * * * python3 /home/chris/.openclaw/bin/market_dashboard.py

# Every 2 hours: GitHub push
45 */2 * * * cd /home/chris/daily-reports && git add -A && git commit -m "update" && git push

# Every 4 hours: Status report to file
0 */4 * * * python3 /home/chris/.openclaw/bin/status_report.py
```

---

## 🔔 HEARTBEAT REMINDERS (EVERY 30 MIN)

Add to cron or use OpenClaw cron system:

**Reminder Text:**
> "HEARTBEAT CHECK: All rate limits reset automatically. If error >5 hours, it's NOT tokens. Check agent status, verify scrapers running, confirm lead enrichment progress. Tokens are UNLIMITED."

---

## 📋 CONTACT INFO

- **Call Josue:** 772-323-3776
- **Text Chris:** 772-777-0622
- **Email:** info@kmjk.pro
- **Website:** https://kmjk.pro

---

## 🎯 TARGET CLIENTS (NOT CONTRACTORS)

1. Property management companies
2. Apartment complexes
3. HOAs
4. Auto dealerships
5. Restaurants/kitchens
6. Real estate investors
7. Warehouses
8. Hotels/resorts

**Services for them:**
- Epoxy flooring
- Kitchen renovation
- Bathroom renovation
- Mobile detailing
- Handyman services
- Roofing
- Gutters

---

## 📍 PRIORITY METROS (ONE AT A TIME)

**PHASE 1: Treasure Coast (Josue's home area)**
1. **Stuart, FL** (Josue's base - KMJK Group)
2. **Jensen Beach, FL**
3. **Port St. Lucie, FL**
4. **Vero Beach, FL**
5. **Sebastian, FL**

**PHASE 2: High-Income Metros**
6. San Jose, CA ($155K median)
7. San Francisco, CA
8. Boston, MA
9. New York, NY
10. Washington, DC
11. Seattle, WA
12. Austin, TX
13. Dallas, TX
14. Miami, FL
15. Los Angeles, CA

---

## 📊 METRICS TO TRACK

- Total leads enriched (names + personal emails)
- Metros completed
- Rate limit hits (and recovery time)
- Agents spawned
- Scrapers running
- Verification success rate

---

## 🚨 ERROR HANDLING

- **429 error:** Wait 5-10 min, retry with stagger
- **Rate limit:** Wait 15 min, resume
- **Timeout:** Check network, retry
- **If error >5h:** NOT tokens - check code/config
- **Agent crash:** Respawn with stagger

---

## 📁 FILE LOCATIONS

| File | Path |
|------|------|
| Lead Database | ~/.openclaw/workspace/leads/lead_bank.db |
| Verified Leads | ~/.openclaw/workspace/leads/VERIFIED_LEADS.csv |
| Master CSV | ~/.openclaw/workspace/leads/master_leads.csv |
| Status Reports | ~/.openclaw/workspace/reports/ |
| Agent Logs | ~/.openclaw/agents/*/sessions/*.jsonl |

---

**Last Updated:** 2026-02-15 18:55 UTC (90-Day Plan)
**Target:** 2026-05-15 (90 days - 4 contractors total)
