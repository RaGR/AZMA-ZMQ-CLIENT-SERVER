import zmq
import json
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, socket):
        pass

class OSCommand(Command):
    def __init__(self, command, params):
        self.command = command
        self.params = params

    def execute(self, socket):
        request = {
            "command_type": "os",
            "command_name": self.command,
            "parameters": self.params
        }
        return self._send_request(socket, request)

    def _send_request(self, socket, request):
        socket.send_string(json.dumps(request))
        return socket.recv_string()

class MathCommand(Command):
    def __init__(self, expression):
        self.expression = expression

    def execute(self, socket):
        request = {
            "command_type": "compute",
            "expression": self.expression
        }
        return self._send_request(socket, request)

    def _send_request(self, socket, request):
        socket.send_string(json.dumps(request))
        return socket.recv_string()

class Client:
    def __init__(self, server_address="tcp://localhost:5555"):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(server_address)

    def send_command(self, command):
        return command.execute(self.socket)

    def close(self):
        self.socket.close()
        self.context.term()

def main():
    client = Client()
    
    while True:
        print("\n--- ZMQ Client ---")
        print("1. Run OS Command")
        print("2. Compute Math Expression")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            command = input("Enter OS command: ")
            params = input("Enter parameters (space-separated): ").split()
            response = client.send_command(OSCommand(command, params))
            print("Response:", response)
        
        elif choice == '2':
            expression = input("Enter math expression: ")
            response = client.send_command(MathCommand(expression))
            print("Result:", response)
        
        elif choice == '3':
            print("Exiting...")
            client.close()
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

