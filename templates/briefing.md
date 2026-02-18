# Daily Briefing Template

## Overview
This is the structure and template for the automated daily briefing system.

## Daily Briefing Structure

### Header
```
🌅 **Daily Briefing - {Day of Week}, Month Day, Year**

*Generated at HH:MM UTC*

──────────────────────────────────
```

### Section 1: Urgent Action Items
```
🚨 **Urgent Action Items**

• [CRM/Asana] Task description - Due: MMM DD (Contact Name)
• [Asana] Task description - Due: MMM DD

OR

No urgent items. Good job! ✨
```

### Section 2: Today's Calendar
```
📅 **Today's Calendar**

**Meeting Title**
  • Time: HH:MM AM/PM
  • Attendees:
    - John Doe (Company Name)
      Last: Discussed pricing strategy, next steps...
    - Jane Smith (Another Company)

**Another Meeting**
  • Time: HH:MM AM/PM
  • Attendees:
    - Bob Wilson (Tech Corp)

OR

No events scheduled for today.
```

### Section 3: Pending Action Items
```
✅ **Pending Action Items**

• [Asana] Task description - Due: MMM DD
• [CRM] Follow up with Contact Name - Due: MMM DD (Company)
• [Asana] Task description - Due: MMM DD

OR

No pending action items.
```

### Section 4: CRM Follow-ups
```
👥 **CRM Follow-ups**

🔴 **John Smith** (ABC Corp)
  • Need to discuss contract renewal
  • Due: Feb 20

🟡 **Jane Doe** (XYZ Inc)
  • Follow up on proposal feedback
  • Due: Feb 22

OR

No pending CRM follow-ups.
```

### Section 5: Content Performance
```
📊 **Yesterday's Content Performance**

**YouTube:**
  • Views: X,XXX
  • Videos posted: X

**Instagram:**
  • Likes: XXX
  • Posts: X

**X (Twitter):**
  • Impressions: XX,XXX
  • Engagement rate: X.X%
```

### Section 6: Email Cross-Reference
```
📧 **Email Cross-Reference**

No recent emails found for today's meeting attendees.

OR

**For Meeting with John Doe (ABC Corp):**
  • Last email: 2 days ago - Contract draft
  • Thread contains: 3 messages
```

## Integration Points

### Data Sources
1. **CRM Database** (`~/.openclaw/workspace/crm/contacts.db`)
   - Contacts table: Who people are
   - Interactions table: Last discussion history
   - Follow-ups table: Pending CRM follow-ups

2. **Asana Database** (`~/.openclaw/workspace/analytics/asana.db`)
   - Tasks table: All action items
   - Filter: incomplete, due soon

3. **Google Calendar API**
   - Today's events
   - Attendee emails (for CRM cross-reference)

4. **Content APIs** (to be integrated)
   - YouTube API: Views, engagement
   - Instagram Basic Display API: Likes, comments
   - X API: Impressions, engagement rate

### Output
- **Telegram**: `daily-brief` topic
- **Topic ID**: `daily-brief`
- **Timing**: 7:00 AM daily (configurable timezone)

## Cron Job Setup

Add to crontab:
```
0 7 * * * /usr/bin/python3 ~/.openclaw/bin/daily_briefing.py send >> ~/.openclaw/cron/logs/daily_briefing.log 2>&1
```

## Usage

```bash
# Preview the briefing without sending
~/.openclaw/bin/daily_briefing.py preview

# Send to Telegram
~/.openclaw/bin/daily_briefing.py send

# Generate and send immediately (bypass time checks)
~/.openclaw/bin/daily_briefing.py now
```

## State Tracking

The system tracks:
- Last briefing date and time
- Number of events covered
- Number of action items included

State file: `~/.openclaw/workspace/config/daily_briefing_state.json`

## Customization

### Adding New Data Sources

1. Create a `load_<source>()` method
2. Add to `main()` loading sequence
3. Create a `generate_<source>_section()` method
4. Add to `generate_briefing()` in desired position

### Modifying Priority Order

The current priority order is:
1. Urgent action items (red flags)
2. Calendar (today's commitments)
3. All action items (task management)
4. CRM follow-ups (relationship management)
5. Content performance (business metrics)
6. Email cross-reference (context)

## Notes

- The system gracefully handles missing data sources
- Email cross-reference integration with Google Gmail API pending
- Content performance APIs need integration
- Calendar integration with Google Calendar API pending
