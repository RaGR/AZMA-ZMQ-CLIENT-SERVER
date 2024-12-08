# ZMQ Client-Server Communication Project 🤖

Hey there! Welcome to my ZeroMQ project - a pretty cool little system for running remote commands and doing some math magic.

## What's This All About? 🤔

So, I built this project to make remote communication between clients and servers super smooth and secure. Think of it like a walkie-talkie for computers, but way more powerful!

## Getting Started

### What You'll Need
- Python 3.8 or newer (because who wants to use old stuff?)
- ZeroMQ library
- A virtual environment (trust me, it'll save you headaches)

### Let's Get This Running!

1. First, grab the code:
   ```bash
   git clone https://github.com/RaGR/AZMA-ZMQ-CLIENT-SERVER
   cd AZMA-ZMQ-CLIENT-SERVER

```

1.  Set up a virtual environment (seriously, do this):

    ```
    python3 -m venv venv
    source venv/bin/activate  # Windows users: use venv\Scripts\activate

    ```

2.  Install the dependencies:

    ```
    pip install -r requirements.txt

    ```

How to Use This Thing
---------------------

### Start the Server

```
python server/main.py

```

### Fire Up the Client

```
python client/main.py

```

### What Can You Do?

When you run the client, you'll see a menu with some cool options:

1.  Run OS commands (carefully!)
2.  Do some math calculations
3.  Quit and go do something else

Project Layout
--------------

Here's how everything's organized:

```
zmq-client-server/
├── client/         # Client-side magic
├── server/         # Server-side wizardry
├── tests/          # Making sure everything works
├── logs/           # Keeping track of what's happening
└── requirements.txt  # All the goodies we need

```

Security? We've Got You Covered 🛡️
-----------------------------------

-   Restricted command execution (no wild west here)
-   Logging everything (Big Brother style)
-   Safe math calculations
-   Potential for adding extra authentication

Wanna Contribute?
-----------------

1.  Fork the repo
2.  Create a cool feature branch
3.  Commit your awesome changes
4.  Push it up
5.  Open a pull request

Run Into Problems?
------------------

-   Connection issues? Check your server's running
-   Authentication troubles? Double-check your setup
-   Performance feeling sluggish? Time to optimize!

Get in Touch
------------

Got questions? Need to chat?

-   Email: <ramtin7.samadi@gmail.com>
-   Project Link: [GitHub Repo](https://github.com/RaGR/AZMA-ZMQ-CLIENT-SERVER)
