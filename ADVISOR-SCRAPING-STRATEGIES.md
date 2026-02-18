# ADVISOR-SCRAPING-STRATEGIES.md
> Advisor-recommended data sources for Treasure Coast lead generation
> Created: 2026-02-16 03:19 UTC
> Status: READY FOR IMPLEMENTATION

---

## THIEL'S STRATEGIES

### Data Sources:
- **Tier 1 (Free government data):**
  - County property databases (Martin, St. Lucie, Indian River)
  - Florida DBPR (licensing)
  - Restaurant/auto shop licenses
- **Tier 2 (Public listings):**
  - Google Maps
  - Yelp
  - LinkedIn
  - Apartment.com
- **Tier 3 (Website scraping):**
  - Contact pages
  - Staff directories
  - Email patterns

### Timing Strategies:
- Target junior property managers (they control multiple properties + move between companies)
- Restaurant off-season marketing (May-Aug) when they renovate
- HOA election cycle timing (sync with budget approval meetings)

### Contrarian Plays:
- Property Manager Pipeline: Capture their entire career portfolio
- Restaurant Turnover Season: Own off-season, not snowbird season
- HOA Board Cycle: Target new board members who want quick wins

---

## JENSEN'S STRATEGIES

### Data Sources by Category:

**Property Managers:**
- Chamber of Commerce directories
- Yelp
- BBB (Better Business Bureau)
- Zillow professionals

**HOAs:**
- Florida-HOA.com
- Local community association websites
- County records

**Apartment Complexes:**
- Apartments.com
- Zillow
- Trulia
- Property management sites

**Restaurants:**
- TripAdvisor
- Yelp
- OpenTable
- Chamber restaurant directories

**Auto Shops:**
- Yelp
- PreferredMechanic
- Local business directories

### Technical Stack:
- SearXNG (free, self-hosted) - primary
- Home proxy (residential IP) - bypass blocks
- Brave API (paid fallback) - 2K/month

### Queries:
- "property managers Stuart FL Martin County"
- "HOAs Martin County FL"
- "apartment complexes Stuart FL"
- "restaurants Stuart FL"
- "auto repair shops Stuart FL"

---

## MUSK'S STRATEGIES

### 4-Tier Pipeline:

**Tier 1 (Paid):**
- Apollo.io → 500-800 verified/month
- ZoomInfo

**Tier 2 (Free scraping):**
- Google Maps API
- Florida SunBiz (business registrations)
- County Property Appraisers

**Tier 3 (Social):**
- LinkedIn Sales Navigator
- Facebook groups

**Tier 4 (Enrichment):**
- NeverBounce validation
- Hunter.io email finding

### Key Insight:
- Target DECISION-MAKERS, not businesses
- Property managers, HOA presidents, facility managers
- That's who says yes

---

## CARMACK'S STRATEGIES

### Data Sources (FREE → Paid):
- **SearXNG search** (free, self-hosted): 28 queries/day
- **Google Maps scraping**: "property management Stuart FL" etc.
- **Public records**: FL HOA database, county clerk sites
- **Business directories**: NARPM, IREM, Yelp, Chamber of Commerce
- **Property listing sites**: Apartments.com, Zillow rentals

### Cities:
- Stuart FL
- Port St. Lucie FL
- Fort Pierce FL
- Vero Beach FL
- Jensen Beach FL
- Sebastian FL
- Hobe Sound FL

### Categories:
- Property Management: "property management company" + city
- HOAs: "HOA management companies" + city
- Restaurants: "restaurant owner" + city
- Auto Shops: "auto repair shop" + city
- Apartments: "apartment complex" + city

### Script Created:
- `treasure_coast_scraper.py` (28 queries × 7 cities)

### Enrichment Pipeline:
- `lead_enricher_v4.py`: Scrapes websites for personal emails ($0)
- `apollo_guesser.py`: SMTP verifies email patterns ($0)
- `bulk_verifier.py`: MillionVerifier API ($0.005/email for final validation)

---

## UNIFIED STRATEGY (COMBINED)

### Priority Data Sources (FREE):
1. **SearXNG** - 28 queries/day (all categories × 7 cities)
2. **Google Maps** - Business name + contact info
3. **Florida-HOA.com** - HOA directory
4. **County clerk sites** - Property records, licenses
5. **NARPM/IREM** - Property manager directories
6. **Yelp/TripAdvisor** - Restaurants + reviews
7. **Apartments.com/Zillow** - Rental properties
8. **Florida SunBiz** - Business registrations
9. **Chamber of Commerce** - Local business directories

### Priority Data Sources (PAID - OPTIONAL):
1. **Apollo.io** - 500-800 verified/month ($79/mo)
2. **NeverBounce** - Email validation ($20/mo)
3. **Instantly.ai** - Email sending ($37/mo)

### Target Cities (Treasure Coast):
1. Stuart, FL
2. Jensen Beach, FL
3. Port St. Lucie, FL
4. Fort Pierce, FL
5. Vero Beach, FL
6. Sebastian, FL
7. Hobe Sound, FL

### Target Categories:
1. Property Management Companies
2. HOAs (Homeowner Associations)
3. Apartment Complexes
4. Restaurants
5. Auto Repair Shops

### Special Targets (Contrarian):
- **Junior property managers** (career pipeline)
- **New HOA board members** (quick wins)
- **Off-season restaurants** (May-Aug renovations)

---

## IMPLEMENTATION STATUS

| Strategy | Source | Status | Priority |
|----------|--------|--------|----------|
| SearXNG 28 queries/day | Carmack | ✅ READY | HIGH |
| Google Maps scraping | Thiel/Jensen/Musk/Carmack | 🔜 TODO | HIGH |
| Florida-HOA.com | Jensen | 🔜 TODO | HIGH |
| County clerk sites | Thiel/Carmack | 🔜 TODO | MEDIUM |
| NARPM/IREM directories | Carmack | 🔜 TODO | MEDIUM |
| Florida SunBiz | Musk | 🔜 TODO | MEDIUM |
| Chamber of Commerce | Jensen/Carmack | 🔜 TODO | MEDIUM |
| Apollo.io (paid) | Musk | ⏸️ OPTIONAL | LOW |
| LinkedIn Sales Nav (paid) | Musk | ⏸️ OPTIONAL | LOW |
| Junior PM targeting | Thiel | 🔜 TODO | HIGH |
| HOA election timing | Thiel | 🔜 TODO | MEDIUM |
| Restaurant off-season | Thiel | 🔜 TODO | MEDIUM |

---

## NEXT STEPS

1. **Create `treasure_coast_scraper.py`** with 28 queries (Carmack's approach)
2. **Add Google Maps scraping** to existing scrapers
3. **Scrape Florida-HOA.com** for HOA directory
4. **Add NARPM/IREM** to directory scraper
5. **Update HEARTBEAT.md** with new targets
6. **Update PROCESS.md** with scraping methodology
7. **Update MEMORY.md** with strategy decisions

---

_Last updated: 2026-02-16 03:19 UTC_
