import TopicizerCommands
from discord.ext import commands
from Settings import Settings
import json
import dotenv
import random

class Topicizer:
    def __init__(self):
        dotenv.load_dotenv()
        self.bot = commands.Bot(command_prefix='!')

        self.topics = {"Science" : {1 : "Anti-Gravity", 2 : "Moon Landing"}, "History" : {1 : "Battle of 1812", 2 : "Roman Empire"}}
        self.trivia = {}
        self.current_category = ""
        self.current_topic = ""
        self.current_trivia = ""
        self.answer = ""

    #def load(self):

    def save(self):
        with open("Topics.json", "w") as out_file:
            json.dump(self.topics, out_file)

        with open("Trivia.json", "w") as out_file:
            for dict in self.trivia:
                json.dump(dict, out_file)

    def spawn_bot(self):
        return self.bot

    def run_bot(self):
        self.bot.run(Settings.TOKEN())

    def commands(self):
        TopicizerCommands.TopicizerCommands(self.bot)
