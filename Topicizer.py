from discord.ext import commands
from FileIO import FileIO
from Settings import Settings
import dotenv
import random

class Topicizer:
    def __init__(self):
        dotenv.load_dotenv()
        self.bot = self.spawn_bot()

        self.__topics = {}
        self.__trivia = {}
        self.__current_category = ""
        self.__current_topic = ""
        self.__current_trivia = ""
        self.__answer = ""

    def load(self):
        self.__topics = FileIO.load_topics()
        self.__trivia = FileIO.load_trivia()

    def save(self):
        FileIO.save_topics(self.__topics)
        FileIO.save_trivia(self.__trivia)

    def spawn_bot(self):
        bot = commands.Bot(command_prefix='!')
        return bot

    def run_bot(self):
        self.bot.run(Settings.TOKEN())
