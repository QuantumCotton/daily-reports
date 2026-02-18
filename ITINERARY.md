# ITINERARY - Weekly Plan & Agent Deployment
# Created: 2026-02-18 00:45 UTC
# Purpose: Track execution, manage priorities, coordinate agents

---

## 📅 WEEK 1: JOSUE STABILIZATION & EMAIL WARMING (Feb 18-24)

### Objective
Stabilize Josue/KMJK at $50K/month (conservative), warm up emails, prepare for national expansion.

### Daily Priorities (Feb 18-24)

#### Monday, Feb 18
- [ ] Review all current cron jobs (document what's running, what's needed)
- [ ] Begin email warming immediately (start gradual warm-up)
- [ ] Gather 16 more TC person emails (hit 500 goal - currently at 484)
- [ ] Update SOUL.md with business model, email warming strategy
- [ ] Upload all documents to GitHub (permanent reference)

#### Tuesday, Feb 19
- [ ] Email warming: Continue gradual warm-up (increase to 20 emails/day)
- [ ] TC enrichment: Continue tc_enricher.py (find personal emails)
- [ ] War room: Deploy business_advisory.py (8 personas ready)
- [ ] Prepare first 5-market launch guides (San Jose, Dallas, SF, Seattle, Houston)

#### Wednesday, Feb 20
- [ ] Email warming: Monitor deliverability, adjust pacing (25 emails/day if reputation good)
- [ ] TC enrichment: Continue gathering leads
- [ ] Email infrastructure: Set up unified inbox (Instantly API purchase)
- [ ] War room: Build dashboard (real-time metrics)

#### Thursday, Feb 21
- [ ] Email warming: Continue warm-up (30 emails/day if reputation excellent)
- [ ] TC enrichment: Continue gathering leads
- [ ] Outreach: Prepare 484 TC person emails for Josue's campaign
- [ ] Refine email templates per business type (property managers, HOAs, etc.)

#### Friday, Feb 22
- [ ] Email warming: Final warm-up phase (40 emails/day max)
- [ ] TC enrichment: Final lead gathering (hit 500 goal)
- [ ] Launch readiness: Verify all systems operational (email infrastructure, war room, dashboards)
- [ ] Decision: Is Josue stable? If yes, prepare Phase 2 launch

#### Saturday, Feb 23
- [ ] Review: Email reputation status (deliverability >90%, bounce rate <5%, spam complaints <1%)
- [ ] Decision: Launch Feb 7th campaign if warmed up, or continue warming
- [ ] Review: TC person emails count (500 goal, if exceeded that's better)
- [ ] Update: ITINERARY.md, MEMORY.md, all documentation

#### Sunday, Feb 24
- [ ] **LAUNCH DATE:** Feb 7th campaign (if warmed up) - 5 email addresses, 10 emails/day = 50 emails/day to Treasure Coast
- [ ] Launch: Send first batch of TC emails to Josue (484 prepared)
- [ ] Monitor: Track open rates, response times, conversions
- [ ] Decision: If Josue stable at $50K, begin Phase 2 launch (5 markets)

---

## 📅 WEEK 2-4: PHASE 2 PREPARATION (Feb 25 - Mar 17)

### Objective
Prepare Phase 2 launch (5 markets: San Jose, Dallas, SF, Seattle, Houston). Emails already warmed, ready to blast.

### Week 2 (Feb 25 - Mar 3)
- [ ] Email warming: Continue warm-up (target 5 markets warmed by end of Week 4)
- [ ] Market research: Prepare 5 market launch guides (per-market specialization)
- [ ] Lead targets: Set scraping quotas (2,000 leads per market = 10,000 total)
- [ ] Contractor search: Find elite contractors in 5 markets (1-2 per market)

### Week 3 (Mar 4 - Mar 10)
- [ ] Email warming: Finalize 5-market warm-up
- [ ] Scraping: Begin lead gathering for 5 markets (continuous 24/7)
- [ ] Enrichment: Agent enrichment (find owner names, personal emails)
- [ ] Outreach templates: Prepare per-business-type emails (property managers, HOAs, etc.)

### Week 4 (Mar 11 - Mar 17)
- [ ] Decision: Is Josue stable at $50K?
  - **If yes:** Launch Phase 2 (5 markets, 5-10 contractors)
  - **If no:** Continue TC outreach, delay Phase 2
- [ ] Email warming: 5 markets warmed and ready
- [ ] Launch readiness: Verify all systems operational (email infrastructure, war room, dashboards)

---

## 📅 WEEK 5+: NATIONAL EXPANSION (Mar 18+)

### Objective
Launch new markets weekly (1 market/week if possible), stabilize each contractor, repeat.

### Week 5 (Mar 18 - Mar 24) - Market 6 Launch
- [ ] Launch: Market 6 (Denver)
- [ ] Contractor: Find elite contractor or build from experienced
- [ ] Emails: Already warmed, blast immediately
- [ ] Leads: 2,000 leads prepared
- [ ] Outreach: Send 200-400 emails
- [ ] Monitor: Track contractor stability (target $50K/month)

### Week 6 (Mar 25 - Mar 31) - Market 7 Launch
- [ ] Launch: Market 7 (Washington DC)
- [ ] Repeat Week 5 process

### Week 7 (Apr 1 - Apr 7) - Market 8 Launch
- [ ] Launch: Market 8 (Austin)
- [ ] Repeat Week 5 process

### Continue: 1 Market Per Week
- **Week 8:** Market 9 (New York)
- **Week 9:** Market 10 (Los Angeles)
- **Week 10:** Market 11 (Chicago)
- **Week 11:** Market 12 (Philadelphia)
- **Week 12:** Market 13 (Boston)
- **Week 13:** Market 14 (San Diego)
- **Week 15:** Market 15 (Miami)

**Timeline Reality Check:**
- **1 market/week:** 40 markets in 40 weeks (10 months)
- **1 market/2 weeks:** 40 markets in 80 weeks (20 months)
- **1 market/month:** 40 markets in 40 months (3.3 years)
- **We can code everything in minutes** - timeline depends on contractor stability, email warming, lead quality

---

## 🤖 AGENT DEPLOYMENT (CURRENT & PLANNED)

### Current Active Agents (24/7 Running)
**From Cron Jobs:**

| Agent | Frequency | Purpose | Status |
|--------|-----------|---------|--------|
| **job_board_scraper.py** | Every 20 min | Job board lead scraping | 🟢 Active |
| **craigslist_scraper.py** | Every 20 min (offset 10 min) | Craigslist scraping | 🟢 Active |
| **directory_scraper.py** | 3x/day | Directory scraping | 🟢 Active |
| **national_scraper.py** | Every 4 hours | National lead gathering | 🟢 Active |
| **bulk_verifier.py** | Daily 3 AM | Bulk email verification | 🟢 Active |
| **lead_verifier.py** | Daily 3:30 AM | Lead verification | 🟢 Active |
| **lead_enricher_v4.py** | Every 2 hours (300 leads) | Lead enrichment | 🟢 Active |
| **market_dashboard.py** | Every 30 min | Dashboard rebuild | 🟢 Active |
| **overnight_repo_agent.py** | Daily 5 AM | Repo improvement | 🟢 Active |
| **system_health.py** | Daily 11 AM | System health check | 🟢 Active |
| **daily_task_generator.py** | Daily 6 AM | Daily task list | 🟢 Active |
| **check_agents.sh** | Every 30 min | Agent status check | 🟢 Active |
| **status_report.py** | Every 4 hours | Status report | 🟢 Active |
| **gateway_healthcheck.sh** | Every 5 min | Gateway health check | 🟢 Active |
| **treasure_coast_scraper.py** | Daily 11 PM | TC scraping (max 5) | 🟢 Active |
| **google_maps_scraper.py** | Daily 7 AM | Google Maps scraping | 🟢 Active |
| **apartment_scraper.py** | Daily 7:37 AM | Apartment scraper | 🟢 Active |
| **florida_hoa_scraper.py** | Daily 5:17 PM | Florida HOA scraper | 🟢 Active |
| **property_manager_scraper.py** | Daily 7:47 PM | Property manager scraper | 🟢 Active |
| **advisor_reviewer.py** | Every 15 min | Advisory council review | 🟢 Active |
| **project_dashboard.py** | Every 15 min | Project dashboard | 🟢 Active |
| **auto_monitor.py** | Every 10 min | Auto monitoring | 🟢 Active |
| **morning_report.py** | Daily 9 AM | Morning report | 🟢 Active |
| **tc_enricher.py** | 12 min, 48 min past hour | TC enrichment (find names) | 🟢 Active |
| **tc_verifier.py** | 18 min, 48 min past hour | TC verification | 🟢 Active |
| **tc_enricher_247.py** | Every 12 min | TC enrichment 24/7 (find personal emails) | 🟢 Active |
| **tc_enricher_personal_247.py** | Every 15 min | TC enrichment 24/7 (personal emails) | 🟢 Active |

**Total Active Agents:** 27 (24/7 running)

### Planned Agent Deployments (War Room + Email Warming)

| Agent | Purpose | When Needed | Status |
|--------|---------|-------------|--------|
| **email_warming_agent.py** | Gradual email warm-up, monitor reputation | IMMEDIATE (NOW) | 🔜 To build |
| **email_reputation_monitor.py** | Track deliverability, open rates, bounce rates | IMMEDIATE (NOW) | 🔜 To build |
| **unified_inbox_manager.py** | Manage email queue, throttling, domain rotation | Week 2 (Feb 25) | 🔜 To build |
| **war_room_dashboard.py** | Real-time metrics across all markets | Week 2 (Feb 25) | 🔜 To build |
| **contractor_recruiter.py** | Find elite contractors in target markets | Week 3 (Mar 4) | 🔜 To build |
| **market_launch_coordinator.py** | Coordinate 1 market/week launches | Week 4 (Mar 11) | 🔜 To build |

---

## 📊 WEEKLY METRICS TRACKING

### Week 1 (Feb 18-24) - Josue Stabilization
| Metric | Target | Actual | Status |
|--------|---------|--------|--------|
| TC Person Emails | 500 | 484 (96.8%) | 🔜 Need 16 more |
| Email Warming | Start NOW | ✅ Immediate | 🟢 Started |
| Feb 7th Campaign | Launch ready | TBD | 🔜 Pending warm-up |
| Josue Revenue Target | $50K/month | TBD | 🔜 To track |

### Week 2 (Feb 25 - Mar 3) - Phase 2 Preparation
| Metric | Target | Actual | Status |
|--------|---------|--------|--------|
| Email Warming (5 markets) | 5 markets warmed | TBD | 🔜 Pending |
| Market Launch Guides | 5 guides | TBD | 🔜 Pending |
| Lead Targets Set | 10,000 total (2K/market) | TBD | 🔜 Pending |
| Contractors Found | 5-10 (1-2/market) | TBD | 🔜 Pending |

### Week 3 (Mar 4 - Mar 10) - Phase 2 Execution Prep
| Metric | Target | Actual | Status |
|--------|---------|--------|--------|
| Email Warming Complete | 5 markets warmed | TBD | 🔜 Pending |
| Scraping Started | 10,000 leads flowing | TBD | 🔜 Pending |
| Enrichment Started | Agent enrichment active | TBD | 🔜 Pending |
| Outreach Templates | Per-business-type ready | TBD | 🔜 Pending |

### Week 4 (Mar 11 - Mar 17) - Phase 2 Launch Decision
| Metric | Target | Actual | Status |
|--------|---------|--------|--------|
| Josue Stable | $50K/month | TBD | 🔜 Pending decision |
| Phase 2 Launch | 5 markets, 5-10 contractors | TBD | 🔜 Pending |

---

## 🚨 DECISION POINTS

### Week 1 (Feb 18-24)
- [ ] Decision: Is email reputation >90% deliverability by Feb 7th?
  - **Yes:** Launch Feb 7th campaign (5 email addresses, 50 emails/day)
  - **No:** Continue warming, delay campaign

### Week 4 (Mar 11-17)
- [ ] Decision: Is Josue stable at $50K/month?
  - **Yes:** Launch Phase 2 (5 markets, 5-10 contractors)
  - **No:** Continue TC outreach, delay Phase 2

### Ongoing Weekly
- [ ] Decision: Should we launch next market?
  - **Criteria:** Previous contractor stable at $50K, emails warmed, leads ready
  - **Yes:** Launch 1 market/week
  - **No:** Continue stabilizing, delay launch

---

## 📚 DOCUMENTATION REFERENCES

### Core Documents
- **NATIONAL_EXPANSION_MASTER_PLAN.md** - 1-year strategy (40 markets, 15 contractors)
- **ELITE_SERVICE_HUB_BUSINESS_MODEL.md** - Business model, costs, commission, scaling
- **MONTHLY_COSTS_TRACKER.md** - Cost tracking, profit calculator, scaling triggers
- **cost_profit_tracker.csv** - Spreadsheet for tracking costs, profits
- **SOUL.md** - Personality, philosophy, business model
- **STARTUP.md** - Session startup guide
- **MEMORY.md** - Master memory file

### Operational Documents
- **ITINERARY.md** - This file (weekly plan, agent deployment)
- **TASKS-48-HOURS.md** - Immediate 48-hour priorities
- **EXPANSION_PLAN.md** - Top 5 metro rankings (San Jose #1, Dallas #2, SF #3, Seattle #4, Houston #5)

### Daily Updates
- **memory/YYYY-MM-DD.md** - Daily session logs
- Updated with all strategic decisions, metrics, blockers, wins

---

*Created: 2026-02-18 00:45 UTC*
*Updated: Feb 18, 2026*
