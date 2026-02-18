# Chat API - Test Results

## Server Status
- **Status**: ✅ Running
- **Port**: 8184
- **URL**: http://107.172.20.181:8184
- **Process ID**: 1335440 (main) + 1335443 (reloader)

## API Endpoints

### 1. List All Conversations
**Endpoint**: `GET /api/chat/conversations`

**Response**:
```json
{
  "conversations": [
    {
      "id": 1,
      "name": "General Chat",
      "icon": "💬",
      "created_at": "2026-02-16T07:19:52.844254",
      "message_count": 0
    },
    ...
  ]
}
```

**Status**: ✅ Tested and working

---

### 2. Get Conversation Messages
**Endpoint**: `GET /api/chat/conversation/{id}`

**Response**:
```json
{
  "conversation": {
    "id": 1,
    "name": "General Chat",
    "icon": "💬",
    "created_at": "2026-02-16T07:19:52.844254"
  },
  "messages": [
    {
      "id": 1,
      "sender": "user",
      "content": "Hello! This is a test message.",
      "timestamp": "2026-02-16T07:20:25.657890"
    }
  ]
}
```

**Status**: ✅ Tested and working

---

### 3. Send Message
**Endpoint**: `POST /api/chat/conversation/{id}/message`

**Request Body**:
```json
{
  "content": "Your message here"
}
```

**Response**:
```json
{
  "messages": [
    {
      "id": 1,
      "sender": "user",
      "content": "Your message here",
      "timestamp": "2026-02-16T07:20:25.657890"
    },
    {
      "id": 2,
      "sender": "glitch",
      "content": "Agent response...",
      "timestamp": "2026-02-16T07:21:25.730750"
    }
  ]
}
```

**Status**: ✅ Tested and working
**Note**: The agent call has a 60-second timeout. If the agent takes longer, a timeout message is stored.

---

### 4. Clear Conversation
**Endpoint**: `DELETE /api/chat/conversation/{id}`

**Response**:
```json
{
  "message": "Cleared 2 messages from conversation",
  "conversation_id": 1
}
```

**Status**: ✅ Tested and working

---

## Pre-populated Conversations

The system comes with 10 conversations ready to use:

1. 💬 General Chat
2. 💡 Project Ideas
3. 📚 Research & Learning
4. 💻 Code Help
5. ⚙️ System Admin
6. ✍️ Writing & Content
7. 🎯 Planning & Strategy
8. 🔧 Troubleshooting
9. 🧠 Creative Brainstorm
10. 📝 Quick Notes

---

## Database

- **Location**: `/home/chris/.openclaw/data/chat.db`
- **Tables**:
  - `conversations`: id, name, icon, created_at
  - `messages`: id, conversation_id, sender, content, timestamp

---

## Integration with Glitch

When a message is sent:
1. User message is stored in database
2. Last 10 messages are loaded for context
3. `openclaw agent --agent deep-researcher --message "..." --json` is called
4. Agent response is stored in database
5. Both messages are returned to client

Each conversation maintains its own context/memory.

---

## CORS Configuration

CORS is enabled for: `http://107.172.20.181:8181`

The dashboard at port 8181 can make requests to the chat API at port 8184.

---

## Server Management

**Start server**:
```bash
nohup python3 /home/chris/.openclaw/bin/chat_server.py > /tmp/chat_server.log 2>&1 &
```

**Check logs**:
```bash
tail -f /tmp/chat_server.log
```

**Stop server**:
```bash
pkill -f chat_server
```

**Check if running**:
```bash
ps aux | grep chat_server | grep -v grep
```
