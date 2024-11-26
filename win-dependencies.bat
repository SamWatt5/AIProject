@echo off

echo "Creating virtual environment..."
py -m venv .venv

echo "Activating virtual environment..."
call .venv\Scripts\activate

echo "Installing pip..."
py -m pip install --upgrade pip
py -m pip --version

echo "Installing packages..."
pip install pandas pillow tk flask flask-cors
if %errorlevel% neq 0 (
    echo "Error: Failed to install packages."
    exit /b 1
)

echo "All packages installed successfully!"
pause