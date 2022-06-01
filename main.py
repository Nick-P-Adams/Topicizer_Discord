from topicizer.Topicizer import Topicizer
from topicizer.TopicizerCommands import TopicizerCommands

if __name__ == '__main__':
    topicizer = Topicizer()
    topicizer.load()
    TopicizerCommands(topicizer)
    topicizer.save()
    topicizer.run_bot()
