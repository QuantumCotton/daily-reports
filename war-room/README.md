# War Room Dashboard - Elite Service Hub

A beautiful, dark glassmorphism operations dashboard for monitoring Elite Service Hub operations.

## Features

### 🔥 Warming Roadmap
- **warming1@kmjk.pro** → Stuart, FL
- **warming2@kmjk.pro** → Jensen Beach, FL
- **warming3@kmjk.pro** → Port St Lucie, FL
- **warming4@kmjk.pro** → Vero Beach, FL
- **warming5@kmjk.pro** → San Jose, CA

Each warming email shows:
- Assigned metro area
- Current status (Active, Idle, or Error)
- Progress percentage with visual progress bar
- Color-coded status indicators

### 📋 Project Tracker
- **ESH Mail** - Status: Building (65%)
- **Lead Generation** - Status: Running (20,611 leads)
- **Epoxy Formulation** - Status: Research Complete (100%)

### 📊 Metrics Dashboard
- Total leads count from SQLite database
- Complete leads (name + email)
- Last updated timestamp

### 🤖 Agent Monitor
- Shows active agents from `~/.openclaw/agents/*/sessions/*.jsonl`
- Last activity timestamp
- Current task being worked on

### 📡 Recent Activity Feed
- Last 20 system events
- Lead count updates
- Agent completions
- Errors (if any)

### ⚡ Quick Actions
- **Run Lead Scraper** - Trigger lead generation
- **Generate Report** - Generate system reports
- **Check System Status** - Quick status check

## Tech Stack

- **HTML + CSS + JavaScript** - Frontend
- **Python Flask** - Backend server
- **SQLite** - Database queries
- **Dark Glassmorphism** - UI theme (Chris's style)

## Installation

### Prerequisites

```bash
# Install Flask and CORS
pip install flask flask-cors
```

### Starting the Server

```bash
# Navigate to the war-room directory
cd ~/.openclaw/workspace/war-room

# Start the server
python3 server.py
```

Or from anywhere:

```bash
python3 ~/.openclaw/workspace/war-room/server.py
```

### Accessing the Dashboard

Open your browser and navigate to:

```
http://localhost:10269
```

Or from another machine on your network:

```
http://<your-ip>:10269
```

## API Endpoints

### GET `/`
- Returns the main dashboard HTML page

### GET `/api/metrics`
- Returns database metrics
```json
{
  "total_leads": 20611,
  "complete_leads": 1485,
  "last_updated": "2026-02-15 23:00:37"
}
```

### GET `/api/agents`
- Returns list of agents with their status
```json
[
  {
    "name": "main",
    "task": "Working on task...",
    "last_activity": "2026-02-15 23:00:00",
    "active": true
  }
]
```

### GET `/api/activity`
- Returns recent activity feed (last 20 events)
```json
[
  {
    "type": "info",
    "text": "Lead database updated: 20611 total leads",
    "timestamp": "2026-02-15 23:00:00"
  }
]
```

### GET `/api/warming-status`
- Returns warming email status with metro assignments and progress
```json
[
  {
    "email": "warming1@kmjk.pro",
    "metro": "Stuart, FL",
    "status": "Active",
    "progress": 75
  },
  {
    "email": "warming2@kmjk.pro",
    "metro": "Jensen Beach, FL",
    "status": "Idle",
    "progress": 45
  },
  {
    "email": "warming3@kmjk.pro",
    "metro": "Port St Lucie, FL",
    "status": "Active",
    "progress": 90
  },
  {
    "email": "warming4@kmjk.pro",
    "metro": "Vero Beach, FL",
    "status": "Error",
    "progress": 30
  },
  {
    "email": "warming5@kmjk.pro",
    "metro": "San Jose, CA",
    "status": "Active",
    "progress": 60
  }
]
```

**Note:** The warming status endpoint currently returns simulated data. To integrate with your actual warming system, update the `get_warming_status()` function in `server.py` to query your warming system's database or API.

### POST `/api/action/<action_name>`
- Execute quick actions
- Actions: `lead-scraper`, `generate-report`, `check-status`
```json
{
  "message": "Action executed successfully",
  "type": "success"
}
```

## Auto-Refresh

The dashboard automatically refreshes every 30 seconds to keep data current.

## Configuration

Edit `server.py` to customize:

```python
# Database path
DB_PATH = '/home/chris/.openclaw/workspace/leads/lead_bank.db'

# Agents path
AGENTS_PATH = '/home/chris/.openclaw/agents'

# Port
PORT = 10269
```

## Integrating Real Warming Data

To connect the Warming Roadmap to your actual warming system:

1. Update the `get_warming_status()` function in `server.py`
2. Query your warming system's database or API
3. Return real status and progress data for each warming email

Example integration:

```python
def get_warming_status():
    """Get warming email status from your warming system"""
    warming_emails = [...]  # Keep the email/metro mapping
    
    # Query your warming system
    for warming_email in warming_emails:
        # Get real status from your database/API
        status_data = query_warming_system(warming_email['email'])
        warming_email['status'] = status_data['status']
        warming_email['progress'] = status_data['progress']
    
    return warming_emails
```

## Troubleshooting

### Dashboard won't load
- Check that the server is running: `ps aux | grep server.py`
- Verify port 10269 is not in use: `lsof -i :10269`

### Data not showing
- Check database path in `server.py`
- Verify SQLite database exists and is accessible
- Check file permissions on `~/.openclaw/workspace/leads/lead_bank.db`

### Agents not showing
- Verify agents path is correct
- Check that session files exist: `find ~/.openclaw/agents -name "*.jsonl"`

### Warming Roadmap showing simulated data
- The warming status endpoint returns placeholder data by default
- See "Integrating Real Warming Data" section above to connect to your system

## Styling

The dashboard uses a dark glassmorphism theme with:
- Semi-transparent panels with blur effects
- Gradient accents (purple/blue)
- Smooth animations and transitions
- Responsive design for all screen sizes
- Color-coded status indicators (green for Active, yellow for Idle, red for Error)

## Running in Production

For production use:

```bash
# Use a production WSGI server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:10269 server:app
```

Or use systemd for automatic startup (create a service file in `/etc/systemd/system/war-room.service`).

## Credits

Built for Elite Service Hub operations monitoring.
