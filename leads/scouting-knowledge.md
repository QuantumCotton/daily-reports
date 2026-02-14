# Lead Scout 247 — Knowledge Base

> Started: 2026-02-14
> Purpose: Record everything learned about scraping patterns, query effectiveness, metro performance, and optimization strategies.

## Initial Knowledge (Day 0)

### What We Know So Far

**Target Zone:** Treasure Coast, FL + 20-mile radius from Stuart
- **High Priority:** Stuart, Palm City, Jensen Beach, Sailfish Point, Sewall's Point
- **Medium:** Port St Lucie, Fort Pierce, Hobe Sound, Hutchinson Island
- **Extended:** Vero Beach, Jupiter, Palm Beach Gardens, Okeechobee

**Scrapers Available:**
1. Job Board Hunter (Indeed + Monster)
2. Craigslist Hunter (3 categories: contractors, client requests, PM gigs)
3. Directory Hunter (Yelp + BBB + Yellow Pages)
4. National Scraper (bulk queue processing)

**Free Search Stack:**
- Tier 1: SearXNG (self-hosted, port 8888)
- Tier 2: DuckDuckGo via home PC proxy (residential IP, port 1080)
- Tier 3: Brave API (paid fallback, rate-limited)

### Unknowns to Learn

These patterns are NOT known yet — will discover during 24/7 operation:

- [ ] Best query patterns per metro/industry
- [ ] Highest-yield metros (which cities produce most leads)
- [ ] Lowest-yield metros (avoid or deprioritize)
- [ ] Rate limit patterns by source (when do Indeed/CL/Yelp throttle?)
- [ ] Best times of day for each scraper
- [ ] Which source produces highest quality leads
- [ ] Job titles that convert to warm leads

### Current Assumptions

**Hypotheses to test:**
1. Job boards in mornings (9am-12pm) produce more hiring listings
2. Craigslist evenings/weekends better for contractors and requests
3. Directories consistent throughout day
4. Smaller metros (Stuart, Jensen Beach) better yield per query than metros
5. "Property manager" queries produce better leads than "PM" (more specific)

## Learning Log

**Cycle Log:**
| Date/Time | Scraper | Metro/Query | Leads Found | Quality | Insights |
|------------|---------|-------------|------------|---------|----------|
| 2026-02-14 TBD | TBD | TBD | TBD | TBD | TBD |

## Query Patterns Tested

| Pattern | Category | Result Count | Quality | Verdict |
|--------|----------|--------------|---------|---------|
| "property manager [city] FL" | Job Board | TBD | TBD | TBD |
| "property management [city]" | CL (gigs) | TBD | TBD |
| "PM [city]" | Job Board | TBD | TBD | TBD |

## Metro Performance

| Metro | Total Leads | Leads/Scrape | Best Source | Verdict |
|-------|-------------|--------------|-------------|---------|
| Stuart, FL | 0 | TBD | TBD | TBD |
| Jensen Beach, FL | 0 | TBD | TBD | TBD |

## Optimization Strategies

**Rules to Apply:**
1. If query pattern produces 5+ leads per scrape → Double down on it
2. If query pattern produces 0-2 leads → Drop it, try alternative
3. If source consistently fails 3x → Switch to alternative source
4. If rate limit hits → Wait 2x normal interval, then retry

**Rate Limit Handling:**
- Job Board (Indeed): 429 → Wait 30 min, then retry
- Craigslist: 403/blocked → Rotate user-agent, change IP, skip this metro
- Yelp/Yahoo: 429 → Switch to BBB or come back later

---

**Last updated: 2026-02-14 10:40 UTC — Initial knowledge base created_
