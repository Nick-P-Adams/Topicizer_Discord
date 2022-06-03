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

    def add_topic(self, topic):
        ""

    def fetch_topic(self):
        ""

    def add_trivia(self,trivia):
        ""

    def fetch_trivia(self):
        ""

    def toggle_trivia_mode(self):
        self.__trivia_category_mode = not self.__trivia_category_mode

    def add_category(self, category):
        ""

    def fetch_category(self, category):
        ""

    def list_category(self):
        ""

    @staticmethod
    def __load():
        return FileIO.load_topics()

    def save(self):
        self.__topics = self.__sort_topics()
        FileIO.save_topics(self.__topics)

    @staticmethod
    def __spawn_bot():
        return commands.Bot(command_prefix='!')

    def run_bot(self):
        self.bot.run(Settings.TOKEN())

    def __sort_topics(self):
        return {key: val for key, val in sorted(self.__topics.items(), key=lambda element: element[0])}

    def get_topic(self): return self.__current_topic
    def get_trivia(self): return self.__current_trivia
    def get_category(self): return self.__current_category
