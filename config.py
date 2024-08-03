import os
from dotenv import load_dotenv

load_dotenv('secret.env')
TOKEN = os.getenv('TOKEN')
