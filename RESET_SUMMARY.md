# RESET SUMMARY - Quick Context
# Last Updated: 2026-02-15 06:30 UTC

## WHO AM I
I'm **GlitchGo** — Chris's best friend and operations director for Elite Service Hub.
- **Role:** Architect, coordinator, overseer — I don't execute, I orchestrate
- **Personality:** Direct, honest, construction-industry aware, data-driven, proactive
- **Philosophy:** "We don't build anything. We control our genius minions."

## PRESSURE TEST RESULTS (2026-02-15 06:30 UTC)

### Concurrency Limits CONFIRMED

| Model | Route | Concurrent Limit | Use For |
|-------|--------|----------------|----------|
| **glm-4.6** | zai/openai | 2 | Complex coordination tasks (deep-researcher, lead-scout) |
| **glm-4.5** | zai | 10 | High-volume bulk work (scrapers, verifiers, most agents) ✅ |
| **glm-4.5-air** | zai | 10+ | Fast parallel work (same as 4.5) ✅ |
| glm-4.5 | openai | 7 | AVOID — falls back to 4.7-flash, hits 429s at 8+ |

**TOTAL CAPACITY: 17-20 concurrent agents maximum**
- **zai route:** 12-20 concurrent
- **openai route:** 5-7 concurrent
- **Hard ceiling:** 20+ simultaneous = all models go into cooldown simultaneously

### Critical Finding
**Stagger by 5-10 seconds ELIMINATES ALL 429s.**
- Test without stagger: 10+ spawns = multiple 429 errors
- Test with stagger (5-10s): Zero 429s, 100% success rate

### Full Documentation
**See:** `/home/chris/.openclaw/workspace/PRESSURE_TEST_RESULTS.md`

## AGENT INVENTORY (56 Total)

| Group | Count | Models | Purpose |
|-------|-------|--------|---------|
| **Core Agents** (16) | Mixed (glm-4.6, 4.7, 4.5) | Coordinators, analysts, writers, builders |
| **Scraper Workers** (20) | glm-4.5 | Job Board, Craigslist, Directory (24/7 slow-roll) |
| **Verifier Workers** (20) | glm-4.5 | Email verification (nightly batches) |

### All Agent Names
**Core (16):**
deep-researcher, platform-builder, lead-scout, lead-generator, outreach-writer, coding-specialist, strategy-planner, research-analyst, creative-writer, seo-analyst, github-reviewer, email-quality, lead-scout-247, data-analyst, quality-control, compliance-officer

**Scrapers (20):**
scraper-worker-01 through scraper-worker-20

**Verifiers (20):**
verifier-worker-01 through verifier-worker-20

## OVERNIGHT STRATEGY (24/7)

### Capacity Plan
- **16-19 agents** constantly in staggered rotation
- **Safe zone:** 15-17 concurrent at once
- **Stagger delay:** 5-10 seconds between spawns
- **Never stops:** Scrapers on 20-minute cycles (Job Board + Craigslist)
- **Result:** Zero 429s, maximum throughput

### Agent Allocation Tonight
| Time (UTC) | Agents | Task |
|------------|--------|------|
| 06:20+ | 8-10 scrapers | Job Board (every 20 min), Craigslist (every 20 min) |
| Every 8h | 2-3 scrapers | Directory (3 metros per batch) |
| 03:00 UTC | 5 verifiers | Bulk email verification |
| Continuous | 2-3 core | Lead enrichment, Josue outreach drafts |

**Total overnight:** 25-36 agents working simultaneously in shifts**

## BUSINESS MODELS

### Elite Mail Platform ✅
**Status:** MVP READY (8 files built)
- **Location:** `/home/chris/.openclaw/workspace/elite-mail/`
- **Files:** index.html, app.py, config.py, requirements.txt, README.md, test_email.py, demo.py, start.sh
- **Revenue model:** 15% commission on contractor revenue
- **Pricing:** $50-100/mo per contractor
- **Target:** 5,000 contractors
- **ARR potential:** $1M+
- **15 metros identified:** San Jose, SF, Boston, NYC, DC, Seattle, Austin, Dallas, Miami, LA, SD, Denver, Phoenix, Philadelphia, Chicago, Atlanta, Houston
- **Email provider:** CHOOSE TONIGHT (Gmail Workspace recommended)
- **Accounts needed:** 5-10 per metro
- **Tech:** Multi-provider SMTP, self-healing reputation, bad-list-proof

### Elite Automated Services (NEW - Blueprint Ready)
**What it is:** Chatbot system for plumbers/HVAC/electricians
**Features:**
- 24/7 intake (calls + texts)
- Auto-dispatch to available techs
- ETA tracking for customers (real-time)
- Auto work order generation
- Instant billing (text-to-pay)
- Emergency vs routine classification
- Siren alerts for emergencies

**Revenue model:** $100-300/mo per contractor
**Target:** 100 contractors within 6 months
**Monthly revenue:** $10K-30K

### Contractor Network (Phase Two)
**Target:** 15 high-income metros
**Goal:** 40+ contractors total
**Revenue per contractor:** $50K-100K/month
**Commission:** 15% after contractor gets paid

### Services We're Taking Over
1. **Epoxy flooring**
2. **Kitchen renovation**
3. **Bathroom renovation**
4. **Mobile detailing**

## CURRENT STATUS

### Lead Database
- **Total leads:** 19,158 (up from 19,127 yesterday - 31 new)
- **Location:** `/home/chris/.openclaw/workspace/leads/lead_bank.db`
- **Curated export:** `/home/chris/.openclaw/workspace/leads/master_leads.csv`

### Dashboard
- **URL:** http://107.172.20.181:8181/
- **Auth:** Chris/Cotton247
- **Status:** Auto-rebuilds every 30 min

### Josue (Primary Contractor)
- **Phone:** 772-323-3776
- **Company:** KMJK Group
- **Email:** info@kmjk.pro
- **Website:** https://kmjk.pro
- **Services:** Kitchen, bath, epoxy, handyman, roofing, gutters
- **Status:** Needs verified leads + outreach tonight

## PRIORITY TONIGHT

1. **Draft 20 Josue outreach emails** (focus on verified leads with owner names)
2. **Keep scrapers moving** (Job Board + Craigslist slow-roll, never stops)
3. **Choose Elite Mail email provider** (Gmail Workspace recommended)

## FILE LOCATIONS

| File | Path | Purpose |
|------|------|---------|
| MEMORY.md | workspace/MEMORY.md | Full system history and status |
| SOUL.md | workspace/SOUL.md | My personality, philosophy, doctrine |
| HEARTBEAT.md | workspace/HEARTBEAT.md | Automated task schedule |
| PRESSURE_TEST_RESULTS.md | workspace/PRESSURE_TEST_RESULTS.md | Concurrency limits documentation |
| RESET_SUMMARY.md | workspace/RESET_SUMMARY.md | This file — quick reference after chat reset |
| ERRORS_AND_ISSUES.md | workspace/ERRORS_AND_ISSUES.md | All problems tracked |

## HOW TO OPERATE AFTER RESET

1. **Read RESET_SUMMARY.md first** — contains everything you need to know
2. **Read MEMORY.md** — updated with pressure test results
3. **Read HEARTBEAT.md** — overnight strategy documented
4. **Read SOUL.md** — agent swarm doctrine updated
5. **Read PRESSURE_TEST_RESULTS.md** — full concurrency documentation

## KEY COMMANDS

```bash
# Check system status
openclaw gateway status

# Check active agents
sessions_list

# Check lead count
python3 -c "import sqlite3; conn = sqlite3.connect('/home/chris/.openclaw/workspace/leads/lead_bank.db'); print(conn.cursor().execute('SELECT COUNT(*) FROM leads').fetchone()[0])"

# Check scraper status
python3 ~/.openclaw/bin/job_board_scraper.py --status
python3 ~/.openclaw/bin/craigslist_scraper.py --status

# Test capacity (staggered spawns)
# Spawn 5 agents, wait 10s, spawn 5 more, etc.
```

## RULES TO REMEMBER

1. **Stagger spawns by 5-10 seconds** — prevents all 429s
2. **Never spawn 20+ simultaneously** — triggers cooldown on all models
3. **Use glm-4.5 (zai route)** for bulk work (10 concurrent, stable)
4. **Use glm-4.6** only for complex tasks (2 concurrent)
5. **Avoid openai route for glm-4.5** — unstable, 7 concurrent limit
6. **Keep scrapers moving 24/7** — slow-roll design (20-min cycles)
7. **100 verified leads > 10,000 scraped** — quality over quantity
8. **Platform-builder is READY** — MVP is built, not research

## WHAT WAS ACCOMPLISHED TODAY

- ✅ Confirmed Z.AI concurrency limits via pressure testing
- ✅ Tested both routes (zai + openai)
- ✅ Identified 56 agents (16 core + 20 scraper + 20 verifier)
- ✅ Designed overnight strategy (16-19 agents continuously)
- ✅ Elite Mail MVP built (8 files ready)
- ✅ Elite Automated Services blueprint ready
- ✅ 15 highest-income metros identified
- ✅ All knowledge files updated (MEMORY, SOUL, HEARTBEAT)

---

**Last Updated:** 2026-02-15 06:30 UTC
**Ready to reset chat. All systems documented.**
