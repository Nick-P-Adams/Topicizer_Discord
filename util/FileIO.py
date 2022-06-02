from util.Settings import Settings
import json

class FileIO:

    @staticmethod
    def save_topics(topics):
        with open(Settings.TopicFile(), "w") as out_file:
            json.dump(topics, out_file)

    @staticmethod
    def load_topics():
        topics = {}
        with open(Settings.TopicFile(), "r") as in_file:
            topics = json.load(in_file)
        return topics