# PROCESS.md - Elite Service Hub Playbook
> **Purpose:** Document everything that works and doesn't work. Create repeatable playbooks for scaling.

> **Created:** 2026-02-15
> **Last Updated:** 2026-02-16 05:03 UTC

---

## 📧 EMAIL INFRASTRUCTURE (TONIGHT'S GOAL - UPDATED)

### Email Structure (80 Emails Across 16 Metros)

**Base domain:** kmjk.pro

**5 Emails Per City:**
1. chris@kmjk.pro (The Owner)
2. projects-[CODE]@kmjk.pro (The "Project Manager")
3. estimates-[CODE]@kmjk.pro (The "Estimator")
4. site-[CODE]@kmjk.pro (The "Site Supervisor")
5. office-[CODE]@kmjk.pro (The Admin)

**Metro Codes (FINAL LIST - 16 Metros):**
| Metro | Code | Source |
|-------|------|--------|
| Treasure Coast | -tc | Chris's preference |
| San Jose (Bay Area) | -ba | Chris's preference |
| Dallas-Fort Worth | -dfw | TOP-15-METROS.md |
| Washington DC | -dc | TOP-15-METROS.md |
| Houston | -hou | TOP-15-METROS.md |
| Seattle | -sea | TOP-15-METROS.md |
| Austin | -aus | TOP-15-METROS.md |
| Denver | -den | TOP-15-METROS.md |
| Raleigh | -rdu | TOP-15-METROS.md |
| Phoenix | -phx | TOP-15-METROS.md |
| Atlanta | -atl | TOP-15-METROS.md |
| Charlotte | -clt | TOP-15-METROS.md |
| Nashville | -bna | TOP-15-METROS.md |
| Orlando | -mco | TOP-15-METROS.md |
| Tampa | -tpa | TOP-15-METROS.md |
| Asheville, NC | -avl | Chris's fantasy area |
| Miami, FL | -mia | Chris's preference |
| Florida Keys | -fky | Chris's fantasy area |
| Hawaii islands | -hw1, -hw2 | Chris's fantasy area |
| Minneapolis-St Paul | -msp | Northern metro for seasonal services |

**Total:** 80 emails (16 metros × 5 emails each)

**Example:**
- Treasure Coast: chris@, projects-tc@, estimates-tc@, site-tc@, office-tc@
- Bay Area: chris@, projects-ba@, estimates-ba@, site-ba@, office-ba@

### Email Setup Options:
- **Option A:** 80 real inboxes (separate storage, can send/receive from each)
- **Option B:** 80 aliases → all forward to chris@kmjk.pro (simpler for warming)

**Chris's preference:** Option B (aliases) for warming, switch to A for actual operations if needed

### Why Cities? → TO FIND NAMES
Each metro area has different property managers → different owners → different names → better personalization

### Warm-up Strategy
- Start warming emails by Feb 18 (2 days from now)
- 14-day warm-up period minimum
- Launch March 7

---

## 🎯 The 90-Day Plan

| Phase | Time | Action | Status |
|-------|------|--------|--------|
| **Phase 1** | Week 1 (Feb 15-21) | Gather leads nationwide + Treasure Coast enrichment | 🟢 IN PROGRESS |
| **Phase 1 Launch** | 20 days (March 7) | First email outreach for Josue | 🔜 UPCOMING |
| **Phase 2** | Weeks 4-12 (Mar 7-Apr 30) | Add 1 city/week (or every 2 weeks) | 🔜 UPCOMING |
| **Phase 3** | 90 days (May 15) | 4 contractors total (Josue + 3 Treasure Coast + 3 elsewhere) | 🔜 UPCOMING |

---

## 📊 Current System Status (2026-02-15 18:50 UTC)

### Scrapers (ALL RUNNING)
| Scraper | Frequency | Last Run | Status |
|---------|-----------|----------|--------|
| Job Board | Every 20 min | 8 min ago | 🟢 RUNNING |
| Craigslist | Every 20 min | Just now | 🟢 RUNNING |
| National | Every 4 hours | 2h 50m ago | 🟢 RUNNING |
| Directory | Daily | Scheduled | 🟢 RUNNING |
| Lead Enricher v4 | Every 2 hours | Scheduled | 🟢 RUNNING |

### Database
- **Total leads:** 20,273
- **Cities:** 81
- **States:** 14
- **With email:** 2,871

---

## 🎯 This Week's Focus (Feb 15-21)

### 1. Treasure Coast Email Enrichment
**Goal:** Convert generic emails to personal emails + owner names

**Target Cities:**
1. Stuart, FL
2. Jensen Beach, FL
3. Port St. Lucie, FL
4. Vero Beach, FL
5. Sebastian, FL

**What to Enrich:**
- Owner names (from About pages, LinkedIn, Secretary of State)
- Personal emails (first.last@, not info@)
- Cell phones (if available)
- Background info about the person

**Tools:**
- `lead_enricher_v4.py` - Scrape business websites
- `apollo_guesser.py` - Email pattern guessing + SMTP verify
- Manual research (LinkedIn, Facebook, Yelp owner responses)

### 2. Continue National Lead Gathering
**Goal:** Get to 10,000+ companies nationwide

**Strategy:**
- Keep all scrapers running 24/7
- Focus on 15 high-income metros
- Don't worry about email quality YET - get the companies first

**Target Metros (High Income):**
1. San Jose, CA ($155K median)
2. San Francisco, CA
3. Boston, MA
4. New York, NY
5. Washington, DC
6. Seattle, WA
7. Austin, TX
8. Dallas, TX
9. Miami, FL
10. Los Angeles, CA
11. Treasure Coast, FL (Josue's area - DONE)
12. Chicago, IL
13. Philadelphia, PA
14. Denver, CO
15. San Diego, CA

### 3. Document Everything
**Goal:** Create playbook for contractor #4, #5, #6

**What to Document:**
- Email enrichment strategies that work
- Best sources for owner names
- Email patterns that verify
- Outreach templates that convert
- Common blockers and how to fix

---

## 🎯 Next Week's Focus (Feb 22-28)

### Email Template Refinement
**Goal:** Create business-type-specific email templates

**Business Types:**
1. Property management companies
2. Apartment complexes
3. HOAs
4. Auto dealerships
5. Restaurants/kitchens
6. Real estate investors
7. Warehouses
8. Hotels/resorts

**Services:**
- Epoxy flooring
- Kitchen renovation
- Bathroom renovation
- Mobile detailing
- Handyman services
- Roofing
- Gutters

**Template Structure:**
- Personal greeting (owner name)
- Pain point specific to business type
- Relevant service offered
- Social proof (case study, review)
- Call to action

---

## 🎯 Phase 1 Launch (March 7, 2026)

### Target: Josue's First Email Outreach
**Goal:** 500-1,000 high-quality Treasure Coast leads

**Requirements:**
- Owner names
- Personal emails
- Background info
- No generic emails (info@, sales@, contact@)

**Email Volume:**
- Week 1: 50 emails/day
- Week 2: 75 emails/day
- Week 3: 100 emails/day
- Week 4: 150 emails/day

**Metrics to Track:**
- Open rate
- Response rate
- Meeting booked
- Deal closed
- Revenue generated

---

## 🎯 Phase 2: Expansion (March 7 - April 30)

### Strategy: Add 1 City/Week (or Every 2 Weeks)
**Goal:** 15 cities total by end of Phase 2

**Selection Criteria:**
- High median income ($100K+)
- Lead database already populated
- Contractor recruited for that area

**Process for New City:**
1. Identify target metro from database
2. Filter leads for business types that need services
3. Enrich emails (owner names, personal emails)
4. Draft business-specific email templates
5. Launch email outreach
6. Track metrics
7. Document what works/doesn't

---

## 🎯 Phase 3: Full Scale (May 1 - May 15)

### Goal: 4 Contractors Total
**Current:** Josue (Treasure Coast)
**Target:** +3 contractors (3 Treasure Coast, 3 elsewhere)

**Contractor Types:**
1. Flooring (epoxy)
2. Kitchen/bath renovation
3. Mobile detailing
4. Handyman services

**Territory Protection:**
- Each contractor gets exclusive territory
- No competition within same metro
- Commission structure: 15% of contractor revenue

---

## 📊 Metrics to Track

### Lead Generation
- Total leads gathered
- Metros covered
- Email enrichment rate (% with personal emails)
- Owner name enrichment rate (% with names)

### Email Outreach
- Emails sent
- Open rate
- Response rate
- Meeting booked rate
- Deal closed rate

### Revenue
- Contractor revenue
- Commission earned (15%)
- ROI on time/investment

---

## 📋 What Works (So Far)

### Lead Gathering
- **SearXNG** - Free search engine, no API limits
- **Job Board scraper** - Every 20 min, slow-roll
- **Craigslist scraper** - Every 20 min, alternates
- **National scraper** - Every 4 hours, SearXNG → Brave fallback

### Email Enrichment
- **lead_enricher_v4.py** - Scrape business websites directly (~15% success)
- **apollo_guesser.py** - SMTP verify email patterns ($0 cost)
- **Manual research** - LinkedIn, Facebook, Yelp owner responses

### What Doesn't Work
- **Z.AI webSearchPrime** - Exhausted until March 1, 2026
- **Google via web_fetch** - Anti-bot blocking
- **Facebook/Nextdoor** - Login wall

---

## 🚀 Repeatable Playbook for Contractor #4, #5, #6

### Week 1: Database Query
1. Query `lead_bank.db` for target metro
2. Filter by business type (PM companies, restaurants, auto shops)
3. Export to CSV

### Week 2: Email Enrichment
1. Run `lead_enricher_v4.py` on all leads (scrape websites)
2. Run `apollo_guesser.py` for email patterns + SMTP verify
3. Manual research: LinkedIn, Facebook, Yelp owner responses
4. Update database with owner names + personal emails

### Week 3: Template Development
1. Copy existing email templates
2. Customize for business type + metro
3. Test with small batch (50 emails)
4. Refine based on response rate

### Week 4: Launch Outreach
1. Start with 50 emails/day
2. Scale up based on response rate
3. Track all metrics
4. Document what works/doesn't

**Total time:** 4 weeks (or 2 weeks if aggressive)

---

## 🔜 Next Actions

### Immediate (This Week)
- [ ] Treasure Coast enrichment: Get owner names + personal emails for 500+ leads
- [ ] Continue national lead gathering (aim for 10,000+ companies)
- [ ] Document enrichment strategies in PROCESS.md

### Next Week
- [ ] Refine email templates per business type
- [ ] Test templates with small batch (50 emails)
- [ ] Refine based on response rate

### Phase 1 Launch (March 7)
- [ ] Finalize Treasure Coast list (500-1,000 high-quality leads)
- [ ] Launch Josue's first email outreach
- [ ] Track all metrics

---

**Last Updated:** 2026-02-15 18:50 UTC
**Next Review:** 2026-02-16 09:00 UTC (daily)

---

## 📧 UPDATED EMAIL INFRASTRUCTURE (2026-02-16)

### Email Structure (360 Aliases Across 40 Metros + 1 Owner)

**Base domain:** kmjk.pro

**9 Role-Based Aliases Per Metro:**
1. projects-[CODE]@kmjk.pro → Project Manager
2. estimates-[CODE]@kmjk.pro → Estimator
3. site-[CODE]@kmjk.pro → Site Supervisor
4. office-[CODE]@kmjk.pro → Admin
5. sales-[CODE]@kmjk.pro → Sales
6. support-[CODE]@kmjk.pro → Support
7. billing-[CODE]@kmjk.pro → Billing
8. info-[CODE]@kmjk.pro → General Info
9. team-[CODE]@kmjk.pro → Team

**Owner Email:**
1. chris@kmjk.pro → Owner (Chris)

**Total:** 361 unique email addresses (1 owner + 360 aliases)

### Metro Codes (40 Metros - UPDATED)
| Metro | Code | 
|-------|------|
| Tri-State Area (NY-NJ-CT) | tri |
| San Francisco Bay Area | ba |
| Philadelphia Metro | phl |
| Chicago Metro | chi |
| Washington D.C. Metro | dc |
| Los Angeles Metro | la |
| Boston Metro | bos |
| Kansas City Metro | kc |
| Dallas-Fort Worth Metro | dfw |
| Houston Metro | hou |
| Wichita Metro | wic |
| Seattle Metro | sea |
| Detroit Metro | det |
| Atlanta Metro | atl |
| Anchorage Metro | anc |
| Memphis Metro | mem |
| Denver Metro | den |
| Des Moines Metro | dsm |
| Oklahoma City Metro | okc |
| Phoenix Metro | phx |
| Raleigh-Durham Metro | rdu |
| Jackson Metro | jax |
| Manchester-Nashua Metro | mht |
| Indianapolis Metro | ind |
| Nashville Metro | bna |
| Cleveland-Akron Metro | cle |
| Columbus Metro | cmh |
| Lexington Metro | lex |
| Salt Lake City Metro | slc |
| Louisville Metro | lou |
| Fort Wayne Metro | fwa |
| Honolulu Metro | hnl |
| Albuquerque Metro | abq |
| Providence Metro | pvd |
| Las Vegas Metro | las |
| Portland Metro (OR) | pdx |
| Charlotte Metro | clt |
| Milwaukee Metro | mke |
| Portland Metro (ME) | pwm |
| Madison Metro | msn |

**Example (Tri-State Area):**
- Owner: chris@kmjk.pro
- Projects: projects-tri@kmjk.pro
- Estimates: estimates-tri@kmjk.pro
- Site: site-tri@kmjk.pro
- Office: office-tri@kmjk.pro
- Sales: sales-tri@kmjk.pro
- Support: support-tri@kmjk.pro
- Billing: billing-tri@kmjk.pro
- Info: info-tri@kmjk.pro
- Team: team-tri@kmjk.pro

### Email Forwarding Rules

#### Default Configuration (Initial Warm-up Phase)
All aliases forward to **chris@kmjk.pro**:

```
# Default forwarding - all to Chris
projects-[CODE]@kmjk.pro → chris@kmjk.pro
estimates-[CODE]@kmjk.pro → chris@kmjk.pro
site-[CODE]@kmjk.pro → chris@kmjk.pro
office-[CODE]@kmjk.pro → chris@kmjk.pro
sales-[CODE]@kmjk.pro → chris@kmjk.pro
support-[CODE]@kmjk.pro → chris@kmjk.pro
billing-[CODE]@kmjk.pro → chris@kmjk.pro
info-[CODE]@kmjk.pro → chris@kmjk.pro
team-[CODE]@kmjk.pro → chris@kmjk.pro
```

#### Future Configuration (Per-Contractor Assignment)
When contractors are assigned to specific metros, update forwarding:

```
# Example: Contractor assigned to Tri-State area
projects-tri@kmjk.pro → contractor-tri@example.com
estimates-tri@kmjk.pro → contractor-tri@example.com
site-tri@kmjk.pro → contractor-tri@example.com
office-tri@kmjk.pro → admin@example.com
sales-tri@kmjk.pro → sales@example.com
support-tri@kmjk.pro → support@example.com
billing-tri@kmjk.pro → billing@example.com
info-tri@kmjk.pro → info@example.com
team-tri@kmjk.pro → chris@kmjk.pro
```

### Email Setup Commands

#### 1. Generate Email List
```bash
# View complete email list
cat /home/chris/.openclaw/workspace/EMAIL-LIST.txt
```

#### 2. Configure Email Aliases
```bash
# Run setup script (requires sudo)
sudo /home/chris/.openclaw/bin/setup_emails.sh
```

#### 3. Verify Configuration
```bash
# Check Exim aliases file
cat /etc/exim4/domains/kmjk.pro/aliases

# Test email delivery
echo "Test" | mail -s "Test email" projects-tri@kmjk.pro
```

#### 4. Update Forwarding Destinations
To update where specific aliases forward:

1. Edit aliases file:
```bash
sudo nano /etc/exim4/domains/kmjk.pro/aliases
```

2. Modify destination email addresses:
```
# Example: Forward Tri-State project emails to contractor
projects-tri@kmjk.pro: contractor@example.com
```

3. Restart Exim4:
```bash
sudo systemctl restart exim4
```

### Warm-up Strategy

#### Phase 1: Domain Reputation (Weeks 1-2)
- Send low volume from chris@kmjk.pro only
- Build sending reputation
- Monitor spam folders

#### Phase 2: Alias Warm-up (Weeks 3-4)
- Gradually introduce 10-20 aliases per day
- Send 5-10 emails per alias/day
- Monitor delivery rates

#### Phase 3: Full Operation (Week 5+)
- All 361 email addresses active
- Scale to planned outreach volumes
- A/B test different subject lines/senders

### Email Volume Targets

#### Warm-up Phase (Weeks 1-4)
- **Week 1:** 20 emails/day (chris@kmjk.pro only)
- **Week 2:** 40 emails/day (chris@kmjk.pro + 10 aliases)
- **Week 3:** 80 emails/day (20 aliases)
- **Week 4:** 150 emails/day (40 aliases)

#### Operation Phase (Week 5+)
- **Per Metro:** 50-150 emails/day (depending on contractor capacity)
- **Total:** 2,000-6,000 emails/day across 40 metros

### Files Reference

| File | Purpose | Location |
|------|---------|----------|
| EMAIL-LIST.txt | Complete list of all 361 email addresses | /home/chris/.openclaw/workspace/EMAIL-LIST.txt |
| setup_emails.sh | Script to configure email aliases | /home/chris/.openclaw/bin/setup_emails.sh |
| aliases | Exim4 aliases configuration | /etc/exim4/domains/kmjk.pro/aliases |

---

**Last Updated:** 2026-02-16 05:47 UTC
