# HEARTBEAT.md - Automated Task Schedule

## Contact Info
- **Call Josue:** 772-323-3776
- **Text Chris:** 772-777-0622
- **Email:** info@kmjk.pro | **Website:** https://kmjk.pro

## HOW TO SEARCH THE WEB
```bash
# PRIMARY: Brave Search API (Pro tier — 20K queries/month)
exec python3 ~/.openclaw/bin/brave_search.py "your search query"

# SECONDARY: Z.AI webSearchPrime — DEAD until March 1, 2026 (Error 1310)
# Do NOT use zai_search.py — it will fail with "Weekly/Monthly Limit Exhausted"
```

## Schedule (Eastern Time)

### Active Cron Jobs (UTC — subtract 5 for ET)
| Cron | Task | Script |
|------|------|--------|
| Every 4h | National lead scraping (Brave) | national_scraper.py |
| Every 2h :30 | Email enrichment (SMTP/MX) | apollo_guesser.py |
| Every 30min | Dashboard rebuild | market_dashboard.py |
| Every 2h :45 | GitHub auto-push | git push to daily-reports |
| Daily 3 AM | Bulk email verification | bulk_verifier.py |
| Daily 3 AM | Lead sample verification | lead_verifier.py |
| Daily 5 AM | Multi-agent repo improvement | overnight_repo_agent.py |
| Every 5min | Gateway health check | gateway_healthcheck.sh |
| Daily 6 AM | System health report | system_health.py |
| Daily 2 AM | Database backup | cp lead_bank.db backup |

### Agent Delegation Schedule
| Time (ET) | Task | Agent |
|-----------|------|-------|
| Overnight | Heavy scraping batches | lead-scout via national_scraper |
| Morning | Enrich new leads | lead-generator via apollo_guesser |
| 9 AM | Morning summary → Telegram | strategy-planner |
| Noon | Light scrape batch | lead-scout |
| 3 PM | Draft outreach for new leads | outreach-writer |
| 6 PM | Evening scrape batch | lead-scout |
| 10 PM | Verify random sample | lead-scout via lead_verifier |
| Midnight | Repo improvement swarm | github-reviewer + coding-specialist |

## Service Categories (17)
1. Property management 2. Apartments 3. HOA 4. Auto/dealership
5. Restaurant/kitchen 6. Cleaning 7. Real estate investors 8. Warehouse
9. Mobile detailing 10. Epoxy 11. Kitchen reno 12. Bathroom reno
13. Roofing 14. Gutter/exterior 15. Handyman 16. General contracting
17. Referral sources (Craigslist, forums)

## Priority Cities
| Priority | Cities |
|----------|--------|
| High | Stuart, Palm City, Jensen Beach, Sailfish Point, Sewall's Point |
| Medium | Port St Lucie, Fort Pierce, Hobe Sound, Hutchinson Island |
| Low | Vero Beach, Jupiter, Okeechobee |

## ESH National Expansion
Target high-income US markets: Naples, Boca Raton, Sarasota, Jupiter, West Palm, Scottsdale, Austin, Nashville, Charlotte.
Each market: 3-4 contractors (kitchen/bath, epoxy, detailing, GC).

## Error Handling
- Brave returns 429 → check rate_limiter, skip batch gracefully
- Search empty 3x → try different query phrasing
- CSV write fails → log + Telegram alert
- Never crash entire scrape for one failed search
- Z.AI search → DO NOT USE until March 1, 2026

## File Locations
| File | Path |
|------|------|
| Lead Database | ~/.openclaw/workspace/leads/lead_bank.db |
| Lead CSV | ~/.openclaw/workspace/leads/master_leads.csv |
| Brave search | ~/.openclaw/bin/brave_search.py |
| National scraper | ~/.openclaw/bin/national_scraper.py |
| Rate limiter | ~/.openclaw/bin/rate_limiter.py |
| System health | ~/.openclaw/bin/system_health.py |
| Lead verifier | ~/.openclaw/bin/lead_verifier.py |
| GitHub push | ~/.openclaw/bin/github_push.py |


## Agentic Slow-Roll Workflows (State-Managed)

These workflows use cursor.json state files for resume-where-left-off.
Each cycle processes ONE metro, then sleeps. No overlapping. No rushing.

### Job Board Hunter (Indeed + Monster)
- **Schedule:** Every 20 minutes via Heartbeat
- **Script:** `python3 ~/.openclaw/bin/job_board_scraper.py --cycle`
- **State file:** `~/.openclaw/bin/state/job_board_cursor.json`
- **What it finds:** Companies hiring property managers, maintenance supervisors,
  facility managers, HOA managers → these are WARM LEADS who need contractors
- **Cycle time:** ~3 min per metro (Indeed + Monster × 3 queries)
- **Full US rotation:** ~48 metros × 20 min = ~16 hours
- **Check status:** `python3 ~/.openclaw/bin/job_board_scraper.py --status`

### Craigslist Hunter (3 categories)
- **Schedule:** Every 20 minutes via Heartbeat (alternates with Job Board)
- **Script:** `python3 ~/.openclaw/bin/craigslist_scraper.py --cycle`
- **State file:** `~/.openclaw/bin/state/craigslist_cursor.json`
- **Three search types per metro:**
  1. Contractors offering services (potential ESH partners)
  2. People ASKING for services (direct client leads)
  3. Property management gigs (warm prospects)
- **Full CL rotation:** ~44 cities × 20 min = ~15 hours
- **Check status:** `python3 ~/.openclaw/bin/craigslist_scraper.py --status`

### Directory Hunter (Yelp + BBB + Yellow Pages)
- **Schedule:** Every 8 hours via cron (heavier, 3 sources per metro)
- **Script:** `python3 ~/.openclaw/bin/directory_scraper.py --max-metros 3`
- **No state file needed (random metro each time)**

### How to Monitor All Scrapers
```bash
python3 ~/.openclaw/bin/job_board_scraper.py --status
python3 ~/.openclaw/bin/craigslist_scraper.py --status
python3 ~/.openclaw/bin/rate_limiter.py
```

### Slow-Roll Timing
```
:00  Job Board cycle (metro N)
:20  Craigslist cycle (metro M)
:40  Rest / other tasks
:00  Job Board cycle (metro N+1)
...repeat
```
This gives us ~72 metro-scrapes per day across both scrapers, $0 cost.

---

## Daily Operations & Dashboard

### Dashboard Monitoring
- **URL:** http://107.172.20.181:8181/ (Chris/Cotton247)
- **Rebuilds:** Every 30 minutes via cron
- **Status:** Auto-updates from lead database, metrics, and agent activity

### Daily Task Generation
- **Task List:** Auto-generates at 6 AM UTC each day in `TASKS-YYYY-MM-DD.md`
- **Purpose:** Checklist of all systems, projects, and agent work to track for the day
- **Creates:** Daily operations checklist, project status updates, financial tracking

### Agent Swarm Monitoring
- **Total Agents Configured:** 11 active agents
- **Concurrent Limit:** 20 agents can run simultaneously
- **Status Checking:** Use `sessions_list` to see active sessions, `sessions_history` for agent logs
- **Performance:** Agents complete tasks independently, report back via session or direct file writes

### Financial Tracking
- **Revenue Sources:** Lead gen commissions, ESH Mail subscriptions
- **Cost Tracking:** APIs, domains, hosting, SMTP providers
- **Profit Margin:** Track by project and customer tier

### Daily Checklist (Auto-generated)
1. Review daily task list at 6 AM UTC
2. Check agent swarm status and performance
3. Monitor dashboard health and connectivity
4. Track lead gen metrics (new leads, verification rates)
5. Review ESH Mail research progress
6. Update financials if any revenue/expenses
7. Check system health (Gateway, VPS, Docker)
8. Address any blockers or permission issues immediately
9. Generate daily summary report for Telegram at 9 AM UTC
10. Update MEMORY.md with significant events/decisions

---

## System Health Monitoring

### Gateway Status
- **Check:** `openclaw gateway status`
- **Health:** `openclaw gateway health-check`
- **Restart:** `openclaw gateway restart`

### VPS Status
- **Uptime:** Monitor server availability
- **Resources:** CPU, memory, disk usage
- **Docker:** Container status, socket permissions

### Agent Performance
- **Success Rate:** Tasks completed vs failed
- **Time Spent:** By agent and task type
- **Blocking Issues:** Permission errors, API limits, missing tools
