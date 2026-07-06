# Linux Infrastructure Automation & Health Monitoring System

A beginner-friendly, production-inspired Linux System Engineering project built with Python and Bash. The project monitors key Linux system resources, checks essential services, generates health reports, and automates execution using Cron.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Load average monitoring
- System uptime monitoring
- Linux service status monitoring
- Configuration using JSON
- Structured logging
- Rotating log files
- JSON health report generation
- Bash automation
- Cron scheduling
- Modular Python architecture

## Project Structure

```
linux-health-monitor/
│
├── app/
│   ├── main.py
│   ├── monitor.py
│   ├── service_monitor.py
│   ├── config.py
│   ├── logger.py
│   ├── health.py
│   └── report.py
│
├── configs/
│   └── config.json
│
├── logs/
│
├── reports/
│
├── scripts/
│   └── run_monitor.sh
│
├── README.md
└── requirements.txt
```

## Technologies

- Python 3
- Bash
- Linux
- psutil
- JSON
- Git

## Linux Concepts Practiced

- File permissions
- Bash scripting
- Process monitoring
- Linux services
- Cron scheduling
- Logging
- Log rotation
- JSON configuration
- System resource monitoring

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd linux-health-monitor
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app/main.py
```

Or:

```bash
./scripts/run_monitor.sh
```

## Example Output

```
============================================================
Linux Health Monitor
============================================================

CPU Usage      : 21.3% [HEALTHY]
Memory Usage   : 42.6% [HEALTHY]
Disk Usage     : 54.2% [HEALTHY]
Load Average   : (0.18, 0.21, 0.19)
Uptime         : 2 days, 4 hours

Services
------------------------------
ssh         : Running
cron        : Running

Overall Health
------------------------------
HEALTHY
```

## Skills Demonstrated

- Linux System Administration
- Python Automation
- Bash Scripting
- Configuration Management
- Structured Logging
- Log Rotation
- System Monitoring
- Service Monitoring
- Cron Automation
- Git Version Control

