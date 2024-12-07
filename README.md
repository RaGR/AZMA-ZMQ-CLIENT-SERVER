# ZMQ Client-Server Communication Project

## 🚀 Overview

This project implements a robust ZeroMQ (ZMQ) based client-server communication system, enabling remote command execution and mathematical computations with enhanced security and flexibility.

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Security](#-security)
- [Extending the Project](#-extending-the-project)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- Remote OS command execution
- Secure mathematical computation
- Flexible command handling
- Comprehensive logging
- Performance monitoring
- Easy extensibility

## 🛠 Prerequisites

- Python 3.8+
- ZeroMQ library
- Virtual environment recommended

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/zmq-client-server.git
cd zmq-client-server
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Starting the Server
```bash
python server/main.py
```

### Running the Client
```bash
python client/main.py
```

### Client Menu Options
1. Run OS Command
2. Compute Mathematical Expression
3. Quit

## 📂 Project Structure
```
zmq-client-server/
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

## 🔒 Security Considerations

- Restricted command execution environment
- Logging of all server activities
- Safe mathematical expression evaluation
- Potential for JWT authentication implementation

## 🧩 Extending the Project

### Adding New Command Types

1. Create a new handler in `server/command_handlers/`
2. Update the command routing logic in `server/main.py`
3. Modify the client to support the new command type

## 🐛 Troubleshooting

### Common Issues
- Connection Refused: Check server is running, firewall settings
- Authentication Failures: Verify configuration
- Performance Problems: Review logging, increase resources

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/zmq-client-server](https://github.com/yourusername/zmq-client-server)
