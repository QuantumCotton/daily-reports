# Personal CRM System

A comprehensive contact management system with vector embeddings, natural language search, relationship health scoring, and automated follow-up reminders.

## Features

- **Auto-discovery**: Scan Gmail and Google Calendar to find contacts
- **Vector embeddings**: Natural language search (e.g., "who do I know at NVIDIA?")
- **Noise filtering**: Automatically filters marketing emails and newsletters
- **Contact profiles**: Company, role, notes, interaction history
- **Relationship health scores**: Track relationship strength over time
- **Follow-up reminders**: Create, snooze, and track follow-ups
- **Duplicate detection**: Smart merging of duplicate contacts
- **Box integration**: Link documents to contacts

## Installation

The system is installed at `~/.openclaw/bin/personal_crm.py`.

## Quick Start

### 1. Initialize

```bash
~/.openclaw/bin/personal_crm.py init
```

This creates:
- Database: `~/.openclaw/workspace/crm/contacts.db`
- OAuth config: `~/.openclaw/workspace/config/google_oauth.json`
- Box config: `~/.openclaw/workspace/config/box_config.json`

### 2. Configure Google OAuth (Optional)

To enable Gmail and Calendar scanning, edit `~/.openclaw/workspace/config/google_oauth.json` with your Google Cloud credentials:

```json
{
  "client_id": "YOUR_GOOGLE_CLIENT_ID",
  "client_secret": "YOUR_GOOGLE_CLIENT_SECRET",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

You'll need to create a Google Cloud project and enable the Gmail and Calendar APIs.

### 3. Basic Usage

#### Import a contact
```bash
~/.openclaw/bin/personal_crm.py import john@example.com --name "John Doe"
```

#### Search contacts (natural language)
```bash
~/.openclaw/bin/personal_crm.py search "who do I know at NVIDIA"
~/.openclaw/bin/personal_crm.py search "engineer in San Francisco"
```

#### View a contact profile
```bash
~/.openclaw/bin/personal_crm.py profile john@example.com
```

#### List all contacts
```bash
~/.openclaw/bin/personal_crm.py list
```

## Commands

### Search
```bash
~/.openclaw/bin/personal_crm.py search <query> [--limit N]
```
Natural language search for contacts. Uses vector embeddings + text matching.

### Profile
```bash
~/.openclaw/bin/personal_crm.py profile <email>
```
View full contact profile including interactions, documents, and health score.

### Import
```bash
~/.openclaw/bin/personal_crm.py import <email> [--name <name>]
```
Manually import a contact. Automatically filters noise senders.

### Sync
```bash
~/.openclaw/bin/personal_crm.py sync [--days N]
```
Sync contacts from Gmail and Google Calendar (requires OAuth setup).

### Follow-up Management

#### Create a follow-up
```bash
~/.openclaw/bin/personal_crm.py followup create <email> --days N --notes "Reminder text"
```

#### List due follow-ups
```bash
~/.openclaw/bin/personal_crm.py followup list [--days N]
```

#### Complete a follow-up
```bash
~/.openclaw/bin/personal_crm.py followup complete <follow-up-id>
```

#### Snooze a follow-up
```bash
~/.openclaw/bin/personal_crm.py followup snooze <follow-up-id> [--days N]
```

### Duplicate Detection
```bash
~/.openclaw/bin/personal_crm.py duplicates [--threshold N]
```
Find potential duplicate contacts based on email, name, and vector similarity.

### Merge Contacts
```bash
~/.openclaw/bin/personal_crm.py merge <keep-email> <merge-email-1> <merge-email-2> ...
```
Merge multiple contacts into one. All interactions and follow-ups are transferred.

### Stale Contacts
```bash
~/.openclaw/bin/personal_crm.py stale [--days N]
```
List contacts with no recent interactions (default: 90 days).

### Link Document
```bash
~/.openclaw/bin/personal_crm.py link <email> <file-id> <file-name> <file-url>
```
Link a Box document to a contact.

## Relationship Health Scores

Health scores (0-100) are calculated based on:

- **Recency (50%)**: How recently you've interacted with the contact
- **Frequency (30%)**: Number of interactions in the last 90 days
- **Consistency (20%)**: Evenness of interaction distribution over time

Score interpretation:
- 80-100: Strong, active relationship
- 50-79: Moderate relationship
- 0-49: Weak or stale relationship

## Noise Filtering

The system automatically filters out:
- Generic addresses (noreply@, info@, support@, etc.)
- Newsletter patterns (news@, updates@, marketing@)
- Common marketing senders
- Known bulk email domains

## Database Schema

### contacts
- id, email, name, company, role
- created_at, updated_at
- embedding (vector for search)
- notes, how_i_know_them

### interactions
- id, contact_id, interaction_type (email/calendar/manual)
- timestamp, summary, metadata

### follow_ups
- id, contact_id, due_date, notes
- status (pending/snoozed/done)
- created_at, completed_at

### document_links
- id, contact_id, box_file_id
- box_file_name, box_file_url
- linked_at

## Notes

- The vector embedding system works offline using word frequency
- For production use, consider integrating with sentence-transformers or OpenAI embeddings
- Gmail and Calendar scanning requires Google Cloud OAuth setup
- Box integration requires Box API credentials

## Examples

```bash
# Find contacts you haven't talked to in a while
~/.openclaw/bin/personal_crm.py stale --days 60

# Set a reminder to follow up next week
~/.openclaw/bin/personal_crm.py followup create jane@company.com --days 7 --notes "Check on project status"

# Find duplicate contacts
~/.openclaw/bin/personal_crm.py duplicates --threshold 0.9

# Merge duplicate contacts
~/.openclaw/bin/personal_crm.py merge john@company.com john.d@company.com j.doe@company.com

# Search by company
~/.openclaw/bin/personal_crm.py search "Google"

# Search by role or context
~/.openclaw/bin/personal_crm.py search "product manager"
~/.openclaw/bin/personal_crm.py search "met at conference"
```
