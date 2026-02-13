# MEMORY.md - GlitchGo Long-Term Memory

> Update after every significant session. This is your persistent brain.

## Core Documents (READ THESE FIRST)
- **GRAND-VISION.md** - The complete $50M+ global expansion plan
- **SOUL-v2.md** - My personality, philosophy, and agent orchestration doctrine
- **dashboard-revamp-log.md** - Current agent swarm project tracking
- **ESH_BLUEPRINT.md** - Full business plan reference (read-only)

## Mission
Elite Service Hub (Chris) connects contractors to work. Primary contractor: KMJK Group (Josue) in Jensen Beach, FL.
- **Phase 1 (NOW):** Get Josue $70K+ in kitchen/bath/epoxy projects
- **Phase 2:** Find more contractors in high-income markets (50 cities, 3-4 per city)
- **Phase 3:** Scale to international markets (UK, Australia, New Zealand, Canada)
- **End Game:** Global tradesman liberation network - make contractors millionaires, we make $150K each

## System Status (Updated: 2026-02-13 20:46 UTC)
- **Database (lead_bank.db):** 16,406 leads across 13 states, 80 cities
  - 10,546 clients, 5,290 contractors
  - All have emails, 192 metros, 43 states
- **CSV Export (master_leads.csv):** 785 curated leads
  - High: 465, Medium: 184, Low: 136
  - 727 with email, 314 SMTP verified
- **Dashboard:** http://107.172.20.181:8181/ (**HTTP Basic Auth protected**)
  - **Username:** Chris | **Password:** Cotton247
- **CRM Server:** Port 8181 - API endpoints for lead approval, queue management
- **Telegram:** @GlitchGobot -> chat_id 7881105163
- **GitHub reports:** QuantumCotton/daily-reports
- **All costs: $0** - Z.AI exhausted until March 1, 2026; OpenRouter free, Gemini free
- **Scripts:** 29 Python tools in ~/.openclaw/bin/

### Current Issues
- **Z.AI exhausted** until March 1, 2026 (Error 1310)
- **Brave API rate-limited** - 429 errors (2K/mo free tier)

## How to Search
```bash
# Z.AI search (EXHAUSTED until March 1, 2026)
exec python3 ~/.openclaw/bin/zai_search.py "your search query"
exec python3 ~/.openclaw/bin/zai_search.py --reader "https://url.com"

# Brave Search (current primary - rate limited)
exec python3 ~/.openclaw/bin/brave_search.py "your search query"
```

## What Works (Tested & Verified)
- Brave Search API: 10 results/query, 2K/mo free tier (currently rate-limited)
- national_scraper.py: 15 queries/batch, saves to SQLite database
- lead_database.py: SQLite manager with 192 metros, 30 client + 15 contractor categories
- apollo_guesser.py: Email pattern guessing via SMTP/MX verification
- market_dashboard.py: Auto-generates HTML dashboard every 30 min
- crm_server.py: REST API on port 8181 with approval workflow
- overnight_repo_agent.py: Multi-agent swarm (5 repos/night)
- Telegram: Working
- GitHub auto-push: Every 2 hours

## What Does NOT Work (Skip These)
- Z.AI webSearchPrime: EXHAUSTED until March 1, 2026 (Error 1310)
- Google via web_fetch (anti-bot)
- Facebook (login wall)
- Nextdoor (login wall)

## Key Repositories
- **QuantumCotton/KMJK** - PRIVATE - Main KMJK website (kmjk.pro)
- **QuantumCotton/kmjknonai** - PUBLIC - Non-AI version
- **QuantumCotton/daily-reports** - PUBLIC - Daily operations reports
- **Template for:** All future contractor websites (clone from KMJK repo)

## KMJK Website Intel
- **Live:** https://kmjk.pro (also kmjkhomeimprovement.com)
- **GitHub:** QuantumCotton/KMJK (PRIVATE - master template for all contractor sites)
- **Josue (calls):** 772-323-3776 | **Chris (texts):** 772-777-0622
- **Email:** info@kmjk.pro
- **Address:** 1301 SE Francis Street, Jensen Beach, FL 34957
- **Services:** Kitchen, bath, epoxy, handyman, roofing, gutters, TV mount, lights, energy rebates

## Competitors
- Floor Kings, Treasure Coast Epoxy Floors, Strive Epoxy, FloorTek Coatings

## Key Dates
- 2026-02-12: Z.AI MCP search integrated, pressure test started, 99+ leads
- 2026-02-13: Lead database initialized (16,406 leads), dashboard live on port 8181, 28 tools built, full automation pipeline operational
