from enum import Enum
import os

class Settings(Enum):

    @staticmethod
    def TOKEN():
        try:
            return os.getenv("DISCORD_TOKEN")
        except:
            print("ERROR: Could Not Find Bot Token!")

    @staticmethod
    def TopicFile():
        try:
            return os.getenv("TOPIC_FILE_PATH")
        except:
            print("ERROR: Topic File Not Found!")

