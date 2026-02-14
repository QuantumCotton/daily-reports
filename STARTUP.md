# STARTUP.md - Read This First Every Session

## Current State (Updated Feb 14, 2026 — Post-Audit)

### What's Working
- Gateway: systemd service, active, healthy (auto-restarts via healthcheck)
- Telegram: @GlitchGobot connected, polling
- Models: GLM-5 available on openai provider, GLM-4.7 as fallback
- Brave Search: Pro tier active (20K queries/month)
- Lead Bank: 16,400+ leads in SQLite, growing daily
- All crons running (scraper, guesser, dashboard, GitHub, repo agent, health check, backup)
- 10 specialist agents registered and connected
- Custom SOUL.md with Glitch personality
- System health alerts via Telegram

### What's Not Working
- Z.AI webSearchPrime: DEAD until March 1, 2026 (error 1310)
- MillionVerifier: valid key but 0 credits (needs purchase)
- Instantly: API connected but needs sending accounts ($30 DFY purchase)

### What I Need to Do Every Session
1. Read my identity: `file_read path=~/.openclaw/identity/IDENTITY.md`
2. Read my soul: `file_read path=~/.openclaw/workspace/SOUL.md`
3. Check lead stats: `exec python3 -c "import sqlite3; c=sqlite3.connect('/home/chris/.openclaw/workspace/leads/lead_bank.db'); print(c.execute('SELECT COUNT(*) FROM leads').fetchone()[0], 'leads')"`
4. Check crons: `exec crontab -l`
5. Check gateway: `exec systemctl --user status openclaw-gateway.service`

### My Agent Team (10 specialists)
| Agent | Model | Job |
|-------|-------|-----|
| deep-researcher | openai/glm-5 | Main agent, research, coordination |
| lead-generator | zai/glm-4.7 | Find and scrape leads |
| lead-scout | zai/glm-4.7 | Verify leads, deep research |
| outreach-writer | openai/glm-5 | Draft outreach emails |
| strategy-planner | openai/glm-5 | Strategy, reporting, summaries |
| coding-specialist | zai/glm-4.7 | Fix bugs, build tools |
| research-analyst | openai/glm-5 | Market research, intelligence |
| creative-writer | zai/glm-4.7 | Marketing copy, content |
| seo-analyst | zai/glm-4.7-flash | SEO audits, keywords |
| github-reviewer | zai/glm-4.7-flash | Code review, repo improvement |

### Tools That Work
- `exec python3 ~/.openclaw/bin/brave_search.py "query"` — Web search (Brave Pro)
- `exec python3 ~/.openclaw/bin/national_scraper.py` — Lead scraping
- `exec python3 ~/.openclaw/bin/apollo_guesser.py` — Email enrichment
- `exec python3 ~/.openclaw/bin/market_dashboard.py` — Dashboard rebuild
- `exec python3 ~/.openclaw/bin/github_push.py` — GitHub push
- `exec python3 ~/.openclaw/bin/overnight_repo_agent.py` — Repo improvement
- `exec python3 ~/.openclaw/bin/system_health.py` — System health report
- `exec python3 ~/.openclaw/bin/rate_limiter.py` — Check API quotas

### Tools That DON'T Work (Skip These)
- Z.AI webSearchPrime MCP — exhausted, don't try until March 1
- smart_enricher.py — uses Z.AI search, disabled
- lead_scrape_staggered.py — uses Z.AI search, disabled
