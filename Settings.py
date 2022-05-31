from enum import Enum
import os

class Settings(Enum):

    @staticmethod
    def TOKEN():
        try:
            return os.getenv("DISCORD_TOKEN")
        except:
            print("ERROR: Could not find bot Token")

