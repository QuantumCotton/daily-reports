# Video Idea Pipeline - Installation Guide

## Overview
Video Idea Pipeline (#8 from 26-system CRM build) - Automatically processes Slack mentions, researches angles, checks duplicates, and creates Asana cards for video production.

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Copy Files to Their Locations

```bash
# Create directories
mkdir -p ~/.openclaw/bin
mkdir -p ~/.openclaw/workspace/config

# Copy main script
cp video_pipeline.py ~/.openclaw/bin/
chmod +x ~/.openclaw/bin/video_pipeline.py

# Copy config files
cp slack.json ~/.openclaw/workspace/config/
cp asana.json ~/.openclaw/workspace/config/
```

### 3. Configure Slack

Edit `~/.openclaw/workspace/config/slack.json`:

```json
{
  "bot_token": "xoxb-YOUR_BOT_TOKEN",
  "signing_secret": "YOUR_SIGNING_SECRET",
  "default_assignee": "ASANA_USER_GID_OR_NULL",
  "twitter": {
    "bearer_token": "YOUR_TWITTER_BEARER_TOKEN"
  }
}
```

**To get Slack credentials:**
1. Go to https://api.slack.com/apps
2. Create a new app (Bot)
3. Enable Event Subscriptions for `app_mention`
4. Add scopes: `channels:history`, `chat:write`, `groups:history`
5. Install to workspace and copy tokens

### 4. Configure Asana

Edit `~/.openclaw/workspace/config/asana.json`:

```json
{
  "access_token": "YOUR_ASANA_PAT",
  "workspace_gid": "WORKSPACE_GID",
  "project_gid": "PROJECT_GID"
}
```

**To get Asana credentials:**
1. Go to https://app.asana.com/0/my-apps
2. Create Personal Access Token
3. Find workspace GID in URL: `app.asana.com/0/{WORKSPACE_GID}/...`
4. Find project GID in URL: `app.asana.com/0/{WORKSPACE_GID}/{PROJECT_GID}/...`

### 5. Initialize Database

```bash
~/.openclaw/bin/video_pipeline.py init
```

This creates `~/.openclaw/workspace/video_pitches.db` with all required tables.

## Usage

### Process a Slack Mention (Manual)

```bash
~/.openclaw/bin/video_pipeline.py process \
  --channel C1234567890 \
  --message-ts "1234567890.123456"
```

### Record Feedback on a Pitch

```bash
~/.openclaw/bin/video_pipeline.py feedback \
  --pitch-id 1 \
  --type accepted \
  --notes "Great idea, let's produce it"
```

### List All Pitches

```bash
~/.openclaw/bin/video_pipeline.py list
```

### List Pitches by Status

```bash
~/.openclaw/bin/video_pipeline.py list --status pitched
```

## Database Schema

### pitches
- `id`: Primary key
- `idea`: The video idea text
- `slack_channel`: Where the mention occurred
- `slack_thread_ts`: Thread timestamp
- `slack_message_ts`: Original message timestamp
- `asana_task_gid`: Asana task ID
- `asana_task_url`: Link to Asana task
- `status`: pitched | accepted | rejected | produced | duplicate
- `similarity_score`: Duplicate detection score
- `created_at`, `updated_at`: Timestamps

### pitch_research
- `pitch_id`: FK to pitches
- `research_type`: twitter | knowledge_base | slack_thread
- `content`: Research data
- `source`: Source identifier
- `url`: Source URL (if applicable)

### pitch_angles
- `pitch_id`: FK to pitches
- `angle`: Potential video angle
- `source`: Where angle came from

### pitch_feedback
- `pitch_id`: FK to pitches
- `feedback_type`: accepted | rejected | produced
- `notes`: Optional feedback notes

### pitch_embeddings
- `pitch_id`: FK to pitches
- `embedding`: Binary semantic embedding (for similarity search)

## Integration with Slack Event Handler

To automatically trigger on mentions, integrate with your Slack event handler:

```python
# In your Slack event handler
@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    if data["type"] == "event_callback":
        event = data["event"]
        if event["type"] == "app_mention":
            if "@assistant potential video idea" in event["text"]:
                # Trigger the pipeline
                subprocess.run([
                    "~/.openclaw/bin/video_pipeline.py",
                    "process",
                    "--channel", event["channel"],
                    "--message-ts", event["ts"],
                    "--thread-ts", event.get("thread_ts", event["ts"])
                ])

    return {"status": "ok"}
```

## Features Implemented

✅ Slack mention trigger detection
✅ Full thread context reading
✅ X/Twitter research on angles
✅ Knowledge base querying (placeholder - connect your KB)
✅ Structured Asana card creation with:
  - Idea
  - Research data
  - Sources
  - Angles
✅ Slack completion message with Asana link
✅ Semantic similarity search (40% threshold = skip)
✅ Pitch tracking with statuses: pitched, accepted, rejected, produced, duplicate
✅ Feedback learning system

## Notes

- Semantic similarity uses sentence-transformers (all-MiniLM-L6-v2)
- Model downloads on first use (~100MB)
- Twitter API v2 is used for research
- Knowledge base integration is a stub - connect your actual KB
- All logs go to Python logging (INFO level by default)

## Troubleshooting

**"Config file missing" error:**
- Ensure config files are in `~/.openclaw/workspace/config/`

**"sentence-transformers not available" warning:**
- Install with: `pip install sentence-transformers torch`
- Pipeline still works, just without duplicate detection

**Slack API errors:**
- Check bot has required scopes
- Verify bot is invited to the channel
- Check bot token is correct

**Asana API errors:**
- Verify PAT has correct permissions
- Check workspace and project GIDs are correct
- Ensure bot is a member of the workspace

## Part of 26-System CRM Build
System #8 of 26
