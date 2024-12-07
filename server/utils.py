import time
import jwt
from config import Config

class RateLimiter:
    def __init__(self, max_requests):
        self.max_requests = max_requests
        self.requests = []

    def allow_request(self):
        current_time = time.time()
        self.requests = [req for req in self.requests if current_time - req < 60]
        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False

def authenticate(token):
    try:
        jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
        return True
    except:
        return False

def validate_input(request):
    required_fields = ['command_type', 'token']
    if not all(field in request for field in required_fields):
        return False
    if request['command_type'] not in ['os', 'compute']:
        return False
    return True

