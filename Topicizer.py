from TopicizerClient import TopicizerClient
import dotenv
import os

class TopicizerBot:
    def __init__(self):
        dotenv.load_dotenv()
        self.TOKEN = os.getenv("DISCORD_TOKEN")
        self.client = TopicizerClient()

    def run(self):
        self.client.run(self.TOKEN)