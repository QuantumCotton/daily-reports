import smtplib
import json
import logging
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, EmailStr

from config import SMTPConfig

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Elite Mail MVP", version="1.0.0")

# Initialize SMTP config
smtp_config = SMTPConfig()

# Simple in-memory logging (for MVP)
email_logs = []

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    message: str

def log_email_event(event_type: str, email_data: Dict[str, Any], status: str = "success", error: str = None):
    """Log email events"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "to": email_data.get("to"),
        "subject": email_data.get("subject"),
        "status": status,
        "error": error
    }
    email_logs.append(log_entry)
    logger.info(f"Email {event_type}: {log_entry}")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page"""
    try:
        with open("index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html not found")

@app.post("/send-email")
async def send_email(email_request: EmailRequest):
    """Send an email via SMTP"""
    
    if not smtp_config.is_configured():
        raise HTTPException(
            status_code=500, 
            detail="SMTP not configured. Please set SMTP_USERNAME, SMTP_PASSWORD, and FROM_EMAIL environment variables."
        )
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_config.from_email
        msg['To'] = email_request.to
        msg['Subject'] = email_request.subject
        
        # Add body to email
        body = MIMEText(email_request.message, 'plain')
        msg.attach(body)
        
        # Connect to SMTP server and send
        server = smtplib.SMTP(smtp_config.smtp_server, smtp_config.smtp_port)
        server.starttls()  # Secure the connection
        server.login(smtp_config.smtp_username, smtp_config.smtp_password)
        
        text = msg.as_string()
        server.sendmail(smtp_config.from_email, email_request.to, text)
        server.quit()
        
        # Log successful send
        log_email_event("sent", {
            "to": email_request.to,
            "subject": email_request.subject,
            "message": email_request.message
        })
        
        return {"message": f"Email sent successfully to {email_request.to}"}
        
    except smtplib.SMTPAuthenticationError:
        error_msg = "SMTP authentication failed. Check your username/password."
        log_email_event("authentication_failed", {
            "to": email_request.to,
            "subject": email_request.subject
        }, status="failed", error=error_msg)
        raise HTTPException(status_code=500, detail=error_msg)
        
    except smtplib.SMTPRecipientsRefused:
        error_msg = f"Recipient {email_request.to} refused by server."
        log_email_event("recipient_refused", {
            "to": email_request.to,
            "subject": email_request.subject
        }, status="failed", error=error_msg)
        raise HTTPException(status_code=400, detail=error_msg)
        
    except Exception as e:
        error_msg = f"Failed to send email: {str(e)}"
        log_email_event("send_failed", {
            "to": email_request.to,
            "subject": email_request.subject
        }, status="failed", error=str(e))
        raise HTTPException(status_code=500, detail=error_msg)

@app.get("/logs")
async def get_logs():
    """Get email logs"""
    return {"logs": email_logs}

@app.get("/status")
async def get_status():
    """Get SMTP configuration status"""
    return smtp_config.get_config_info()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    
    # Check if SMTP is configured
    if not smtp_config.is_configured():
        print("⚠️  WARNING: SMTP is not configured!")
        print("Please set the following environment variables:")
        print("- SMTP_USERNAME: Your SMTP username")
        print("- SMTP_PASSWORD: Your SMTP password")
        print("- FROM_EMAIL: Your from email address")
        print("\nFor Gmail SMTP:")
        print("- SMTP_SERVER: smtp.gmail.com")
        print("- SMTP_PORT: 587")
        print("- You'll need to generate an App Password: https://myaccount.google.com/apppasswords")
        print()
    
    print("🚀 Starting Elite Mail MVP server...")
    print("📧 SMTP Server:", smtp_config.smtp_server)
    print("🔧 Port: 8000")
    print("🌐 Open http://localhost:8000 to use the web interface")
    print()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)