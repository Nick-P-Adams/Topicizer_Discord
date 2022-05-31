from TopicizerClient import TopicizerClient
from discord.ext import commands
from Settings import Settings
import dotenv
import random

class Topicizer:
    def __init__(self):
        dotenv.load_dotenv()
        self.client = TopicizerClient()
        self.bot = commands.Bot(command_prefix='!')

    def run_client(self):
        self.client.run(Settings.TOKEN())

    def run_bot(self):
        self.bot.run(Settings.TOKEN())
