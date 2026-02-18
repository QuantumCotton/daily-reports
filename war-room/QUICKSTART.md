# Quick Start Guide - War Room Dashboard

## 🚀 Start the Dashboard

```bash
cd ~/.openclaw/workspace/war-room
./start.sh
```

Or directly:

```bash
cd ~/.openclaw/workspace/war-room
python3 server.py
```

## 📱 Access the Dashboard

Open your browser: **http://localhost:10269**

From another device: **http://107.172.20.181:10269**

## 🛑 Stop the Dashboard

Press `Ctrl+C` in the terminal, or:

```bash
pkill -f "python3 server.py"
```

## ✅ What You'll See

### Project Tracker
- ESH Mail (Building - 65%)
- Lead Generation (Running - 20,611 leads)
- Epoxy Formulation (Complete - 100%)

### Metrics Dashboard
- Total Leads: 20,611
- Complete Leads (name+email): 1,485
- Last Updated: 2026-02-15 23:00:37

### Agent Monitor
- Shows all agents from ~/.openclaw/agents/
- Active agents have green dot
- Last activity timestamps

### Activity Feed
- Last 20 system events
- Color-coded: green (success), blue (info), red (error)

### Quick Actions
- Run Lead Scraper
- Generate Report
- Check System Status

## 🔧 Auto-Refresh

Dashboard refreshes every 30 seconds automatically.

## 📊 API Testing

Test endpoints directly:

```bash
# Metrics
curl http://localhost:10269/api/metrics

# Agents
curl http://localhost:10269/api/agents

# Activity
curl http://localhost:10269/api/activity

# Trigger action
curl -X POST http://localhost:10269/api/action/check-status
```

## 🎨 Features

- Dark glassmorphism theme
- Responsive design (mobile-friendly)
- Real-time data from SQLite database
- Live agent monitoring
- System event tracking
- Quick action buttons

## 📝 Configuration

Edit `server.py` to customize:

```python
DB_PATH = '/home/chris/.openclaw/workspace/leads/lead_bank.db'  # Database
AGENTS_PATH = '/home/chris/.openclaw/agents'                       # Agents
PORT = 10269                                                        # Port
```

## 🐛 Troubleshooting

**Port already in use?**
```bash
lsof -i :10269
kill <PID>
```

**Dependencies missing?**
```bash
pip3 install flask flask-cors --break-system-packages
```

**Database not found?**
Check that `lead_bank.db` exists in `/home/chris/.openclaw/workspace/leads/`

---

Built for Elite Service Hub operations monitoring.
