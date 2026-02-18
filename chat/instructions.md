# Warzone Chat System

## How It Works

1. **Chris sends message** → Stored in `messages.json`
2. **Chat monitor** (cron every minute) → Detects new messages → Creates pending files
3. **GlitchGo** → Checks pending files → Responds via `chat_respond.py`

## GlitchGo's Chat Commands

When you're running and want to check for new messages:

```bash
# Check for pending messages
ls -lt ~/.openclaw/workspace/chat/pending/

# View a specific pending message
cat ~/.openclaw/workspace/chat/pending/<filename>.json

# Respond to a message
python3 ~/.openclaw/bin/chat_respond.py <group_id> "Your message here"

# View all messages in a group
cat ~/.openclaw/workspace/chat/messages.json | python3 -m json.tool | grep -A 10 "<group_id>"
```

## Groups

- **warzone** — War Room (lead-scout, outreach-writer, strategy-planner, chris)
- **lead-gen** — Lead Generation (scraper army)
- **treasure-coast** — Regional ops
- **founders** — Carmack, Musk, Thiel, Jensen
- **quality** — Quality Control

## Future Integration

To make this fully real-time:
1. Hook chat API into OpenClaw's session system
2. Use `sessions_send` to forward messages to agents
3. Create dedicated "chat router" agent that monitors and dispatches
4. Add webhook support for instant notifications

