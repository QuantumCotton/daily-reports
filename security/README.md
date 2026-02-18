# Security Council - AI-Powered Security Review System

## Overview

The Security Council performs automated nightly security reviews of your entire codebase using AI-powered analysis from four perspectives:

1. **Offensive** - What could attackers exploit?
2. **Defensive** - Are protections adequate?
3. **Data Privacy** - Is sensitive data handled correctly?
4. **Operational Realism** - Are measures practical or theater?

## Files

- `~/.openclaw/bin/security_council.py` - Main script
- `~/.openclaw/workspace/config/security_checklist.json` - Configuration
- `~/.openclaw/workspace/security/reports/` - Generated reports
- `~/.openclaw/logs/security_council.log` - Execution logs

## Schedule

- **Runs nightly at 3:30am UTC** via cron
- Reports delivered to Telegram (alerts topic)
- Critical findings trigger immediate alerts

## Usage

### Run Full Review
```bash
python3 ~/.openclaw/bin/security_council.py
```

### Critical Only Mode
```bash
python3 ~/.openclaw/bin/security_council.py --critical-only
```

### Deep Dive on Finding
```bash
python3 ~/.openclaw/bin/security_council.py --deep-dive 5
```

## Configuration

Edit `~/.openclaw/workspace/config/security_checklist.json` to:

- Add/remove codebase paths
- Configure exclude patterns
- Adjust sensitive pattern detection
- Set severity thresholds
- Customize AI analysis prompts

## Requirements

- `OPENAI_API_KEY` environment variable (for AI analysis)
- `TELEGRAM_BOT_TOKEN` environment variable
- `TELEGRAM_CHAT_ID` environment variable

## Report Format

Reports include:

- Total findings count
- Critical findings (severity ≥ 9)
- Findings grouped by perspective
- File locations and line numbers
- Actionable recommendations
- Severity ratings (0-10 scale)

## Interactive Features

Ask for deeper analysis of any finding:
- Via Telegram: "deep dive #N"
- Via CLI: `--deep-dive N`

## Severity Thresholds

- **Critical (9-10)**: Immediate action required
- **High (7-8)**: Address within 24-48 hours
- **Medium (5-6)**: Review and plan fix
- **Low (0-4)**: Note for future review
