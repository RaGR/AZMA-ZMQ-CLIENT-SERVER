from abc import ABC, abstractmethod
import logging
from .os_commands import OSCommandHandler
from .math_commands import MathCommandHandler

class CommandHandler(ABC):
    @abstractmethod
    def handle(self, request):
        pass

class CommandHandlerFactory:
    def __init__(self):
        self.handlers = {
            'os': OSCommandHandler(),
            'compute': MathCommandHandler()
        }

    def get_handler(self, command_type):
        handler = self.handlers.get(command_type)
        if not handler:
            raise ValueError(f"Unknown command type: {command_type}")
        return handler

