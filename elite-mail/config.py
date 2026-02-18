import os
from typing import Optional

class SMTPConfig:
    def __init__(self):
        # SMTP Server Configuration
        # You can use Gmail SMTP or AWS SES
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_username = os.getenv("SMTP_USERNAME", "")
        self.smtp_password = os.getenv("SMTP_PASSWORD", "")
        self.from_email = os.getenv("FROM_EMAIL", "")
        
        # For Gmail, you'll need an App Password
        # Go to: https://myaccount.google.com/apppasswords
        
    def is_configured(self) -> bool:
        return all([self.smtp_username, self.smtp_password, self.from_email])
    
    def get_config_info(self) -> dict:
        return {
            "smtp_server": self.smtp_server,
            "smtp_port": self.smtp_port,
            "username": self.smtp_username,
            "from_email": self.from_email,
            "configured": self.is_configured()
        }