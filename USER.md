# USER.md — Chris

## Identity
- **Name:** Chris
- **Company:** Elite Service Hub
- **Role:** Founder — built this entire AI operations system from scratch
- **GitHub:** QuantumCotton
- **VPS:** 107.172.20.181 (RackNerd, SSH: chris)

## What Chris Does
Chris connects contractors to clients through technology. He built Elite Service Hub to automate lead generation, outreach, and client acquisition for contractors who are too busy working to market themselves. He earns commission on every contract landed through his system.

## The Revenue Model
```
1. AI finds leads (property managers, auto shops, restaurants, etc.)
2. AI drafts personalized outreach emails
3. Chris reviews and sends outreach
4. Josue (KMJK Group) does the work
5. Chris earns commission from Elite Service Hub
6. Repeat. Scale. Add more contractors.
```

## Current Contractor: Josue (KMJK Group)
- Epoxy flooring, kitchen renovation, property maintenance, mobile detailing
- Based in Stuart, FL — serves Palm Beach to Vero Beach
- Phone: 772-323-3776
- Reference client: PSR Homes LLC (22 units, Boca Raton)

## Phase 2 Plan
Once Josue's pipeline is stable and generating consistent leads:
1. Identify 5 more contractors in different cities doing similar work
2. Clone the lead gen playbook for each contractor
3. Each contractor gets: their own agent team, cron schedule, lead pipeline, dashboard
4. Scale Elite Service Hub into a nationwide contractor services platform
5. Target cities: Tampa, Orlando, Jacksonville, Atlanta, Charlotte (TBD)

## Communication Preferences
- **Telegram** for daily summaries (keep under 500 words)
- **HTML reports** for detailed breakdowns (push to GitHub)
- **Dashboard** for real-time monitoring
- Don't message between 11pm-7am ET unless it's critical
- Prefers action over permission — do the work, report results
- Wants to see: lead count, phone numbers, top priorities, conversion tracking

## Autonomy Rules — What You Can Do Without Asking
- Search the web for leads
- Scrape business websites for contact info
- Append leads to master_leads.csv
- Draft outreach emails (save to drafts/, never send)
- Generate and send Telegram reports
- Upload HTML reports to GitHub
- Update MEMORY.md and daily memory files
- Run scheduled cron tasks per HEARTBEAT.md

## What Requires Chris's Approval
- Sending any email or message to a lead/client
- Deleting any file
- Installing new software or packages
- Making changes to openclaw.json or gateway config
- Any financial transaction or commitment
- Posting anything publicly (social media, forums)
- Changing cron schedules or agent configurations

## How Chris Wants Problems Reported
1. **One-liner via Telegram** — what broke, what you tried, what you need
2. Don't send a wall of text. Don't send a stack trace. Summarize.
3. If it's blocking lead generation, mark as URGENT
4. If it's cosmetic or non-blocking, note it in errors.log and move on
