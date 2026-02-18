#!/usr/bin/env python3
"""
Simple test script to verify email sending functionality
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText

# Add current directory to path so we can import config
sys.path.insert(0, '.')
from config import SMTPConfig

def test_email_sending():
    """Test basic email sending functionality"""
    
    print("🧪 Testing Elite Mail MVP Email Functionality")
    print("=" * 50)
    
    # Load configuration
    config = SMTPConfig()
    
    # Check if configured
    if not config.is_configured():
        print("❌ SMTP not configured!")
        print("Please set these environment variables:")
        print("- SMTP_USERNAME")
        print("- SMTP_PASSWORD") 
        print("- FROM_EMAIL")
        print("\nFor Gmail, generate an App Password:")
        print("https://myaccount.google.com/apppasswords")
        return False
    
    print(f"✅ SMTP Configuration loaded:")
    print(f"   Server: {config.smtp_server}:{config.smtp_port}")
    print(f"   Username: {config.smtp_username}")
    print(f"   From: {config.from_email}")
    print()
    
    try:
        # Connect to SMTP server
        print("🔗 Connecting to SMTP server...")
        server = smtplib.SMTP(config.smtp_server, config.smtp_port)
        server.starttls()
        
        print("🔐 Authenticating...")
        server.login(config.smtp_username, config.smtp_password)
        print("✅ Authentication successful!")
        
        # Send test email
        test_to = config.from_email  # Send to self for testing
        test_subject = "Elite Mail MVP Test"
        test_body = """
This is a test email from Elite Mail MVP.

If you're receiving this, the email sending functionality is working correctly!

Timestamp: {}
        """.format(str(datetime.now()))
        
        print(f"📧 Sending test email to {test_to}...")
        
        msg = MIMEText(test_body)
        msg['Subject'] = test_subject
        msg['From'] = config.from_email
        msg['To'] = test_to
        
        server.send_message(msg)
        server.quit()
        
        print("✅ Test email sent successfully!")
        print(f"📬 Check your inbox at {test_to}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("Check your username/password or App Password")
        return False
        
    except smtplib.SMTPException as e:
        print(f"❌ SMTP Error: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Import datetime here for the test
    from datetime import datetime
    
    success = test_email_sending()
    
    if success:
        print("\n🎉 Email functionality is working!")
        print("You can now run: python app.py")
        print("Then visit: http://localhost:8000")
    else:
        print("\n💥 Email test failed!")
        print("Please fix the configuration before proceeding.")
    
    sys.exit(0 if success else 1)