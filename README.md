# Python TCP Port Scanner

A multithreaded TCP port scanner developed in Python that scans a target host for open ports within a specified port range. The project demonstrates socket programming, concurrency using threading, and basic network reconnaissance techniques.

## Features
- TCP port scanning
- Scan a specified range of ports
- Multithreaded scanning for faster performance
- Displays open and closed port status
- Logs scan results to a file
- Records scan time and duration
- Handles connection errors gracefully

## Technologies Used
- Python
- Socket Programming
- Threading
- File Handling

## Project Structure
```
port_scanner
│
├── port_scanner.py
├── test_server.py
└── results.txt
```

## Usage
Run the scanner:

```
# Python TCP Port Scanner

A multithreaded TCP port scanner developed in Python that scans a target host for open ports within a specified port range. The project demonstrates socket programming, concurrency using threading, and basic network reconnaissance techniques.

## Features
- TCP port scanning
- Scan a specified range of ports
- Multithreaded scanning for faster performance
- Displays open and closed port status
- Logs scan results to a file
- Records scan time and duration
- Handles connection errors gracefully

## Technologies Used
- Python
- Socket Programming
- Threading
- File Handling

## Project Structure
```
port_scanner
│
├── port_scanner.py
├── test_server.py
└── results.txt
```

## Usage
Run the scanner:

```
py port_scanner.py
```

Enter:
- Target IP address or hostname
- Starting port
- Ending port

Example:

```
Enter target IP or website: scanme.nmap.org
Enter starting port: 20
Enter ending port: 100
```

## Example Output
```
Scanning target: scanme.nmap.org
Scanning ports 20 to 100

Port 22 is OPEN
Port 80 is OPEN
Port 21 is CLOSED
```

## Disclaimer
This project is for educational and authorized security testing purposes only.
```

Enter:
- Target IP address or hostname
- Starting port
- Ending port

Example:

```
Enter target IP or website: scanme.nmap.org
Enter starting port: 20
Enter ending port: 100
```

## Example Output
```
Scanning target: scanme.nmap.org
Scanning ports 20 to 100

Port 22 is OPEN
Port 80 is OPEN
Port 21 is CLOSED
```

## Disclaimer
This project is for educational and authorized security testing purposes only.
