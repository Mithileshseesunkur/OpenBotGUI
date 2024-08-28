#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 1024x768x24 &

# Set the DISPLAY environment variable
export DISPLAY=:1

# Run your Python script
python main.py
