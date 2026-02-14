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


## SearXNG — Self-Hosted Search Engine (Docker)

### What It Is
A self-hosted meta search engine running in Docker. Aggregates results from 8 search
engines (Google, Bing, DDG, Yahoo, Brave, Mojeek, Qwant, Startpage). Completely free.

### Usage
```bash
# JSON API (from any script or curl):
curl "http://127.0.0.1:8888/search?q=plumber+Stuart+FL&format=json"

# From Python:
from free_search import search_searxng
results = search_searxng("plumber Stuart FL")

# Or use the unified search (auto-picks best tier):
from free_search import search
results = search("plumber Stuart FL")
```

### Management
```bash
# Check status
echo a | sudo -S docker ps --filter name=searxng

# Restart
echo a | sudo -S docker restart searxng

# View logs
echo a | sudo -S docker logs searxng --tail 20

# Full restart (pull latest + recreate)
cd ~/searxng && echo a | sudo -S docker-compose down && echo a | sudo -S docker-compose up -d

# Config location
~/searxng/settings.yml      # Search engine config
~/searxng/docker-compose.yml  # Container config
```

### Config Details
- Port: localhost:8888 (mapped to container port 8080)
- Memory limit: 512 MB
- CPU limit: 1 core
- Limiter: OFF (no rate limiting for local use)
- Image proxy: OFF
- Safe search: OFF

## Free Search — 3-Tier Search Library

### What It Is
Drop-in search function that tries SearXNG first (free), then DDG via home PC proxy
(free, residential IP), then Brave API (paid fallback).

### Usage
```python
from free_search import search, search_searxng, search_ddg_proxy, search_brave

# Unified (auto-picks best available):
results = search("your query here")

# Specific tier:
results = search_searxng("query")     # Tier 1: SearXNG
results = search_ddg_proxy("query")   # Tier 2: DDG via home proxy
results = search_brave("query")       # Tier 3: Brave API

# Each returns: [{"title": "...", "url": "...", "snippet": "..."}, ...]
```

### CLI
```bash
cd ~/.openclaw/bin && python3 free_search.py "kitchen remodeling Jensen Beach FL"
```
Shows results from all 3 tiers with counts.

## Home PC Proxy — Residential IP Tunnel

### What It Is
Chris's home PC (Windows 11, 1Gbps internet) runs an SSH reverse tunnel that lets
the VPS route web requests through a residential IP. This bypasses DDG datacenter
IP blocking.

### Availability
- **Active:** ~1:30 AM - 9:00 AM PST (Chris starts it before bed)
- **Check:** Port 1080 open = proxy is live
```python
import socket
s = socket.socket(); s.settimeout(2)
try:
    s.connect(("127.0.0.1", 1080)); s.close()
    print("PROXY LIVE")
except:
    print("PROXY OFFLINE")
```

### How It Works
```
VPS port 1080 → SSH tunnel → Home PC port 8118 → Home internet → DDG/websites
```
The `free_search.py` library automatically detects if the proxy is available and
uses it. No manual configuration needed.

## Lead Enricher v4 — Zero-Cost Email Enrichment

### What It Is
Scrapes business websites directly (/about, /team, /contact pages) to find personal
emails and owner names. No API calls needed.

### How It Works
1. Fetches the company website homepage + /about, /team, /contact pages
2. Finds personal emails via regex (john.smith@company.com)
3. Extracts names from email prefixes (john.smith → John Smith)
4. Falls back to owner name text patterns on page
5. Generates email patterns (first.last@domain) and SMTP verifies

### Usage
```bash
# Enrich 30 leads (default batch)
python3 ~/.openclaw/bin/lead_enricher_v4.py 30

# Enrich specific count
python3 ~/.openclaw/bin/lead_enricher_v4.py 100
```

### Stats
- ~15% enrichment rate (finds email on 15% of websites scraped)
- $0 cost (direct HTTP requests only)
- Runs every 2 hours via cron, 30 leads per batch

## Web Search

### Brave Search (FALLBACK ONLY — Tier 3)
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

## Cron Jobs (crontab -l) — Updated Feb 14, 2026
- Job board scraper: every 20 min (SearXNG, 64 queries, $0)
- Craigslist scraper: 3x/hour ($0)
- National scraper: every 4 hours (SearXNG → Brave fallback)
- Lead enricher v4: every 2 hours, 30 leads (direct website scraping, $0)
- Apollo guesser: every 2 hours on :15 (SMTP verify, $0)
- Directory scraper: 3x/day ($0)
- Bulk verifier: nightly 3 AM UTC
- Lead verifier: nightly 3:30 AM UTC
- Dashboard rebuild: every 30 min
- GitHub push: every 2 hours on :45
- Repo agent: daily 5 AM UTC (midnight EST)
- Gateway health check: every 5 min
- Gateway restart: daily 7 AM UTC (prevents memory leaks)
- SearXNG health check: every 30 min (docker start searxng)
