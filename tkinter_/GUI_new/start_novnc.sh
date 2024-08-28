#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 1024x768x24 &

# Set the DISPLAY environment variable
export DISPLAY=:1

# Start websockify
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Start noVNC
/usr/share/novnc/utils/launch.sh --vnc localhost:5900 &

# Run your Python script
python gui_main.py
