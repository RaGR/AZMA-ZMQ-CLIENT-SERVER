# ZMQ Client-Server Communication System

## Overview

This project implements a robust ZeroMQ (ZMQ) based communication system designed for secure remote command execution and mathematical computations. By leveraging ZeroMQ's messaging capabilities, the system provides a flexible and efficient solution for distributed computing tasks.

## Features

- Remote command execution
- Secure mathematical computation
- Flexible command routing
- Comprehensive logging
- Performance monitoring

## Prerequisites

- Python 3.8+
- ZeroMQ library
- Recommended: Virtual environment

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/RaGR/AZMA-ZMQ-CLIENT-SERVER
cd AZMA-ZMQ-CLIENT-SERVER
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

bashCopypip install -r requirements.txt
Running the System
Start the Server
```bash 
python server/main.py
```

Run the Client
```bash
python client/main.py
```

## Project Structure
```
Copyzmq-client-server/
├── client/
│   ├── main.py
│   └── utils.py
├── server/
│   ├── main.py
│   └── command_handlers/
│       ├── os_commands.py
│       └── math_commands.py
├── tests/
│   ├── test_client.py
│   └── test_server.py
├── logs/
│   └── server_logs.log
└── requirements.txt
```

## Security Considerations

Restricted command execution environment
Comprehensive activity logging
Secure mathematical expression evaluation
Potential JWT authentication implementation

## Extending the Project
###Adding New Command Types

Create a handler in server/command_handlers/
Update command routing in server/main.py
Modify client to support new command type

## Troubleshooting
### Common Issues

### Connection Refused:

Verify server is running
Check firewall settings


### Authentication Failures:

Review configuration
Validate credentials


### Performance Bottlenecks:

Analyze logs
Optimize resource allocation



## Contributing

Fork the repository
Create a feature branch
Commit changes
Push to the branch
Open a pull request

## Contact

Maintainer: Ramtin
Email: ramtin7.samadi@gmail.com
Project Link: AZMA-ZMQ-CLIENT-SERVER
