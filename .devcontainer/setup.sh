#!/usr/bin/env bash
set -e

echo "Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..
chmod +x .devcontainer/setup.sh
echo "Setup complete."