import pytest
import asyncio
from server.command_handlers import CommandHandlerFactory
from server.utils import RateLimiter, authenticate, validate_input
from config import Config

@pytest.fixture
def command_handler_factory():
    return CommandHandlerFactory()

@pytest.mark.asyncio
async def test_os_command_handler(command_handler_factory):
    handler = command_handler_factory.get_handler('os')
    request = {
        'command_name': 'echo',
        'parameters': ['Hello, World!']
    }
    result = await handler.handle(request)
    assert result.strip() == 'Hello, World!'

@pytest.mark.asyncio
async def test_math_command_handler(command_handler_factory):
    handler = command_handler_factory.get_handler('compute')
    test_cases = [
        {'expression': '2 + 2', 'expected': '4'},
        {'expression': 'max(10, 20)', 'expected': '20'},
        {'expression': 'round(3.7)', 'expected': '4'},
        {'expression': 'pow(2, 3)', 'expected': '8'},
        {'expression': 'sin(0)', 'expected': '0.0'},
    ]
    
    for case in test_cases:
        result = await handler.handle(case)
        assert result == case['expected']

@pytest.mark.asyncio
async def test_invalid_math_command(command_handler_factory):
    handler = command_handler_factory.get_handler('compute')
    request = {'expression': '__import__("os").system("rm -rf /")'}
    result = await handler.handle(request)
    assert "Error" in result

def test_rate_limiter():
    limiter = RateLimiter(2)
    assert limiter.allow_request()
    assert limiter.allow_request()
    assert not limiter.allow_request()

def test_authenticate():
    valid_token = jwt.encode({"user": "test"}, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
    assert authenticate(valid_token)
    assert not authenticate("invalid_token")

def test_validate_input():
    valid_request = {
        "command_type": "os",
        "token": "valid_token",
        "command_name": "echo",
        "parameters": ["test"]
    }
    assert validate_input(valid_request)

    invalid_request = {
        "command_type": "invalid",
        "token": "valid_token"
    }
    assert not validate_input(invalid_request)

@pytest.mark.asyncio
async def test_integration():
    # This test requires the server to be running
    import zmq.asyncio
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    request = {
        "command_type": "compute",
        "expression": "2 + 2",
        "token": "valid_token"  # Replace with a valid token
    }

    await socket.send_json(request)
    response = await socket.recv_json()

    assert "result" in response
    assert response["result"] == "4"

    socket.close()
    context.term()

