# Business Advisory Council

The final piece of the 26-system CRM build. A parallel AI expert system that provides intelligent business recommendations.

## Overview

The Business Advisory Council runs 8 independent AI specialists in parallel, each analyzing only their relevant domain data. A synthesizer then merges findings, eliminates duplicates, and ranks by priority.

## Advisors

| Advisor | Icon | Focus |
|---------|------|-------|
| Revenue Guardian | 💰 | Revenue, YouTube analytics, earnings |
| Growth Strategist | 📈 | Audience growth, Instagram, Twitter |
| Skeptical Operator | ⚙️ | Operations, cron jobs, system health |
| Customer Champion | 👥 | CRM, customer success, retention |
| Content Architect | 📝 | Content strategy, newsletters |
| Data Sherlock | 🔍 | Analytics, patterns, trends |
| Financial Steward | 💎 | Costs, ROI, profitability |
| Innovation Catalyst | 💡 | New opportunities, products |

## Usage

### Run Full Analysis
```bash
python3 ~/.openclaw/bin/business_advisory.py
```

### Run Single Advisor
```bash
python3 ~/.openclaw/bin/business_advisory.py --advisor revenue_guardian
```

### Deep Dive on Item
```bash
python3 ~/.openclaw/bin/business_advisory.py --deep-dive 3
```

### Record Feedback (Learning)
```bash
python3 ~/.openclaw/bin/business_advisory.py --approve 3
python3 ~/.openclaw/bin/business_advisory.py --reject 7
```

### Check Status
```bash
python3 ~/.openclaw/bin/business_advisory.py --status
```

## Data Sources

The system collects data from:
- YouTube Analytics (cached)
- Instagram Analytics (cached)
- Twitter/X Analytics (cached)
- CRM Database (personal_crm SQLite)
- HubSpot Contacts
- Email Inbox
- Meeting Transcripts
- Cron Job Status
- Slack Notifications
- Asana Tasks
- Newsletter Performance
- Earnings Reports
- Cost Reports
- System Health

Each advisor ONLY sees their relevant data sources.

## Output

### Telegram Digest
Numbered list of 10-12 prioritized insights sent to Telegram meta_analysis topic.

Example:
```
🧠 Business Advisory Council
Generated: 2026-02-17 20:30 UTC
Advisors consulted: Revenue Guardian, Growth Strategist, ...

1. 🔴 YouTube CTR dropped 15% this week - consider A/B testing thumbnails
   Advisors: revenue_guardian, data_sherlock

2. 🟡 Instagram engagement up 20% after switching to carousel format
   Advisors: growth_strategist, content_architect

...
```

### Deep Dive
When you say "tell me more about #3", the system provides:
- Full insight details
- Supporting advisors with their credentials
- Action steps
- Context from relevant data

### Feedback Loop
- `/approve 3` - Boosts similar insights from these advisors
- `/reject 7` - Reduces confidence in similar insights

## Configuration

### Advisors Config
`~/.openclaw/workspace/config/advisors.json`

- Defines 8 advisors with:
  - System prompts
  - Data source assignments
  - Expertise areas
  - Priority keywords

### State Management
`~/.openclaw/workspace/state/business_advisory_state.json`

- Last digest
- Digest items
- Feedback history
- Advisor performance scores

## Files

| Location | Purpose |
|----------|---------|
| `~/.openclaw/bin/business_advisory.py` | Main script |
| `~/.openclaw/workspace/config/advisors.json` | Advisor configuration |
| `~/.openclaw/workspace/digests/` | Digest outputs (JSON + TXT) |
| `~/.openclaw/workspace/deep_dives/` | Deep dive outputs |
| `~/.openclaw/workspace/cache/` | Data cache |

## Parallel Processing

All 8 advisors run in parallel (ThreadPoolExecutor, max 8 workers). No advisor sees another's output - pure independent analysis.

## Synthesis Process

1. Collect all insights from 8 advisors
2. Send to AI Synthesizer
3. Merge related/duplicate insights
4. Rank by business impact and urgency
5. Return top 10-12 items

## Learning System

The system learns from your feedback:

- **Approved items**: Boost confidence in similar insights from same advisors
- **Rejected items**: Reduce confidence in similar insights
- **Advisor performance**: Track approval rate per advisor

## Integration with CRM

This is system #26 of the 26-system CRM build. It integrates with:
- personal_crm.py (customer data)
- platform_health.py (system health)
- earnings_reports.py (financial data)
- All other CRM systems via cached data

## Example Workflow

1. **Morning**: Run analysis, get digest
2. **Review**: Read through 10-12 items
3. **Deep Dive**: Say "tell me more about #3" for details
4. **Action**: Implement recommendations
5. **Feedback**: Next day, mark items as approve/reject
6. **Learning**: System adapts to your preferences

## Scheduling

Recommended: Run every 6 hours (configurable)

```bash
# Add to crontab
0 */6 * * * /home/chris/.openclaw/bin/business_advisory.py
```

## Troubleshooting

### No insights generated
- Check data cache files in `~/.openclaw/workspace/cache/`
- Verify AI API keys are correct
- Check logs: `~/.openclaw/workspace/logs/`

### Advisor errors
- Check data source availability
- Review advisor config in advisors.json
- Run single advisor to debug

### Telegram not sending
- Verify telegram_topics.json has channel_id and bot_token
- Check bot permissions
- Digest will be saved to file as fallback
