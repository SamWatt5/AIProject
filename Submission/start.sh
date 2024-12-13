#!/bin/bash

# Start Flask server in a new terminal window
osascript <<EOF
tell application "Terminal"
    do script "cd $(pwd); flask --app main run"
end tell
EOF

# Navigate to frontend directory
cd frontend || exit

# Install dependencies
npm install

# Pause (prompt user to continue)
read -p "Press Enter to start the frontend..."

# Start the frontend
npm start
