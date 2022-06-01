from Settings import Settings
import json

class FileIO:

    @staticmethod
    def save_topics(topics):
        with open(Settings.TopicFile(), "w") as out_file:
            json.dump(topics, out_file)

    @staticmethod
    def save_trivia(trivia):
        with open(Settings.TriviaFile(), "w") as out_file:
            json.dump(trivia, out_file)

    @staticmethod
    def load_topics():
        topics = {}
        with open(Settings.TopicFile(), "r") as in_file:
            topics = json.load(in_file)
        return topics

    @staticmethod
    def load_trivia():
        trivia = {}
        with open(Settings.TriviaFile(), "r") as in_file:
            trivia = json.load(in_file)
        return trivia