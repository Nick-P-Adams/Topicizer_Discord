# Add all async command functions for Topicizer here
def TopicizerCommands(topicizer):

    @topicizer.bot.group(name='topic', invoke_without_command=True, help="Gives Topic Of Current Category")
    async def topic(ctx):
        response = "tesst"
        await ctx.send(response)

    @topic.command(name='add', help="Allows Users To Add New Topics\n\
                                     !topic add (topic)\n\
                                     Example: !topic add \"Search for life on Mars\"")
    async def add_topic(ctx, topic):
        response = "tesst"
        await ctx.send(response)

    @topicizer.bot.group(name='trivia', invoke_without_command=True,
                         help="Command For Getting And Adding Trivia Based On Current Topic Or Category")
    async def trivia(ctx):
        response = "tesst1"
        await ctx.send(response)

    @trivia.command(name='add',
                    help="Allows User To Add New Trivia Related To Topic\n\
                          !trivia add (trivia) (answer)\n\
                          Example: !trivia add \"What year did Curiosity Rover land on Mars?\" \"2012\"")
    async def add_trivia(ctx, trivia, answer):
        print(trivia)
        print(answer)
        response = "tesst2"
        await ctx.send(response)

    @trivia.command(name='mode')
    async def switch_mode(ctx):
        print("hi")

    @topicizer.bot.command(name='category', help="Allows Users To Specify Category\n\
                                                 !category (category)\n\
                                                 Example: !category Space")
    async def category(ctx, category):
        response = "tesst"
        await ctx.send(response)

    @topicizer.bot.event
    async def on_ready():
        print(f'{topicizer.bot.user} has connected to Discord!')