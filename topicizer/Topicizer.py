from discord.ext import commands
from util.FileIO import FileIO
from util.Settings import Settings
import dotenv

class Topicizer:
    def __init__(self):
        dotenv.load_dotenv(dotenv_path="app/.env")
        self.bot = self.spawn_bot()

        self.__topics = self.load()
        self.__trivia_category_mode = True
        self.__current_category = ""
        self.__current_topic = ""
        self.__current_trivia = ""
        self.__answer = ""

    def load(self):
        return FileIO.load_topics()

    def save(self):
        FileIO.save_topics(self.__topics)

    def spawn_bot(self):
        bot = commands.Bot(command_prefix='!')
        return bot

    def run_bot(self):
        self.bot.run(Settings.TOKEN())
