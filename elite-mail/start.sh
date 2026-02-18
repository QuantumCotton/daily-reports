#!/bin/bash

echo "🚀 Elite Mail MVP Startup Script"
echo "================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🧪 Running email test..."
python3 test_email.py

if [ $? -eq 0 ]; then
    echo "✅ Email test passed! Starting server..."
    echo "🌐 Open http://localhost:8000 in your browser"
    python3 app.py
else
    echo "❌ Email test failed. Please configure SMTP first."
    echo ""
    echo "Example configuration:"
    echo "export SMTP_USERNAME='your-email@gmail.com'"
    echo "export SMTP_PASSWORD='your-app-password'"
    echo "export FROM_EMAIL='your-email@gmail.com'"
    echo ""
    echo "Then run: ./start.sh"
fi