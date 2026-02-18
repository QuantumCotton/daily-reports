# Model Usage and Cost Tracking System

## Overview

Tracks every AI API call with model usage, tokens, task types, and estimated costs. Logs are stored in JSONL format and reports can be generated on demand.

## Files

- **model_tracker.py** - Logger module for tracking API calls
- **cost_report.py** - CLI tool for generating cost reports
- **install_model_tracker.sh** - Installation script

## Installation

```bash
cd /path/to/agent-coding-specialist-f16066b0
bash install_model_tracker.sh
```

This will:
- Copy files to `~/.openclaw/bin/`
- Create `~/.openclaw/workspace/logs/` for log storage
- Make scripts executable

## Usage

### Logging API Calls

Import and use in your Python code:

```python
from model_tracker import log_api_call

# Log a chat completion
log_api_call(
    provider="anthropic",
    model="claude-3.5-sonnet-20241022",
    input_tokens=1000,
    output_tokens=500,
    task_type="chat",
    session_id="my-session-id",
    metadata={"user": "chris", "feature": "crm-automation"}
)
```

### Generating Reports

```bash
# Daily report (default)
python3 ~/.openclaw/bin/cost_report.py --period daily

# Weekly report
python3 ~/.openclaw/bin/cost_report.py --period weekly

# Monthly report
python3 ~/.openclaw/bin/cost_report.py --period monthly

# All time
python3 ~/.openclaw/bin/cost_report.py --period all
```

### Filtering

```bash
# By provider
python3 ~/.openclaw/bin/cost_report.py --provider anthropic

# By model
python3 ~/.openclaw/bin/cost_report.py --model claude-3.5-sonnet-20241022

# By task type
python3 ~/.openclaw/bin/cost_report.py --task-type chat

# Combine filters
python3 ~/.openclaw/bin/cost_report.py --provider openai --task-type completion

# Custom date range
python3 ~/.openclaw/bin/cost_report.py --start 2024-01-01 --end 2024-01-31

# Detailed view with recent entries
python3 ~/.openclaw/bin/cost_report.py --period weekly --detailed

# JSON output for automation
python3 ~/.openclaw/bin/cost_report.py --period monthly --json
```

## Supported Providers and Models

### Anthropic
- claude-3-opus-20240229
- claude-3-sonnet-20240229
- claude-3-haiku-20240307
- claude-3.5-sonnet-20240620
- claude-3.5-sonnet-20241022

### OpenAI
- gpt-4-turbo
- gpt-4-turbo-preview
- gpt-4
- gpt-4-32k
- gpt-3.5-turbo
- gpt-3.5-turbo-16k
- gpt-4o
- gpt-4o-mini

### Google
- gemini-1.0-pro
- gemini-1.5-pro
- gemini-1.5-flash
- gemini-2.0-flash-exp

### xAI
- grok-2
- grok-beta
- grok-2-vision-1212

## Log Format

Each log entry is a JSON line:

```json
{
  "timestamp": "2024-02-17T20:15:00.000000Z",
  "provider": "anthropic",
  "model": "claude-3.5-sonnet-20241022",
  "input_tokens": 1000,
  "output_tokens": 500,
  "total_tokens": 1500,
  "task_type": "chat",
  "estimated_cost_usd": 0.010500,
  "session_id": "session-123",
  "metadata": {
    "user": "chris",
    "feature": "crm-automation"
  }
}
```

## Pricing

Pricing is included in the code (as of 2024). Costs are calculated in USD per 1K tokens:

- **Input tokens**: Prompt/context tokens
- **Output tokens**: Response generation tokens

To update pricing, edit the `PRICING` dictionary in `model_tracker.py`.

## Example Report Output

```
📊 Cost Report (daily)
📅 2024-02-17 to 2024-02-18

💰 Summary
  Total Calls: 24
  Total Tokens: 45,678
  Total Cost: $1.2345

🏢 By Provider
  anthropic:
    Calls: 15
    Tokens: 32,100
    Cost: $0.8450
  openai:
    Calls: 9
    Tokens: 13,578
    Cost: $0.3895

🤖 By Model
  claude-3.5-sonnet-20241022:
    Calls: 12
    Tokens: 28,500
    Cost: $0.7500
  gpt-4o:
    Calls: 9
    Tokens: 13,578
    Cost: $0.3895
  gemini-1.5-flash:
    Calls: 3
    Tokens: 3,600
    Cost: $0.0950

📋 By Task Type
  chat:
    Calls: 18
    Tokens: 38,200
    Cost: $1.0200
  completion:
    Calls: 6
    Tokens: 7,478
    Cost: $0.2145
```

## Quick Reference for Chris

Check costs anytime with:

```bash
# Today's spend
python3 ~/.openclaw/bin/cost_report.py --period daily

# This week's spend
python3 ~/.openclaw/bin/cost_report.py --period weekly

# This month's spend
python3 ~/.openclaw/bin/cost_report.py --period monthly

# All-time spend
python3 ~/.openclaw/bin/cost_report.py --period all

# Filter to specific model (e.g., Claude 3.5 Sonnet)
python3 ~/.openclaw/bin/cost_report.py --model claude-3.5-sonnet-20241022 --period monthly

# See what tasks cost the most
python3 ~/.openclaw/bin/cost_report.py --period all --detailed
```
