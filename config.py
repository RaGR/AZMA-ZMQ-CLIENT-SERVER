import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_ADDRESS = os.getenv('SERVER_ADDRESS', 'tcp://*:5555')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/server_logs.log')
    MAX_REQUESTS_PER_MINUTE = int(os.getenv('MAX_REQUESTS_PER_MINUTE', 60))
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
    JWT_EXPIRATION_MINUTES = int(os.getenv('JWT_EXPIRATION_MINUTES', 30))

