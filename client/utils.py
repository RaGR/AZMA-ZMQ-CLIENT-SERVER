import zmq
import json
import time
import logging
from abc import ABC, abstractmethod

class TestCommand(ABC):
    @abstractmethod
    def get_request(self):
        pass

class OSTestCommand(TestCommand):
    def get_request(self):
        return {
            "command_type": "os",
            "command_name": "echo",
            "parameters": ["Connection Test"]
        }

class MathTestCommand(TestCommand):
    def get_request(self):
        return {
            "command_type": "compute",
            "expression": "2 ** 3"
        }

class ZMQClientTester:
    def __init__(self, server_address="tcp://localhost:5555", timeout=5):
        self.server_address = server_address
        self.timeout = timeout
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        return logging.getLogger(__name__)

    def _create_socket(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self.server_address)
        socket.setsockopt(zmq.RCVTIMEO, self.timeout * 1000)
        return socket

    def test_connection(self):
        socket = self._create_socket()
        try:
            test_command = OSTestCommand()
            socket.send_string(json.dumps(test_command.get_request()))
            response = socket.recv_string()
            self.logger.info(f"Connection Test Response: {response}")
            return True
        except zmq.Again:
            self.logger.error("Connection Timeout")
            return False
        except Exception as e:
            self.logger.error(f"Connection Error: {e}")
            return False
        finally:
            socket.close()

    def performance_test(self, num_requests=10):
        socket = self._create_socket()
        results = {
            'successful_requests': 0,
            'failed_requests': 0,
            'total_time': 0
        }
        
        for i in range(num_requests):
            try:
                start_time = time.time()
                test_command = OSTestCommand() if i % 2 == 0 else MathTestCommand()
                socket.send_string(json.dumps(test_command.get_request()))
                response = socket.recv_string()
                end_time = time.time()
                request_time = end_time - start_time
                
                results['successful_requests'] += 1
                results['total_time'] += request_time
                
                self.logger.info(f"Request {i}: Response = {response}, Time = {request_time:.4f}s")
            except Exception as e:
                results['failed_requests'] += 1
                self.logger.error(f"Request {i} Failed: {e}")
        
        socket.close()
        return results

def main():
    tester = ZMQClientTester()
    
    print("Running Connection Test...")
    connection_result = tester.test_connection()
    
    if connection_result:
        print("Performance Testing...")
        performance_results = tester.performance_test()
        print("\nPerformance Summary:")
        print(f"Successful Requests: {performance_results['successful_requests']}")
        print(f"Failed Requests: {performance_results['failed_requests']}")
        print(f"Average Request Time: {performance_results['total_time'] / performance_results['successful_requests']:.4f}s")

if __name__ == "__main__":
    main()

