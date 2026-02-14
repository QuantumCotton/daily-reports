# Organized Lead List — Priority Outreach Targets
**Generated:** 2026-02-14 12:40 UTC
**Purpose:** Prioritized lead list for email outreach campaigns

---

## Database Overview

**Total Leads:** 16,406
**Verified Emails:** 281 (1.7%)
**Top Cities:** Stuart (641), Miami (399), Jacksonville (391), Naples (385)
**Categories:** 30+ categories, from auto dealerships to property management

---

## Priority Tier 1: High-Value Local Leads (Stuart, Port St Lucie, Jupiter, Jensen Beach)

### Property Management Companies
**Target:** HOA property management, apartment complexes, multi-unit operators
**Template:** Template 1 (PM Dashboard) or Template 5 (HOA/COA)
**Estimated Leads:** 100-200 in Treasure Coast area

**Priority Outreach:**
1. [ ] Coastal Property Management (Stuart)
2. [ ] Palm Beach and Martin Counties Property Management
3. [ ] Martin Property Management
4. [ ] Signature Property Management
5. [ ] Property Boss LLC
6. [ ] Local apartment complexes (20+ properties)

**Why First:**
- KMJK is already in Treasure Coast
- Local = trust + fast response
- PM dashboard = strong value prop
- Can do site visits for quotes

---

### Auto Dealerships (Epoxy Focus)
**Target:** Auto body shops, dealerships, car washes
**Template:** Template 3 (Auto Shop Epoxy)
**Estimated Leads:** 50-100 in Treasure Coast area

**Priority Outreach:**
1. [ ] All auto dealerships in Stuart, Port St Lucie, Jupiter
2. [ ] Auto body shops in Treasure Coast
3. [ ] Car washes and detailing services

**Why Second:**
- Epoxy floors = high margin, quick job
- Visual impact (before/after photos work well)
- Low coordination (one contact, one decision maker)
- Can quote remotely (square footage estimate)

---

### Restaurants (Commercial Kitchen)
**Target:** Restaurants, commercial kitchens, catering
**Template:** Template 4 (Restaurant Kitchen)
**Estimated Leads:** 50-100 in Treasure Coast area

**Priority Outreach:**
1. [ ] Local restaurants in Stuart, Jensen Beach, Port St Lucie
2. [ ] Country clubs with food service
3. [ ] Catering companies

**Why Third:**
- Health inspector angle = urgency
- Commercial kitchen = higher ticket
- Night/weekend work = less disruption
- Can work around restaurant hours

---

## Priority Tier 2: High-Value Statewide (Florida Metro Areas)

### Tampa / St. Petersburg / Clearwater
**Total Leads:** ~1,139
**Categories:** All 30+ categories represented
**Strategy:** Focus on PM, auto dealers, restaurants first

**Top Targets:**
1. [ ] Property management companies (Tampa Bay area)
2. [ ] Auto dealerships (Car dealers, body shops)
3. [ ] Restaurants (downtown Tampa, St. Pete)
4. [ ] HOA communities (Clearwater, St. Pete Beach)

**Why Fourth:**
- Larger market = more volume
- 3-4 hours drive from Stuart (serviceable)
- Higher concentration of businesses

---

### Miami / Fort Lauderdale
**Total Leads:** ~500+
**Categories:** All 30+ categories
**Strategy:** Focus on high-ticket jobs (epoxy, full kitchen reno)

**Top Targets:**
1. [ ] Luxury property management (Miami Beach, Coral Gables)
2. [ ] High-end auto dealerships (Porsche, BMW, Mercedes)
3. [ ] Fine dining restaurants (South Beach, Wynwood)
4. [ ] Yacht clubs (epoxy floors, marine services)

**Why Fifth:**
- Higher ticket = better ROI
- Luxury clients = less price-sensitive
- Can charge premium for quality

---

### Jacksonville / Gainesville / Tallahassee
**Total Leads:** ~1,100+
**Categories:** All 30+ categories
**Strategy:** Focus on commercial/industrial clients

**Top Targets:**
1. [ ] Industrial plants (epoxy floors, large scale)
2. [ ] Warehouses (coatings, flooring)
3. [ ] Cold storage facilities (specialized epoxy)
4. [ ] Hospitals/medical facilities (renovations)

**Why Sixth:**
- Industrial = large contracts
- Commercial = recurring work
- Can scale team for big jobs

---

## Priority Tier 3: Specialist Categories (High-Ticket, Niche)

### Industrial & Commercial
**Categories:**
- Industrial plant manager (420 leads)
- Warehouse owner (392 leads)
- Cold storage facility (414 leads)
- Aircraft hangar (391 leads)

**Strategy:**
- Custom proposals (large-scale epoxy, specialized coatings)
- Bid on commercial contracts
- Target facility managers (not owners)

---

### Medical & Healthcare
**Categories:**
- Hospital medical facility (417 leads)
- Dental office (391 leads)
- Daycare center (425 leads)

**Strategy:**
- Focus on safety/compliance (non-slip, health code)
- Target facility managers/admins
- Emphasize quick turnaround (can't close operations long)

---

### Niche Categories
**Categories:**
- Fire station (378 leads)
- Church religious facility (376 leads)
- School (if available)

**Strategy:**
- Government/bid contracts (fire stations)
- Community-focused (churches, schools)
- Bulk discounts (multiple facilities)

---

## Outreach Campaign Schedule

### Week 1: Local Treasure Coast
- **Day 1-2:** Property management companies (50 leads)
- **Day 3-4:** Auto dealerships (30 leads)
- **Day 5:** Restaurants (20 leads)

### Week 2: Tampa Bay Area
- **Day 1-3:** Property management (100 leads)
- **Day 4-5:** Auto dealerships (50 leads)

### Week 3: Miami / Fort Lauderdale
- **Day 1-3:** Luxury property management (50 leads)
- **Day 4-5:** High-end auto + fine dining (40 leads)

### Week 4: Rest of Florida
- **Day 1-5:** Mix of industrial, medical, commercial (150 leads)

---

## Outreach Metrics to Track

### Per Campaign
- [ ] Emails sent: ___
- [ ] Opens: ___ (___%)
- [ ] Clicks: ___ (___%)
- [ ] Replies: ___ (___%)
- [ ] Phone calls from email: ___

### By Category
- [ ] Property management: ___ sent, ___% response
- [ ] Auto dealerships: ___ sent, ___% response
- [ ] Restaurants: ___ sent, ___% response
- [ ] Industrial/commercial: ___ sent, ___% response

### By Template
- [ ] Template 1 (PM Dashboard): ___ sent, ___% response
- [ ] Template 2 (Mission Log): ___ sent, ___% response
- [ ] Template 3 (Auto Shop): ___ sent, ___% response
- [ ] Template 4 (Restaurant): ___ sent, ___% response
- [ ] Template 5 (HOA/COA): ___ sent, ___% response

---

## Lead Database Queries (for extraction)

### Treasure Coast Property Management
```sql
SELECT company, city, state, email, phone, website
FROM leads
WHERE city IN ('Stuart', 'Port St Lucie', 'Jupiter', 'Jensen Beach', 'Palm City', 'Sewall\'s Point')
  AND (category LIKE '%property management%' OR category LIKE '%HOA%')
  AND email IS NOT NULL
ORDER BY city, company
LIMIT 100
```

### Treasure Coast Auto Dealerships
```sql
SELECT company, city, state, email, phone, website
FROM leads
WHERE city IN ('Stuart', 'Port St Lucie', 'Jupiter', 'Jensen Beach')
  AND category LIKE '%auto%'
  AND email IS NOT NULL
ORDER BY city, company
LIMIT 50
```

### Tampa Bay Property Management
```sql
SELECT company, city, state, email, phone, website
FROM leads
WHERE city IN ('Tampa', 'St. Petersburg', 'Clearwater', 'Bradenton', 'Sarasota')
  AND (category LIKE '%property management%' OR category LIKE '%HOA%')
  AND email IS NOT NULL
ORDER BY city, company
LIMIT 100
```

### High-End Miami Auto Dealerships
```sql
SELECT company, city, state, email, phone, website
FROM leads
WHERE city IN ('Miami', 'Miami Beach', 'Coral Gables', 'Fort Lauderdale')
  AND category LIKE '%auto%'
  AND email IS NOT NULL
ORDER BY city, company
LIMIT 50
```

### Industrial / Commercial (Statewide)
```sql
SELECT company, city, state, category, email, phone, website
FROM leads
WHERE category IN ('industrial plant manager', 'warehouse owner', 'cold storage facility', 'aircraft hangar')
  AND email IS NOT NULL
ORDER BY city, company
LIMIT 100
```

---

## Next Steps

1. ✅ **GitHub repository inventory** - Complete
2. ✅ **Email templates upgraded** - Complete (with PM dashboard features)
3. ✅ **Lead list organized** - This document
4. ⏳ **Extract leads for Week 1 campaign** - Ready to start
5. ⏳ **Set up email delivery system** - Zoho Mail or ESH Mail
6. ⏳ **Create tracking system** - Email opens, clicks, replies
7. ⏳ **Build visual assets** - Before/after photos, dashboard screenshots
8. ⏳ **Start Week 1 outreach** - Property management in Treasure Coast

---

## Questions for Chris

1. **Email Delivery:** Should we use Zoho Mail or wait for ESH Mail MVP?
2. **Dashboard Screenshots:** Should I mock up the PM dashboard features now?
3. **Before/After Photos:** Do you have photos of completed jobs I can use?
4. **Email Volume:** How many emails per day? (10, 20, 50?)
5. **Tracking:** Do you want open/click tracking, or just basic email delivery?
6. **Priority:** Should I start Week 1 outreach immediately, or wait for email system?

---

_Last updated: 2026-02-14 12:40 UTC_
