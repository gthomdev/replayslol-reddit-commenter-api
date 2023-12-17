import os
from dotenv import load_dotenv


class Credentials:
    def __init__(self):
        load_dotenv()
        self.connection_string = os.environ.get('POSTGRES_URL')
