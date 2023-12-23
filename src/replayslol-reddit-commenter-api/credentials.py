import os
from dotenv import load_dotenv


class Credentials:
    def __init__(self):
        load_dotenv()
        self.connection_string = os.environ.get('POSTGRES_URL')
        self.valid_tokens = os.environ.get('VALID_TOKENS').split(',')
