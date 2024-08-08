import os
from dotenv import load_dotenv

load_dotenv('secret.env')
TOKEN = os.getenv('TOKEN')


class Config:
    def __init__(self):
        self.family_price_fish = 30000
        self.family_price_metallurgy = 15000
