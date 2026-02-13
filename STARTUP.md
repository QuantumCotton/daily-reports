# STARTUP.md - Read This First Every Session

## Current State (Updated Feb 13, 2026)

### What's Working
- Gateway: systemd service, active, healthy
- Telegram: @GlitchGobot connected, polling
- Models: GLM-5 available on zai provider, GLM-4.7 as fallback
- Brave Search: MCP configured with API key
- Lead Bank: 16,400+ leads in SQLite
- All crons running (scraper, guesser, dashboard, GitHub, repo agent)

### What's Not Working
- Z.AI webSearchPrime: DEAD until March 1, 2026 (error 1310)
- MillionVerifier: valid key but 0 credits (needs purchase)
- Instantly: API connected but no sending accounts yet (needs DFY purchase)
- /tmp/openclaw/ log dir owned by root (gateway can't write today's log)

### What I Need to Do
1. Read my identity: `file_read path=~/.openclaw/identity/IDENTITY.md`
2. Check lead stats: `exec python3 -c "import sqlite3; c=sqlite3.connect('/home/chris/.openclaw/workspace/leads/lead_bank.db'); print(c.execute('SELECT COUNT(*) FROM leads').fetchone()[0], 'leads')"`
3. Check crons: `exec crontab -l`
4. Check gateway: `exec systemctl --user status openclaw-gateway.service`

### Tools That Work
- `exec python3 ~/.openclaw/bin/brave_search.py "query"` - Web search
- `exec python3 ~/.openclaw/bin/national_scraper.py` - Lead scraping
- `exec python3 ~/.openclaw/bin/apollo_guesser.py` - Email enrichment
- `exec python3 ~/.openclaw/bin/market_dashboard.py` - Dashboard
- `exec python3 ~/.openclaw/bin/github_push.py` - GitHub push
- `exec python3 ~/.openclaw/bin/overnight_repo_agent.py` - Repo improvement

### Tools That DON'T Work
- Z.AI webSearchPrime MCP - exhausted, don't try
- smart_enricher.py - uses Z.AI search, disabled
- lead_scrape_staggered.py - uses Z.AI search, disabled
