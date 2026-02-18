# Newsletter & CRM Platform Integration

## Overview
Integration scripts for Beehiiv (newsletter platform) and HubSpot (sales CRM) with SQLite caching for the business advisory council.

## Files Created

### Scripts (executable)
- `~/.openclaw/bin/beehiiv_sync.py` - Beehiiv data sync
- `~/.openclaw/bin/hubspot_sync.py` - HubSpot data sync

### Configuration
- `~/.openclaw/workspace/config/beehiiv.json` - Beehiiv API config
- `~/.openclaw/workspace/config/hubspot.json` - HubSpot API config

### Databases (created on first run)
- `~/.openclaw/workspace/analytics/beehiiv.db` - Beehiiv data cache
- `~/.openclaw/workspace/analytics/hubspot.db` - HubSpot data cache

## Beehiiv Sync Features

**Tracks:**
- Total, active, and paid subscriber counts
- 24h new subscribers and unsubscribes
- 7-day growth rate
- 30-day churn rate
- Per-post open rates and click rates
- Subscriber segments

**Database Tables:**
- `subscribers` - Subscriber snapshots with metrics
- `post_analytics` - Individual post performance
- `segments` - Subscriber segments
- `metrics_history` - Historical trend data

## HubSpot Sync Features

**Tracks:**
- Deals (stage, value, active deals)
- Deal lifecycle (closed won/lost)
- Pipeline status by stage
- Contacts (basic info, lifecycle stage)
- Customer status

**Database Tables:**
- `deals` - Deal records with stage/value
- `contacts` - Contact information
- `pipeline_status` - Pipeline stage summaries
- `metrics_history` - Aggregate metrics over time
- `deal_contacts` - Deal-contact relationships

## Setup

### 1. Configure Beehiiv
Edit `~/.openclaw/workspace/config/beehiiv.json`:
```json
{
  "api_key": "your_beehiiv_api_key",
  "publication_id": "your_publication_id"
}
```

Get API key: https://www.beehiiv.com/developers/api

### 2. Configure HubSpot
Edit `~/.openclaw/workspace/config/hubspot.json`:
```json
{
  "api_key": "your_hubspot_api_key",
  "portal_id": "your_portal_id"
}
```

Get API key: https://developers.hubspot.com/docs/api/overview

### 3. Install Dependencies
```bash
pip install requests
```

## Usage

Run syncs manually:
```bash
~/.openclaw/bin/beehiiv_sync.py
~/.openclaw/bin/hubspot_sync.py
```

Add to cron for automated syncs (e.g., every hour):
```bash
# Edit crontab
crontab -e

# Add these lines:
0 * * * * ~/.openclaw/bin/beehiiv_sync.py >> ~/.openclaw/logs/beehiiv_sync.log 2>&1
0 * * * * ~/.openclaw/bin/hubspot_sync.py >> ~/.openclaw/logs/hubspot_sync.log 2>&1
```

## Query Examples

### Beehiiv - Latest subscriber metrics
```sql
SELECT * FROM subscribers ORDER BY synced_at DESC LIMIT 1;
```

### Beehiiv - Post performance
```sql
SELECT post_title, open_rate, click_rate, published_at
FROM post_analytics
ORDER BY published_at DESC;
```

### HubSpot - Active deals by stage
```sql
SELECT pipeline_label, stage_label, active_deals_count, total_value
FROM pipeline_status
WHERE synced_at = (SELECT MAX(synced_at) FROM pipeline_status)
ORDER BY pipeline_label, stage_order;
```

### HubSpot - Deal metrics trend
```sql
SELECT date, metric_value
FROM metrics_history
WHERE metric_type = 'pipeline_value'
ORDER BY date DESC;
```

## Integration with Business Advisory Council

The cached data is available for:
- Cross-platform analysis (newsletter engagement vs deal velocity)
- Lead attribution (newsletter readers converting to customers)
- Performance dashboards
- Automated reporting

## Notes
- Scripts create databases automatically on first run
- Historical data preserved for trend analysis
- Error handling with clear error messages
- Pagination support for large datasets
- Graceful handling of missing API endpoints
