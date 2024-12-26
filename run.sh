#!/bin/bash

# Define virtual environment and requirements file paths
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Check if .env file exists
if [ ! -f .env ]; then
  echo ".env file not found! Please make sure it's in the root of the project."
  exit 1
fi

# Check if virtual environment exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment not found. Creating one..."
  python3 -m venv "$VENV_DIR"
  echo "Virtual environment created at $VENV_DIR"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Check if requirements.txt exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
  echo "$REQUIREMENTS_FILE not found! Please make sure the requirements file is present."
  exit 1
fi

# Install required dependencies
echo "Installing dependencies from $REQUIREMENTS_FILE..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Run the FastAPI application with uvicorn
echo "Starting FastAPI application..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
