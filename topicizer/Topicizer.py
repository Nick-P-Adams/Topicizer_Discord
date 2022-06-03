from discord.ext import commands
from util.FileIO import FileIO
from util.Settings import Settings
import random
import dotenv


class Topicizer:
    def __init__(self):
        dotenv.load_dotenv(dotenv_path="app/.env")
        self.bot = self.__spawn_bot()

        self.__topics = self.__load()
        self.__trivia_category_mode = True
        self.__current_category = self.fetch_category("random")
        self.__current_topic = self.fetch_topic()
        self.__current_trivia = self.fetch_trivia()
        self.__answer = ""

    def add_topic(self, topic):
        self.__topics[self.__current_category]['Topic'][topic] = {}

    def fetch_topic(self):
        fetched_topic = random.choice(list(self.__topics[self.__current_category]['Topic']))
        self.__current_topic = fetched_topic
        return fetched_topic

    def add_trivia(self, trivia, answer):
        if self.__trivia_category_mode:
            self.__topics[self.__current_category]['Trivia'][trivia] = answer
        else:
            self.__topics[self.__current_category]['Topic'][self.__current_topic] += {trivia: answer}

    def fetch_trivia(self):
        if self.__trivia_category_mode:
            fetched_trivia = random.choice(list(self.__topics[self.__current_category]['Trivia']))
        else:
            fetched_trivia = random.choice(list(self.__topics[self.__current_category]['Topic'][self.__current_topic]))
        self.__current_trivia = fetched_trivia
        return fetched_trivia

    def toggle_trivia_mode(self):
        self.__trivia_category_mode = not self.__trivia_category_mode

    def add_category(self, category):
        self.__topics[category] = {"Topic": {}, "Trivia": {}}

    def fetch_category(self, category):
        fetched_category = "The category you entered does not exist\n\
                            Use command !category add \"{category}\" to add this category as a new one\n\
                            Use command !category \"random\" to get a random category\n\
                            Or use command !category list to get a list of all categories".format(category=category)

        if category.lower() == "random":
            fetched_category = random.choice(list(self.__topics))
        elif self.__topics.get(category) != None:
            fetched_category = category
        self.__current_category = fetched_category
        return fetched_category

    def list_category(self):
        return self.topics.keys()

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
