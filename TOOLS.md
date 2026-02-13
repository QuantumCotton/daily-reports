# TOOLS.md — Available Tools & Scripts

## Lead Generation System (~/.openclaw/bin/)

### National Scraper
```bash
# Run a batch of lead scraping queries (default 15, override with SCRAPE_BATCH)
SCRAPE_BATCH=50 BRAVE_API_KEY=BSAfZ4u2UIbWxvjMRqKx4rpJwIUg0Za python3 ~/.openclaw/bin/national_scraper.py

# Run overnight marathon (40 batches x 50 queries)
python3 ~/.openclaw/bin/overnight_marathon.py
```
Pulls from scrape_queue in SQLite, searches Brave, stores leads. FL Phase 1 first.

### Lead Database
```bash
# Initialize database, populate metros, migrate CSV
python3 ~/.openclaw/bin/lead_database.py

# Query stats from Python:
from lead_database import get_db, get_stats, init_db
conn = init_db(); stats = get_stats(conn)
```
SQLite at ~/.openclaw/workspace/leads/lead_bank.db
192 metros, 43 states, 30 client + 15 contractor categories.

### Apollo Guesser
```bash
# Enrich leads with email patterns via SMTP verification
python3 ~/.openclaw/bin/apollo_guesser.py
```
No API needed — uses MX records + SMTP to validate email patterns.

### Bulk Verifier
```bash
# Verify emails via MillionVerifier (needs credits)
MILLIONVERIFIER_API_KEY=TeAinz3Gw303dNx0wkReB6C9o python3 ~/.openclaw/bin/bulk_verifier.py
```
Reads unverified from SQLite, verifies 200/batch, updates status.

### CRM Server
```bash
# Start CRM backend (port 8181)
python3 ~/.openclaw/bin/crm_server.py
```
API: /api/leads, /api/national, /api/queue, /api/status, /api/approve, /api/send

### Market Dashboard
```bash
# Rebuild HTML dashboard
python3 ~/.openclaw/bin/market_dashboard.py
```
Generates HTML with approval workflow, market map, contractor/client views.

## Multi-Agent Repo Swarm

### Overnight Repo Agent
```bash
# Run full repo improvement pipeline (5 repos per night)
python3 ~/.openclaw/bin/overnight_repo_agent.py
```
Architecture:
- Coordinator (GLM-4.7-flash, 1 call) — creates improvement plan
- Analyzer swarm (GLM-4.6, 8 parallel per account) — analyzes file chunks
- Worker swarm (GLM-4.5 + GLM-4.5-air, 6 parallel) — implements changes
- Critic swarm (GLM-4.6, parallel) — scores 0-100 across 10 metrics
- SEO audit (GLM-4.5-air, 3 parallel) — technical/on-page/social SEO

Two Z.AI accounts (zai + openai route) for 20+ concurrent agents.
Changes pushed to `agent-improve-YYYYMMDD` branches.
Morning report at ~/daily-reports/morning-report.html

## Web Search

### Brave Search (PRIMARY)
```bash
python3 ~/.openclaw/bin/brave_search.py "your search query"
```
API key: BSAfZ4u2UIbWxvjMRqKx4rpJwIUg0Za
Free tier: 2,000/month. Pro: 20,000/month. Returns 10 results per query.

### Z.AI webSearchPrime (DEAD until March 1, 2026)
Error 1310: Weekly/Monthly Limit Exhausted. Do NOT use.

## AI Models Available

### Z.AI Native (key: 87bb...)
- glm-4.7 (reasoning, 1 concurrent) — use sparingly as coordinator
- glm-4.7-flash (fast reasoning) — good for planning
- glm-4.6 (10 concurrent) — primary analyzer/critic
- glm-4.5 (10 concurrent) — primary worker
- glm-4.5-air (10 concurrent) — bulk tasks
- glm-4.6v (vision) — image analysis
- glm-ocr — text extraction from images

### Z.AI OpenAI Route (key: 99a0...)
Same models, doubles concurrency capacity.

### OpenRouter (free)
- stepfun/step-3.5-flash:free
- deepseek-r1t2-chimera:free
- hermes-3-llama-3.1-405b:free

### DO NOT USE
- Google Gemini — mediocre quality, not worth the API call

## Utility Scripts

### Rate Limiter
```bash
python3 -c "from rate_limiter import get_status; print(get_status())"
```
Weekly caps per service, auto-pauses, resets Mondays.

### GitHub Push
```bash
cd ~/daily-reports && git add -A && git commit -m 'update' && git push origin main
```

## Cron Jobs (crontab -l)
- National scraper: every 4 hours
- Apollo guesser: every 2 hours on :30
- Bulk verifier: nightly 3 AM UTC
- Dashboard rebuild: every 30 min
- GitHub push: every 2 hours on :45
- Repo agent: daily 5 AM UTC (midnight EST)
