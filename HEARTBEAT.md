# HEARTBEAT.md - Automated Task Schedule

## Contact Info
- **Call Josue:** 772-323-3776
- **Text Chris:** 772-777-0622
- **Email:** info@kmjk.pro | **Website:** https://kmjk.pro

## HOW TO SEARCH THE WEB
```bash
exec python3 ~/.openclaw/bin/zai_search.py "your search query"
exec python3 ~/.openclaw/bin/zai_search.py --reader "https://url-to-read.com"
```
This is Z.AI webSearchPrime. Unlimited. No rate limits. Returns JSON.

## Schedule (Eastern Time)

### Pressure Test Mode (Active Feb 12-13)
Every 15 minutes, 8 hours of hammering. ~100 queries per cycle.

### Normal Mode (After Pressure Test)
| Time | Task | Agent |
|------|------|-------|
| 11:00 PM | Heavy scrape - all services, all cities | lead-scout |
| 2:00 AM | Dedup + enrich leads (phone/email) | lead-scout |
| 5:00 AM | Draft outreach for High priority | outreach-writer |
| 6:00 AM | Draft outreach for Medium priority | outreach-writer |
| 7:00 AM | Strategy review + lead scoring | strategy-planner |
| 8:00 AM | SEO check (Wednesdays) | seo-analyst |
| 9:00 AM | Daily summary -> Telegram + GitHub | strategy-planner |
| 12:00 PM | Light scrape (5 searches) | lead-scout |
| 3:00 PM | Follow-up drafts | outreach-writer |
| 6:00 PM | Light scrape (5 searches) | lead-scout |
| 10:00 PM | Verify random sample of leads | lead-scout |
| 10:30 PM | Push leads to GitHub | strategy-planner |

### Hourly (Always)
- Push leads CSV to GitHub (QuantumCotton/daily-reports)

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

## ESH Expansion (Phase 2)
Target high-income US markets: Naples, Boca Raton, Sarasota, Jupiter, West Palm, Scottsdale, Austin, Nashville, Charlotte.
Each market: 3-4 contractors (kitchen/bath, epoxy, detailing, GC).

## Error Handling
- Search empty 3x -> try different phrasing
- CSV write fails -> log + Telegram alert
- Never crash entire scrape for one failed search

## File Locations
| File | Path |
|------|------|
| Lead CSV | ~/.openclaw/workspace/leads/master_leads.csv |
| Z.AI search | ~/.openclaw/bin/zai_search.py |
| Pressure test | ~/.openclaw/bin/pressure_test.py |
| Lead verifier | ~/.openclaw/bin/lead_verifier.py |
| GitHub push | ~/.openclaw/bin/github_push.py |
