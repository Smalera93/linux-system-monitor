# Linux System Monitor

A lightweight Linux system-monitoring application written in Python.

The application reads system information from Linux `/proc` interfaces and Python's standard library to report system uptime, memory usage, disk usage, CPU utilisation and network activity. Network monitoring includes cumulative received/sent data and current download/upload rates.

The application uses separate modules for reading system data, performing calculations and formatting the output.

## Features

- System uptime
- Memory usage, including total, available and used memory
- Disk usage and available space
- CPU utilisation calculated from two samples
- Network traffic totals and download/upload rates
- Human-readable output with automatic byte-unit formatting
- Error handling for invalid data and unavailable system information

## Requirements

- Linux operating system
- Python 3 (developed and tested with Python 3.12)

The application uses Python's standard library and does not require additional Python packages.

## Running the application

From the project directory, run:

```bash
PYTHONPATH=src python3 -m system_monitor.main
```

The application displays a system report in the terminal. CPU and network rates are calculated using samples taken over a short interval.

## Running the tests

Run the unit tests using:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

The project currently includes 72 automated unit tests covering calculations, formatting, boundary conditions and selected error cases.

GitHub Actions is configured to run the test suite automatically on pushes and pull requests.

## Implementation

System information is obtained from the following sources:

- `/proc/uptime` - system uptime
- `/proc/meminfo` - memory information
- `/proc/stat` - CPU time counters
- `/proc/net/dev` - network interface counters
- `shutil.disk_usage()` - disk capacity and usage

The code is organised into separate modules for each monitored resource, with shared formatting functions and a central entry point for generating the report.

## Project status

Ongoing personal project, developed to improve practical experience with Python, Linux system interfaces, automated testing and software development practices.
