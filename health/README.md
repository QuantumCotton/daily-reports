# Health Journal / Health Tracking System

Track food, drinks, symptoms, and notes to identify patterns and triggers.

## Quick Start

### Log an Entry

```bash
# Food
~/.openclaw/bin/health_journal.py food "Oatmeal with berries and honey"

# Drink
~/.openclaw/bin/health_journal.py drink "Coffee with milk"

# Symptom (with severity 1-5)
~/.openclaw/bin/health_journal.py symptom "Headache" --severity 3

# Note
~/.openclaw/bin/health_journal.py note "Feeling tired after lunch"

# View today's entries
~/.openclaw/bin/health_journal.py today
```

### Run Weekly Analysis

```bash
# Analyze past 7 days
~/.openclaw/bin/health_analysis.py

# Analyze past 14 days
~/.openclaw/bin/health_analysis.py --days 14
```

## Features

- **Four Entry Types**: food, drink, symptom, note
- **Symptom Severity Scale**: 1-5 (1=mild, 5=severe)
- **Date-Organized Storage**: Entries organized by date in markdown format
- **Weekly Analysis**: Correlates foods with symptoms, identifies triggers
- **Daily Reminders**: 3x daily at 8am, 1pm, 7pm (requires cron setup)

## Setting Up Daily Reminders

Add these lines to your crontab (`crontab -e`):

```cron
# Health Journal Reminders
0 8 * * * echo "🍳 Breakfast time! Log your meal with: ~/.openclaw/bin/health_journal.py food \"<your breakfast>\""
0 13 * * * echo "🥗 Lunch time! How are you feeling? Log with: ~/.openclaw/bin/health_journal.py"
0 19 * * * echo "🍽️ Dinner time! Log your day's meals with: ~/.openclaw/bin/health_journal.py"
```

## Analysis Features

The weekly analysis provides:

1. **Entry Summary**: Count of entries by type
2. **Most Common Foods**: Foods you eat most frequently
3. **Symptom Frequency**: Symptoms you experience most
4. **Potential Triggers**: Foods linked to severe symptoms (severity 4-5)
5. **Food-Symptom Correlations**: Foods linked to symptoms by severity level

## File Locations

- **Journal Script**: `~/.openclaw/bin/health_journal.py`
- **Analysis Script**: `~/.openclaw/bin/health_analysis.py`
- **Journal File**: `~/.openclaw/workspace/health/journal.md`

## Telegram Integration

To use with Telegram, you'll need to set up a bot and topic. The scripts output can be piped to a Telegram message sender.

## Example Journal Entry

```markdown
## 2026-02-17

### Food
- [08:30] Oatmeal with berries and honey

### Drink
- [08:30] Coffee with milk
- [12:00] Water

### Symptom
- [14:30] Bloating (Severity: 3)

### Note
- [20:00] Feeling energetic today
```

## Tips for Best Results

1. **Be Consistent**: Log at regular times (use the reminders!)
2. **Be Specific**: Note ingredients and preparation methods
3. **Time Symptoms**: Log symptoms as soon as you notice them
4. **Review Weekly**: Run analysis to identify patterns
5. **Track Severities**: Use the 1-5 scale consistently

## Part of CRM System

This is system #10 of a 26-system CRM build.
