# Elite Mail MVP

A minimal viable email sending web application with SMTP integration.

## Features

- Simple web interface for sending emails
- SMTP integration (Gmail/AWS SES compatible)
- Basic email logging
- RESTful API endpoints

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure SMTP

Set environment variables for your SMTP provider:

#### For Gmail SMTP:
```bash
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USERNAME="your-gmail@gmail.com"
export SMTP_PASSWORD="your-app-password"
export FROM_EMAIL="your-gmail@gmail.com"
```

**Important for Gmail:** You need to generate an App Password:
1. Go to https://myaccount.google.com/apppasswords
2. Enable 2-factor authentication if not already enabled
3. Generate a new App Password for "Mail"
4. Use this App Password as your SMTP_PASSWORD

#### For AWS SES:
```bash
export SMTP_SERVER="email-smtp.us-east-1.amazonaws.com"
export SMTP_PORT="587"
export SMTP_USERNAME="your-aws-ses-username"
export SMTP_PASSWORD="your-aws-ses-password"
export FROM_EMAIL="your-verified-email@example.com"
```

### 3. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:8000`

## Usage

### Web Interface
1. Open `http://localhost:8000` in your browser
2. Fill out the email form (to, subject, message)
3. Click "Send Email"

### API Endpoints

- `GET /` - Web interface
- `POST /send-email` - Send an email
- `GET /logs` - View email logs
- `GET /status` - Check SMTP configuration status
- `GET /health` - Health check

#### Send Email API Example

```bash
curl -X POST "http://localhost:8000/send-email" \
     -H "Content-Type: application/json" \
     -d '{
       "to": "recipient@example.com",
       "subject": "Test Email",
       "message": "This is a test email from Elite Mail MVP."
     }'
```

## File Structure

```
elite-mail/
├── index.html      # Web interface
├── app.py          # FastAPI backend
├── config.py       # SMTP configuration
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Development

This MVP uses in-memory logging for simplicity. For production, consider:

- Database persistence for logs
- Queue system for bulk email sending
- Rate limiting
- Authentication/authorization
- Open/click tracking

## Troubleshooting

### Gmail Authentication Issues
- Enable 2-factor authentication on your Google account
- Generate an App Password (don't use your regular password)
- Check that "Less secure app access" is not required with App Passwords

### AWS SES Issues
- Verify your sender email address in AWS SES
- Ensure you're out of the SES sandbox for sending to external addresses
- Check your AWS credentials have SES permissions

### Port Already in Use
If port 8000 is already in use, you can change it:
```bash
uvicorn app:app --host 0.0.0.0 --port 8001
```

## License

MIT License - feel free to use this code for your projects.