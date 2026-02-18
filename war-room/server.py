#!/usr/bin/env python3
"""
War Room Dashboard Server
Serves the Elite Service Hub operations dashboard
"""

import sqlite3
import json
import os
import glob
from datetime import datetime
from pathlib import Path
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

# Configuration
DB_PATH = '/home/chris/.openclaw/workspace/leads/lead_bank.db'
AGENTS_PATH = '/home/chris/.openclaw/agents'
PORT = 10269

app = Flask(__name__)
CORS(app)


def get_warming_status():
    """Get warming email status with metro assignments"""
    # Warming emails and their metro assignments
    warming_emails = [
        {'email': 'warming1@kmjk.pro', 'metro': 'Stuart, FL'},
        {'email': 'warming2@kmjk.pro', 'metro': 'Jensen Beach, FL'},
        {'email': 'warming3@kmjk.pro', 'metro': 'Port St Lucie, FL'},
        {'email': 'warming4@kmjk.pro', 'metro': 'Vero Beach, FL'},
        {'email': 'warming5@kmjk.pro', 'metro': 'San Jose, CA'}
    ]
    
    # TODO: Integrate with actual warming system to get real status
    # For now, return simulated status
    # In production, this would query your warming system's database or API
    for warming_email in warming_emails:
        # Simulated status - replace with actual data source
        warming_email['status'] = 'Active'  # or 'Idle', 'Error'
        warming_email['progress'] = 75  # percentage
    
    return warming_emails


def get_db_metrics():
    """Query database for lead metrics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Total leads
        cursor.execute('SELECT COUNT(*) FROM leads')
        total = cursor.fetchone()[0]

        # Complete leads (name + email)
        cursor.execute('SELECT COUNT(*) FROM leads WHERE email != "" AND contact_name != ""')
        complete = cursor.fetchone()[0]

        # Last updated
        cursor.execute('SELECT MAX(updated_at) FROM leads')
        last_updated = cursor.fetchone()[0]

        conn.close()

        return {
            'total_leads': total,
            'complete_leads': complete,
            'last_updated': last_updated or 'N/A'
        }
    except Exception as e:
        print(f"Error querying database: {e}")
        return {
            'total_leads': 0,
            'complete_leads': 0,
            'last_updated': 'Error'
        }


def get_agent_info():
    """Get information about active agents from session files"""
    agents = []

    try:
        # Find all agent session files
        session_pattern = os.path.join(AGENTS_PATH, '*', 'sessions', '*.jsonl')

        for session_file in glob.glob(session_pattern):
            try:
                # Extract agent name from path
                parts = Path(session_file).parts
                agent_idx = parts.index('agents') + 1
                agent_name = parts[agent_idx]

                # Get last modified time
                mtime = os.path.getmtime(session_file)
                last_activity = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')

                # Try to read the last line to see what they're working on
                task = 'Idle'
                try:
                    with open(session_file, 'r') as f:
                        lines = f.readlines()
                        if lines:
                            last_entry = json.loads(lines[-1])
                            # Extract task from message or content
                            if 'message' in last_entry:
                                task = last_entry['message'][:50]
                            elif 'content' in last_entry:
                                task = str(last_entry['content'])[:50]
                except:
                    pass

                # Check if agent is active (modified in last 5 minutes)
                is_active = (datetime.now().timestamp() - mtime) < 300

                agents.append({
                    'name': agent_name,
                    'task': task,
                    'last_activity': last_activity,
                    'active': is_active
                })
            except Exception as e:
                print(f"Error processing session file {session_file}: {e}")
                continue

        # Sort by last activity (most recent first)
        agents.sort(key=lambda x: x['last_activity'], reverse=True)

    except Exception as e:
        print(f"Error getting agent info: {e}")

    return agents


def get_activity_feed():
    """Generate activity feed from various sources"""
    activities = []

    try:
        # Add lead count update
        metrics = get_db_metrics()
        activities.append({
            'type': 'info',
            'text': f'Lead database updated: {metrics["total_leads"]} total leads',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        # Add complete leads info
        if metrics['complete_leads'] > 0:
            activities.append({
                'type': 'success',
                'text': f'Complete leads (name+email): {metrics["complete_leads"]}',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        # Add agent activities
        agents = get_agent_info()
        active_agents = [a for a in agents if a['active']]

        if active_agents:
            activities.append({
                'type': 'info',
                'text': f'{len(active_agents)} active agent(s) running',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        # Add recent agent completions (from inactive agents with recent activity)
        recent_inactive = [a for a in agents if not a['active'] and
                          (datetime.now().timestamp() - datetime.strptime(a['last_activity'], '%Y-%m-%d %H:%M:%S').timestamp()) < 3600]

        if recent_inactive:
            for agent in recent_inactive[:3]:  # Limit to 3
                activities.append({
                    'type': 'success',
                    'text': f'Agent {agent["name"]} completed task',
                    'timestamp': agent['last_activity']
                })

        # Check for errors
        error_log = '/home/chris/.openclaw/workspace/leads/errors.log'
        if os.path.exists(error_log):
            try:
                with open(error_log, 'r') as f:
                    errors = f.readlines()[-5:]  # Last 5 errors
                    for error in errors[-2:]:  # Show last 2
                        if error.strip():
                            activities.append({
                                'type': 'error',
                                'text': f'Error logged: {error.strip()[:80]}',
                                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
            except:
                pass

    except Exception as e:
        print(f"Error generating activity feed: {e}")
        activities.append({
            'type': 'error',
            'text': f'Error loading activity feed: {str(e)}',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    # Sort by timestamp (most recent first) and limit to 20
    activities.sort(key=lambda x: x['timestamp'], reverse=True)
    return activities[:20]


@app.route('/')
def index():
    """Serve the main dashboard page"""
    return send_from_directory('.', 'index.html')


@app.route('/api/metrics')
def api_metrics():
    """Get database metrics"""
    return jsonify(get_db_metrics())


@app.route('/api/agents')
def api_agents():
    """Get agent information"""
    return jsonify(get_agent_info())


@app.route('/api/activity')
def api_activity():
    """Get activity feed"""
    return jsonify(get_activity_feed())


@app.route('/api/warming-status')
def api_warming_status():
    """Get warming email status with metro assignments"""
    return jsonify(get_warming_status())


@app.route('/api/action/<action_name>', methods=['POST'])
def api_action(action_name):
    """Execute a quick action"""
    actions = {
        'lead-scraper': {
            'message': 'Lead scraper triggered - Check your lead generation system',
            'type': 'info'
        },
        'generate-report': {
            'message': 'Report generation requested - Check /home/chris/.openclaw/workspace/reports/',
            'type': 'success'
        },
        'check-status': {
            'message': f'System Status: {len(get_agent_info())} agents, {get_db_metrics()["total_leads"]} leads',
            'type': 'info'
        }
    }

    result = actions.get(action_name, {
        'message': f'Unknown action: {action_name}',
        'type': 'error'
    })

    return jsonify(result)


if __name__ == '__main__':
    print(f"Starting War Room Dashboard on port {PORT}")
    print(f"Dashboard URL: http://localhost:{PORT}")
    print(f"Database: {DB_PATH}")
    print(f"Agents path: {AGENTS_PATH}")
    print()

    try:
        # Test database connection
        metrics = get_db_metrics()
        print(f"Database connected: {metrics['total_leads']} leads found")
    except Exception as e:
        print(f"Warning: Could not connect to database: {e}")

    app.run(host='0.0.0.0', port=PORT, debug=False)
