# Add all async command functions for Topicizer here
def TopicizerCommands(topicizer):

### Topic Commands ######################################################################

    @topicizer.bot.group(name='topic', invoke_without_command=True,
                         help="Allows Users To Display Current Topic\n\
                               !topic")
    async def topic(ctx):
        response = "tesst"
        await ctx.send(response)

    @topic.command(name='fetch',
                   help="Sets A New Current Topic Randomly\n\
                         !topic fetch")
    async def fetch_topic(ctx):
        response = "tesst"
        await ctx.send(response)

    @topic.command(name='add',
                   help="Allows Users To Add New Topics\n\
                         !topic add \"topic\"\n\
                         Example: !topic add \"Search for life on Mars\"")
    async def add_topic(ctx, topic):
        response = "tesst"
        await ctx.send(response)

### Trivia Commands ######################################################################

    @topicizer.bot.group(name='trivia', invoke_without_command=True,
                         help="Allows Users To Display Current Trivia\n\
                               !trivia")
    async def trivia(ctx):
        response = "tesst1"
        await ctx.send(response)

    @trivia.command(name='fetch',
                    help="Sets A New Current Trivia Randomly\n\
                          !trivia fetch")
    async def fetch_trivia(ctx):
        response = "tesst"
        await ctx.send(response)

    @trivia.command(name='add',
                    help="Allows Users To Add New Trivia Related To Topic Or Category Depending On Mode\n\
                          !trivia add \"trivia\" \"answer\"\n\
                          Example: !trivia add \"What year did Curiosity Rover land on Mars?\" \"2012\"")
    async def add_trivia(ctx, trivia, answer):
        print(trivia)
        print(answer)
        response = "tesst2"
        await ctx.send(response)

    @trivia.command(name='mode',
                    help="Allows Users To Toggle Trivia Mode Between Category And Topic\n\
                          By Default Mode Is Set To Category\n\
                          !trivia mode")
    async def switch_mode(ctx):
        print("hi")

### Category Commands ######################################################################

    @topicizer.bot.group(name='category', invoke_without_command=True,
                         help="Allows Users To Specify Category\n\
                               !category \"category\"\n\
                               Example: !category \"Space\"\n\
                               Call !category To Display Current Category")
    async def category(ctx, category):
        response = "tesst"
        await ctx.send(response)

    @category.command(name="add", help="Allows Users To Add New Categories\n\
                                       !category add \"category\"\n\
                                       Example: !category add \"Geography\"")
    async def add_category(ctx, category):
        print("")

    @category.command(name="list",
                      help="Allows Users To List All Categories\n\
                            !category list\n")
    async def list_categories(ctx):
        print("")

### Bot Events ######################################################################

    @topicizer.bot.event
    async def on_ready():
        print(f'{topicizer.bot.user} has connected to Discord!')
