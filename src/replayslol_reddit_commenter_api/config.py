import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.connection_string = os.environ.get('POSTGRES_URL')
        self.valid_tokens = os.environ.get('VALID_TOKENS').split(',')
        self.ssl_keyfile = os.environ.get('SSL_KEYFILE')
        self.ssl_certfile = os.environ.get('SSL_CERTFILE')
        self.host_address = os.environ.get('HOST_ADDRESS')
        self.environment = os.environ.get('ENVIRONMENT')
