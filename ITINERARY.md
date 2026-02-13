# ITINERARY - Feb 13, 2026

## STATUS: SYSTEM OPERATIONAL
- Gateway: systemd service, active, GLM-5 available
- Telegram: @GlitchGobot polling, responding
- Lead Bank: 16,400+ leads, 2,647 with email
- Brave Search: configured as primary (Z.AI search dead until March 1)
- Crons: all running (scraper, guesser, dashboard, GitHub, repo agent)
- Dashboard: http://107.172.20.181:8080

## CHRIS MUST DO (Human Tasks)
### This Week
1. **Buy Instantly DFY sending accounts** ($30) - Gen 2, US-based IPs
   - Go to: https://instantly.ai -> DFY Accounts
   - Buy 2-3 accounts minimum for warm-up
   - Connect them to your Instantly workspace
   - They auto-warm for 14 days
2. **Buy KMJK-adjacent domain** (~$10) - for cold outreach
   - e.g., kmjkservices.com or kmjkhomeservices.com
   - Point MX records to your email provider
   - NEVER use kmjk.pro for cold email
3. **Buy Brave Search Pro** ($5/mo) - 20K queries/month vs 2K free
   - Go to: https://brave.com/search/api/
   - Upgrade existing key or get new one
   - Update BRAVE_API_KEY in crontab if key changes
4. **Buy MillionVerifier credits** ($299/500K) - bulk email verification
   - Go to: https://millionverifier.com
   - Credits applied to existing API key

### When Email Accounts Are Ready (after 14-day warmup)
5. **Create campaign sequences in Instantly**
   - 3-email drip sequence per lead type
   - Client outreach: "We found your property..."
   - Contractor recruitment: "We have leads in your market..."
6. **Start sending** - 200/day per account, scale up

## GLITCH MUST DO (Automated Tasks)
### Daily (Already Running)
- National scraper: every 4 hours (Brave, 15 queries)
- Apollo guesser: every 2 hours (SMTP email enrichment)
- Dashboard rebuild: every 30 min
- GitHub push: hourly
- Lead verification: nightly
- Repo improvement: nightly at midnight EST

### Weekly Goals
- Grow lead bank by 500-1000 leads/week
- Enrich 200+ leads with email patterns
- Improve 5 GitHub repos per night
- Generate morning executive reports
- Monitor site health (kmjk.pro, chriscotton.me)

### When Chris Buys Instantly Accounts
- Help configure sending campaigns
- Create email templates via outreach-writer agent
- Set up Instantly V2 API integration
- Monitor deliverability and response rates

### When Brave Pro Activates
- Increase scraper batch size from 15 to 50 queries
- Run overnight marathons more frequently
- Expand to Phase 2 FL markets aggressively

## BUSINESS PLAN SUMMARY
### Phase 1 (NOW): Josue/KMJK - Jensen Beach FL
- Target: $70K+ in kitchen/bath/epoxy projects
- Status: 16K+ leads in bank, enriching daily

### Phase 2: Expand FL
- Markets: Naples, Boca, Sarasota, Jupiter, WPB
- Need: 3-4 contractors per market
- Timeline: After email campaigns prove ROI

### Phase 3: National
- 15+ US markets, 3-4 contractors each
- Scale target: 200 contractors x $4,500-9,000/mo = $25M ARR

## KEY CONTACTS
- **Chris (texts):** 772-777-0622
- **Josue (calls):** 772-323-3776
- **Email:** info@kmjk.pro
- **Website:** https://kmjk.pro

## SYSTEM REFERENCE
- **VPS:** 107.172.20.181 (SSH: chris/a)
- **Gateway:** systemd, port 18789, OpenClaw v2026.2.9
- **Dashboard:** PM2 "glitch-v2", port 8080
- **CRM:** screen "crm", port 8181
- **Models:** GLM-5 (primary), GLM-4.7, 4.7-flash, 4.6, 4.5, 4.5-air
- **Search:** Brave API (primary), Z.AI webSearch (dead until March 1)
