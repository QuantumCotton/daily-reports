# Project Dashboard - Quick Guide

> Created: 2026-02-16
> Purpose: Visual project management - Mind map, Kanban board, Timeline

---

## 📍 Access

**Dashboard:** http://107.172.20.181:8181/project_dashboard.html

**Data File:** `/home/chris/.openclaw/workspace/project_dashboard/project_data.json`

**Script:** `/home/chris/.openclaw/bin/project_dashboard.py`

---

## 🎯 Features

### 1. Kanban Board
- **3 Columns:** To Do → In Progress → Done
- **Priority Colors:** Critical (red), High (orange), Medium (yellow), Low (green)
- **Task Info:** Task name, assignee, due date

### 2. Timeline
- **3-Week Outlook:** Key dates and events
- **Phase Tags:** Phase 1 (orange), Phase 2 (yellow), Phase 3 (green), Phase 4 (blue)

### 3. Mind Map
- **4 Main Categories:**
  - Lead Generation
  - ESH Mail Platform
  - Contractor-in-a-Box
  - Advisor Team
- **Sub-items:** System components, strategies, roles

### 4. Advisor Team
- **4 Advisors:** Musk (CEO), Thiel (CMO), Carmack (CTO), Jensen (CRO)
- **Color-coded badges:** Each advisor has unique color

---

## 🛠️ How to Use

### View Dashboard
Open: http://107.172.20.181:8181/project_dashboard.html

### Add Task
```bash
python3 ~/.openclaw/bin/project_dashboard.py --add "column,task,assignee,priority,due"
```

Example:
```bash
python3 ~/.openclaw/bin/project_dashboard.py --add "to_do,Email warm-up setup,Glitch,critical,2026-02-18"
```

### Move Task
```bash
python3 ~/.openclaw/bin/project_dashboard.py --update "column,id,new_column"
```

Example:
```bash
python3 ~/.openclaw/bin/project_dashboard.py --update "to_do,1,in_progress"
```

### Regenerate Dashboard
```bash
python3 ~/.openclaw/bin/project_dashboard.py
```

---

## 🎨 Color System

### Priorities
- **Critical** (#ef4444): Must do this week
- **High** (#f97316): Must do this month
- **Medium** (#eab308): Nice to have
- **Low** (#22c55e): Low priority

### Advisors
- **Musk (CEO)** (#e74c3c): 10x thinking, autonomous operations
- **Thiel (CMO)** (#3498db): Contrarian strategy, monopoly positioning
- **Carmack (CTO)** (#2ecc71): Engineering efficiency, state machines
- **Jensen (CRO)** (#9b59b6): Scalability, hub-and-spoke model

### Phases
- **Phase 1** (#f97316): Week 1 (Feb 15-21) - Email warm-up + Josue's first deal
- **Phase 2** (#eab315): Weeks 2-4 (Feb 22-Mar 7) - Onboard 2 contractors + ESH Mail beta
- **Phase 3** (#22c55e): Weeks 5-8 (Mar 8-Apr 5) - First email outreach + scale to 10 contractors
- **Phase 4** (#3b82f6): Weeks 9-12 (Apr 6-May 15) - 4 contractors total

---

## 📊 Current Tasks

### To Do (7 tasks)
- Email warm-up setup (Glitch, critical, 2026-02-18)
- Josue's first deal (Glitch + Josue, critical, 2026-02-21)
- Quality scoring implementation (Glitch, high, 2026-02-18)
- Email templates (advisor hooks) (outreach-writer, high, 2026-02-18)
- Payment automation (Stripe) (coding-specialist, high, 2026-02-19)
- Build ESH Mail website (platform-builder, high, 2026-02-25)
- Create 75 domain names for warmup (Glitch, high, 2026-02-20)

### In Progress (2 tasks)
- Treasure Coast enrichment (344/500 complete) (lead-scout, high, 2026-02-21)
- Lead generation (400/day goal) (All scrapers, medium, Ongoing)

### Done (3 tasks)
- Advisor agents created (Glitch, high, 2026-02-16)
- Advisor strategies documented (All advisors, high, 2026-02-16)
- New scrapers created (Glitch, high, 2026-02-16)

---

## 🤖 Advisor Collaboration

**How advisors work on this:**
1. Chris asks me (Glitch) to spawn an advisor
2. Advisor reviews dashboard, adds tasks, updates status
3. I update dashboard with advisor's input
4. Chris, Glitch, and all advisors see changes

**Example:**
```
Chris: "Musk, review Phase 1 tasks, prioritize by 10x impact"
↓
I spawn Musk
↓
Musk: "Prioritize email warm-up (critical), Josue's first deal (critical), quality scoring (high)"
↓
I update dashboard priorities
↓
Chris sees updated priorities
```

---

## 🔄 Auto-Update

**Cron job (every 15 minutes):**
```bash
*/15 * * * * python3 /home/chris/.openclaw/bin/project_dashboard.py
```

**Result:** Dashboard auto-regenerates with latest data from project_data.json

---

## 📝 Data Structure

**project_data.json:**
```json
{
  "kanban": {
    "to_do": [...],
    "in_progress": [...],
    "done": [...]
  },
  "timeline": [...],
  "mindmap": {...},
  "advisors": {...},
  "updated_at": "2026-02-16T03:58:00"
}
```

---

**Last Updated:** 2026-02-16 03:58 UTC
**Next Review:** Every 15 minutes (automated)
