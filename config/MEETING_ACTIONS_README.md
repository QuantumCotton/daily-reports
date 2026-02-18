# Meeting Actions Pipeline - Setup Guide

## Location
Installed to: `~/.openclaw/bin/meeting_actions.py`

## Configuration Files Required

Create these config files in `~/.openclaw/workspace/config/`:

### 1. `todoist.json`
```json
{
  "api_token": "your_todoist_api_token",
  "project_id": "optional_project_id_for_tasks"
}
```

Get your Todoist API token from: https://todoist.com/settings/integrations

### 2. `fathom.json`
```json
{
  "api_key": "your_fathom_api_key"
}
```

Get your Fathom API key from your Fathom account settings.

### 3. `telegram.json`
```json
{
  "bot_token": "your_telegram_bot_token",
  "chat_id": "your_telegram_chat_id"
}
```

- Create a bot via @BotFather on Telegram
- Get your chat ID by messaging @userinfobot

### 4. `crm.json`
```json
{
  "my_email": "your@email.com",
  "internal_team": {
    "domains": ["yourcompany.com", "internal.co"],
    "emails": ["colleague1@other.com", "colleague2@other.com"]
  },
  "contacts": {
    "contact_id_1": {
      "name": "John Doe",
      "email": "john@example.com",
      "alternative_emails": ["john.doe@company.com"]
    }
  },
  "relationships_file": "~/.openclaw/workspace/data/crm_relationships.json"
}
```

## Usage

### Run continuously (daemon mode)
```bash
~/.openclaw/bin/meeting_actions.py
```

### Run once (for testing)
```bash
~/.openclaw/bin/meeting_actions.py --once
```

### Check status
```bash
~/.openclaw/bin/meeting_actions.py --status
```

### List pending items
```bash
~/.openclaw/bin/meeting_actions.py --list-pending
```

### List "waiting on" items
```bash
~/.openclaw/bin/meeting_actions.py --list-waiting
```

### Manually approve/reject (via CLI)
```bash
~/.openclaw/bin/meeting_actions.py --approve <action_item_id>
~/.openclaw/bin/meeting_actions.py --reject <action_item_id>
```

## How It Works

1. **Polling**: Every 5 minutes during business hours (9am-6pm UTC, Mon-Fri), polls Fathom for recent meetings

2. **Meeting Buffer**: Only processes meetings that ended within the last 15 minutes (configurable)

3. **Action Item Extraction**: Scans transcripts for action items using pattern matching:
   - "I will..." / "I need to..."
   - "You will..." / "You need to..."
   - "assign X to Y"
   - "action item: ..." / "todo: ..."

4. **Ownership Detection**: Determines if an action is "mine" or "theirs" based on context

5. **Approval Queue**: Your actions go to Telegram for approve/reject before creating Todoist tasks

6. **Waiting On Tracking**: Others' actions are tracked as "waiting on" (excluding internal team)

7. **CRM Integration**:
   - Matches attendees to CRM contacts by email
   - Updates relationship summaries with meeting context
   - Tracks meeting history per contact

8. **Completion Checks**: Runs 3x daily (8am, 12pm, 4pm UTC) to sync completed Todoist tasks

9. **Auto-Archive**: Items older than 14 days are automatically archived

## State File

State is persisted to: `~/.openclaw/workspace/state/meeting_actions_state.json`

Contains:
- Processed meetings
- All action items with status
- Approval queue
- "Waiting on" items
- Last poll/completion check timestamps

## Customization

Edit these constants in `meeting_actions.py`:

```python
BUSINESS_HOURS_START = 9  # Hour in UTC
BUSINESS_HOURS_END = 18   # Hour in UTC
BUSINESS_DAYS = [0, 1, 2, 3, 4]  # Monday=0, Friday=4

MEETING_END_BUFFER = 15  # Minutes to wait after meeting ends
POLL_INTERVAL = 300  # Seconds between polls (5 minutes)
ARCHIVE_THRESHOLD = 14  # Days before archiving

COMPLETION_CHECK_TIMES = [8, 12, 16]  # Hours in UTC
```

## Dependencies

Install required Python packages:
```bash
pip install httpx pydantic
```

## Running as a Service (Optional)

To run as a background service, use systemd, supervisord, or cron:

### Using systemd
Create `/etc/systemd/system/meeting-actions.service`:
```ini
[Unit]
Description=Meeting Actions Pipeline
After=network.target

[Service]
Type=simple
User=your_username
ExecStart=/home/your_username/.openclaw/bin/meeting_actions.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable meeting-actions
sudo systemctl start meeting-actions
```

## Telegram Integration

The bot sends approval requests with inline buttons. Click "Approve" to create a Todoist task or "Reject" to skip.

You can also handle approvals via CLI using the `--approve` and `--reject` flags if needed.

## Final Piece

This completes the 26-system CRM build.
