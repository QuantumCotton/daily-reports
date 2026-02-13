# AGENTS.md - Agent Coordination

## Active Agents
| Agent | Model | Role |
|-------|-------|------|
| lead-scout | zai/glm-4.6 | Find, enrich, verify leads via Z.AI search |
| outreach-writer | zai/glm-4.6 | Draft cold outreach emails |
| strategy-planner | zai/glm-4.5-air | Rank leads, reports, GitHub push |
| seo-analyst | zai/glm-4.5-air | Web presence, competitors |

## HOW TO SEARCH (ALL AGENTS MUST USE THIS)
```bash
exec python3 ~/.openclaw/bin/zai_search.py "your query"
exec python3 ~/.openclaw/bin/zai_search.py --reader "https://url.com"
```

## Pipeline
```
lead-scout -> master_leads.csv -> outreach-writer -> drafts/ -> Chris sends
                    |
            strategy-planner -> Telegram + GitHub
                    |
            seo-analyst -> competitor intel
```

## Agent Startup Protocol
1. Read your AGENT.md
2. Read SOUL.md
3. Read TOOLS.md (USE zaisearch!)
4. Check HEARTBEAT.md
5. Execute tasks
6. Update MEMORY.md

## Rules
- lead-scout writes CSV, others read
- outreach-writer reads leads, writes drafts only
- strategy-planner reads all, writes reports, pushes GitHub
- No agent sends emails - drafts only
