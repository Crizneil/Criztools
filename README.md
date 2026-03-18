# GH-CRIZ OMNI TOOL

A professional workspace manager for GitHub with integrated system monitoring and automation features.

## Features

- Pulse Heartbeat: Automated health logging to pulse.log.
- Network Sync: Automatic following based on keywords and unfollowing non-followers.
- Tech Scout: Real-time search for trending repositories in Laravel and JavaScript.
- System Monitor: Live display of CPU, RAM, and disk usage for PISCES Laptop.

## Technical Stack

- Python 3.10+
- PyGithub
- rich
- psutil

## Installation

### 1. Install Python (Windows)
If you do not have Python installed:
1. Download the installer from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer and **MUST** check the box that says "Add Python to PATH".
3. Once installed, open a new Terminal (PowerShell or CMD).

### 2. Install Dependencies
Run the following command to install the required libraries:
python -m pip install -r requirements.txt

### 3. Set GitHub Token
Set your GitHub token as an environment variable:
set GH_TOKEN=your_personal_access_token

### 4. Run the Application
python main.py

## Usage Flags

- --auto: Executes the Pulse Heartbeat and exits immediately.
