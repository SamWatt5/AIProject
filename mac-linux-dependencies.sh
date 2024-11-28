#!/bin/bash 

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate  

echo "Installing pip..."
python3 -m pip install --upgrade pip
python3 -m pip --version

echo "Installing packages..."
python3 -m pip install pandas flask flask-cors

echo "Ensuring flask-cors is properly installed"
python3 -m pip install flask-cors
python3 -m pip show flask-cors

echo "Ensuring that SSL certificates are properly configured"
python3 -m pip install certifi

if [ $? -ne 0 ]; then
    echo "Error: Failed to install packages."
    exit 1
fi

echo "All packages installed successfully!"
read -p "Press any key to continue..."