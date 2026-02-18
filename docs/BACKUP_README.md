# Database Backup System for CRM

A secure, automated backup system for SQLite databases with encryption, Google Drive integration, and Telegram alerts.

## Features

- ✅ **Auto-discovery**: Finds all SQLite databases in workspace
- ✅ **Encryption**: AES-256 encryption for all backups
- ✅ **Google Drive**: Automatic upload with folder management
- ✅ **Rotation**: Keeps last 7 backups automatically
- ✅ **Alerts**: Telegram notifications on backup failures
- ✅ **Logging**: Rotating log files for troubleshooting

## Installation

### 1. Install Dependencies

```bash
pip3 install pydrive2 cryptography python-telegram-bot --break-system-packages
```

### 2. Setup Configuration Files

#### 2.1 Copy configuration to workspace

```bash
mkdir -p ~/.openclaw/workspace/config
cp backup_config.json ~/.openclaw/workspace/config/
```

#### 2.2 Edit the configuration

```bash
nano ~/.openclaw/workspace/config/backup_config.json
```

**Required settings to configure:**

1. **Encryption Key** (MUST be at least 32 characters):
   ```json
   "encryption_key": "your-secure-encryption-key-min-32-characters"
   ```

2. **Telegram Bot** (for alerts):
   - Create a bot via @BotFather on Telegram
   - Get your bot token and chat ID
   ```json
   "telegram": {
     "bot_token": "your_bot_token",
     "chat_id": "your_chat_id"
   }
   ```

3. **Google Drive** (for backup storage):
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project
   - Enable Google Drive API
   - Create OAuth 2.0 credentials (Desktop application)
   - Download `client_secrets.json`
   - Rename to `gdrive_credentials.json` and save to `~/.openclaw/workspace/config/`

### 3. Install Scripts

```bash
cp db_backup.py ~/.openclaw/bin/
cp db_restore.py ~/.openclaw/bin/
chmod +x ~/.openclaw/bin/db_backup.py ~/.openclaw/bin/db_restore.py
```

## Usage

### Running Backups

#### Manual Backup
```bash
python3 ~/.openclaw/bin/db_backup.py
```

#### Test Mode (discover databases only, no backup)
```bash
python3 ~/.openclaw/bin/db_backup.py --test
```

#### With custom config
```bash
python3 ~/.openclaw/bin/db_backup.py --config /path/to/config.json
```

### Restoring Backups

#### List available backups on Drive
```bash
python3 ~/.openclaw/bin/db_restore.py --list
```

#### Restore from local file
```bash
python3 ~/.openclaw/bin/db_restore.py --file /path/to/backup.tar.enc
```

#### Restore from Google Drive (interactive)
```bash
python3 ~/.openclaw/bin/db_restore.py
```

#### Restore specific backup from Drive
```bash
python3 ~/.openclaw/bin/db_restore.py --drive-id "backup_file_id"
python3 ~/.openclaw/bin/db_restore.py --drive-name "crm_db_backup_20260217_201415.tar.enc"
```

## Setting Up Cron (Automated Backups)

Add to crontab for daily backups at 2 AM:

```bash
crontab -e
```

Add line:
```
0 2 * * * /usr/bin/python3 /home/chris/.openclaw/bin/db_backup.py
```

## File Structure

```
~/.openclaw/
├── workspace/
│   ├── config/
│   │   ├── backup_config.json          # Main configuration
│   │   └── gdrive_credentials.json     # Google Drive OAuth
│   └── logs/
│       └── db_backup.log               # Backup logs
└── bin/
    ├── db_backup.py                    # Backup script
    └── db_restore.py                   # Restore script
```

## Backup Process

1. **Discover**: Scan workspace for *.db, *.sqlite, *.sqlite3 files
2. **Archive**: Create tar archive with relative paths
3. **Encrypt**: AES-256 encrypt the archive
4. **Upload**: Upload to Google Drive folder
5. **Rotate**: Delete backups older than 7 days
6. **Alert**: Send Telegram notification on failure

## Security

- All backups encrypted with AES-256 (Fernet)
- Encryption key derived from your secret key using PBKDF2 (100,000 iterations)
- Credentials saved locally only
- Never transmit encryption keys over network

## Troubleshooting

### Google Drive Authentication

First run will open browser window for OAuth consent. Credentials are saved to avoid re-authentication.

### Encryption Key Error

```
ValueError: Encryption key must be at least 32 characters
```

Update your config with a longer key:
```bash
nano ~/.openclaw/workspace/config/backup_config.json
```

### Telegram Bot Not Working

Check logs:
```bash
tail -f ~/.openclaw/workspace/logs/db_backup.log
```

Ensure:
- Bot token is correct
- Chat ID is correct
- Bot has permission to send messages

### No Databases Found

Run test mode to see what's discovered:
```bash
python3 ~/.openclaw/bin/db_backup.py --test
```

Check patterns in config:
```json
"include_patterns": ["*.db", "*.sqlite", "*.sqlite3"]
```

## Logs

View backup logs:
```bash
tail -f ~/.openclaw/workspace/logs/db_backup.log
```

Logs are rotated automatically when they reach 10MB (keeps 5 backups).

## Backup Naming

Backups follow this pattern:
```
crm_db_backup_YYYYMMDD_HHMMSS.tar.enc
```

Example: `crm_db_backup_20260217_201415.tar.enc`

## Restoration Safety

⚠️ **Warning**: Restoration overwrites existing databases!

Always:
1. Test restore in a staging environment first
2. Verify backup integrity
3. Have a backup of your backup
4. Confirm prompts when running restore

## Support

For issues, check:
1. Log file: `~/.openclaw/workspace/logs/db_backup.log`
2. Google Drive folder: "CRM Database Backups"
3. Telegram alerts for failures
