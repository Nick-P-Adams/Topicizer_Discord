# Add all async command functions for Topicizer here
def TopicizerCommands(topicizer):

    @topicizer.bot.command(name='test')
    async def test(ctx):
        response = "tesst"
        await ctx.send(response)