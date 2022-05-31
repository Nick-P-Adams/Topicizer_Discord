from Topicizer import Topicizer
from Settings import Settings
from discord.ext import commands

if __name__ == '__main__':
    topicizer = Topicizer()
    bot = commands.Bot(command_prefix='!')

    @bot.command(name='test')
    async def test(ctx):
        response = "tesst"
        await ctx.send(response)

    bot.run(Settings.TOKEN())