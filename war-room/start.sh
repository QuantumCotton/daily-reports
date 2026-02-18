#!/bin/bash
# War Room Dashboard Startup Script

echo "========================================="
echo "Starting War Room Dashboard"
echo "========================================="
echo ""

# Check if server is already running
if pgrep -f "server.py" > /dev/null; then
    echo "⚠️  Server is already running!"
    echo "   PID: $(pgrep -f 'server.py')"
    echo ""
    echo "To stop the server, run:"
    echo "  kill $(pgrep -f 'server.py')"
    echo ""
    exit 1
fi

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if dependencies are installed
python3 -c "import flask, flask_cors" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Flask or flask-cors not installed!"
    echo "   Installing now..."
    pip3 install flask flask-cors --break-system-packages --quiet
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
    echo "✓ Dependencies installed"
fi

echo "✓ Starting server on port 10269..."
echo "  Dashboard URL: http://localhost:10269"
echo "  Press Ctrl+C to stop"
echo ""

# Start the server
python3 server.py
