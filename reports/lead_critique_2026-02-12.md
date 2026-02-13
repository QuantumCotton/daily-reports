# Lead Generation Critique — 2026-02-12 19:52 UTC

## Executive Summary

**Total Leads Collected:** 622 leads (including header)
**Actual Businesses:** ~400+ estimated (after removing low-quality entries)

---

## Data Quality Issues

### 🔴 CRITICAL ISSUES

1. **Directory Listings Masquerading as Businesses (50-100+ leads)**
   - **Problem:** Search results from directory sites being saved as leads
   - **Examples:**
     - `"Apartments for Rent in Fort Pierce FL"` (Apartments.com)
     - `"Best Property Management Companies in Port St. Lucie, FL"` (Expertise.com)
     - `"Auto Body Shop near Port Saint Lucie, FL 34952"` (Carwise.com)
   - **Impact:** These aren't businesses - they're search result pages
   - **Action Needed:** Filter out directory domains, extract actual business names from pages

2. **Business Names Contain SEO Text**
   - **Problem:** Names include location/search terms instead of clean company names
   - **Examples:**
     - `"Martin, FL Property Management Companies"` → Should be "Campbell Property Management"
     - `"Auto Body Shop near Port Saint Lucie, FL 34952"` → Should be "Zimmer Collision"
   - **Impact:** Makes outreach look spammy and unprofessional
   - **Action Needed:** Parse business name from page content, not search result title

3. **Missing Contact Information (~60-70% of leads)**
   - **Problem:** Phone and email fields are empty
   - **Impact:** Cannot reach out without phone or email
   - **Action Needed:** Enrichment step - scrape contact pages directly

4. **Malformed CSV Rows**
   - **Problem:** Some rows have escaped quotes, extra fields
   - **Impact:** CSV parsing errors
   - **Example:** `"Martin, FL Property Management Companies",,,https://...`
   - **Action Needed:** CSV validation and cleanup script

---

## Quality Metrics

### High Quality Leads (estimated 200-250)
- ✅ Phone number present
- ✅ Website verified and accessible
- ✅ Business name is actual company name
- ✅ Address information available
- ✅ Category correctly classified

### Medium Quality Leads (estimated 100-150)
- ⚠️ Phone present OR email present (not both)
- ⚠️ Business name needs cleanup
- ⚠️ Address incomplete

### Low Quality Leads (estimated 150-200)
- ❌ No phone or email
- ❌ Directory/listing page, not actual business
- ❌ Business name is generic/description

---

## Category Distribution

| Category | Count | Quality Issue |
|-----------|--------|---------------|
| FL (state) | 216 | **DATA ERROR** - Category field contains state |
| esh_scout | 66 | Good source, needs enrichment |
| real_estate | 29 | Mixed quality |
| property_mgmt | 28 | Good target |
| restaurant | 24 | Need phone/email |
| auto | 23 | Need phone/email |
| hoa | 18 | Good target |
| detailing | 18 | Need phone/email |
| property_manager | 15 | Good target |
| cleaning | 12 | Need phone/email |
| apartment_complex | 12 | **Many are directories** |
| kitchen | 11 | Good target |
| healthcare | 11 | Need phone/email |
| epoxy | 10 | Good target |
| construction | 10 | Good target |

---

## Priority Analysis

| Priority | Count | Notes |
|----------|--------|--------|
| High | 233 | Good pipeline |
| Medium | 42 | Some low-quality mixed in |
| Low | 78 | Many have no contact info |
| 2026-02-12 (ERROR) | 240 | **Priority column contains dates** |

---

## Geographic Distribution

| City | Count | Priority |
|-------|--------|----------|
| (empty) | 249 | **DATA ERROR** - 40% missing city |
| Stuart | 187 | Good focus area |
| Jensen Beach | 29 | Good |
| Port St Lucie | 24 | Good |
| Palm City | 18 | Good |
| West Palm Beach | 14 | Expansion target |
| Boca Raton | 12 | Expansion target |
| Naples | 9 | Expansion target |

---

## Search Source Analysis

### websearch (early, ~100-150 leads)
- Higher quality generally
- Some directory listings slipped through
- Good variety of sources

### zai_search (~400+ leads)
- Main driver of volume
- **Major issue:** Directory pages being saved as leads
- Category classification errors (216 as "FL" state)

---

## What's Working Well

✅ **Volume:** 600+ leads collected in 8 hours is solid
✅ **Geographic Focus:** Heavy concentration in target market (Stuart/Palm City/Jensen Beach)
✅ **Category Mix:** Good spread across 17 service types
✅ **Automation:** Z.AI search is working reliably
✅ **GitHub Pushes:** Committing regularly, good tracking

---

## What Needs Immediate Fix

### 1. Filter Out Directory Domains
Create blacklist and skip these results:
- apartments.com
- realtor.com
- expertise.com
- carwise.com
- zillow.com/professionals
- yelp.com (listings, not business pages)
- angi.com (listings)

### 2. Enrichment Phase
Run second pass to get contact info:
```
For each lead without phone/email:
  1. Visit website
  2. Look for Contact page
  3. Extract phone number
  4. Look for email addresses
  5. Update CSV
```

### 3. CSV Cleanup Script
Fix malformed rows:
- Remove escaped quotes
- Clean business names
- Fix priority column (remove dates, use High/Medium/Low)
- Standardize city/state

### 4. Deduplication
Remove exact duplicates:
- Same business name + city
- Same website URL

---

## Recommended Actions

### Before Resuming Lead Gen:

1. **Stop current scraping** ✅ (Done)
2. **Run cleanup script** to remove directories
3. **Run enrichment** to get phone/email
4. **Manual review** of top 50 High priority leads
5. **Test outreach** on 5-10 leads

### Then Resume With:

**Updated search queries:**
- Add `"business_name contact"` to searches
- Exclude directory terms
- Focus on specific business types

**Better extraction:**
- Parse actual business name from page content
- Extract phone number from contact pages
- Verify email addresses exist

---

## Estimated Viable Leads After Cleanup

| Before | After Cleanup | Viable for Outreach |
|---------|---------------|---------------------|
| 622 | ~300-350 | ~150-200 |

**We have enough to work with!** Focus on quality over quantity for training.
