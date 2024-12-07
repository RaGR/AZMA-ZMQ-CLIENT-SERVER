import zmq
import json
import logging
import asyncio
from zmq.asyncio import Context
from command_handlers import CommandHandlerFactory
from config import Config
from utils import RateLimiter, authenticate, validate_input
import signal

class Server:
    def __init__(self):
        self.config = Config()
        self.context = Context.instance()
        self.socket = self.context.socket(zmq.REP)
        self.logger = self._setup_logger()
        self.command_handler_factory = CommandHandlerFactory()
        self.rate_limiter = RateLimiter(self.config.MAX_REQUESTS_PER_MINUTE)
        self.running = True

    def _setup_logger(self):
        logging.basicConfig(filename=self.config.LOG_FILE, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s: %(message)s')
        return logging.getLogger(__name__)

    async def start(self):
        self.socket.bind(self.config.SERVER_ADDRESS)
        self.logger.info("Server started and listening for requests.")
        print("Server started. Listening for incoming requests...")

        while self.running:
            try:
                json_request = await self.socket.recv_string()
                response = await self.handle_request(json_request)
                await self.socket.send_string(response)
            except Exception as e:
                self.logger.error(f"Error in main server loop: {str(e)}")

    async def handle_request(self, json_request):
        try:
            if not self.rate_limiter.allow_request():
                return json.dumps({"error": "Rate limit exceeded"})

            request = json.loads(json_request)
            self.logger.info(f"Received request: {request}")

            if not authenticate(request.get('token')):
                return json.dumps({"error": "Authentication failed"})

            if not validate_input(request):
                return json.dumps({"error": "Invalid input"})

            handler = self.command_handler_factory.get_handler(request['command_type'])
            response = await handler.handle(request)

            self.logger.info(f"Sending response: {response}")
            return json.dumps({"result": response})

        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            self.logger.error(error_msg)
            return json.dumps({"error": error_msg})

    def shutdown(self):
        self.running = False
        self.socket.close()
        self.context.term()
        self.logger.info("Server shut down gracefully")

def main():
    server = Server()
    loop = asyncio.get_event_loop()

    def signal_handler():
        print("Shutting down...")
        server.shutdown()
        loop.stop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler)

    try:
        loop.run_until_complete(server.start())
    finally:
        loop.close()

if __name__ == "__main__":
    main()

