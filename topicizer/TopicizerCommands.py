# Add all async command functions for Topicizer here
def TopicizerCommands(topicizer):

### Topic Commands ######################################################################

    @topicizer.bot.group(name='topic', invoke_without_command=True,
                         help="Allows Users To Display Current Topic\n\
                               !topic")
    async def topic(ctx):
        response = "Current Topic is: " + topicizer.get_topic()
        await ctx.send(response)

    @topic.command(name='fetch',
                   help="Sets A New Current Topic Randomly\n\
                         !topic fetch")
    async def fetch_topic(ctx):
        response = "New Topic is :" + topicizer.fetch_topic()
        await ctx.send(response)

    @topic.command(name='add',
                   help="Allows Users To Add New Topics\n\
                         !topic add \"topic\"\n\
                         Example: !topic add \"Search for life on Mars\"")
    async def add_topic(ctx, topic):
        topicizer.add_topic(topic)
        response = topic + " added to Topics"
        await ctx.send(response)

### Trivia Commands ######################################################################

    @topicizer.bot.group(name='trivia', invoke_without_command=True,
                         help="Allows Users To Display Current Trivia\n\
                               !trivia")
    async def trivia(ctx):
        response = "Current Trivia is: " + topicizer.get_trivia()
        await ctx.send(response)

    @trivia.command(name='fetch',
                    help="Sets A New Current Trivia Randomly\n\
                          !trivia fetch")
    async def fetch_trivia(ctx):
        response = "New Trivia is" + topicizer.fetch_trivia()
        await ctx.send(response)

    @trivia.command(name='add',
                    help="Allows Users To Add New Trivia Related To Topic Or Category Depending On Mode\n\
                          !trivia add \"trivia\" \"answer\"\n\
                          Example: !trivia add \"What year did Curiosity Rover land on Mars?\" \"2012\"")
    async def add_trivia(ctx, trivia, answer):
        topicizer.add_trivia(trivia, answer)
        response = trivia + " Trivia added with answer " + answer
        await ctx.send(response)

    @trivia.command(name='mode',
                    help="Allows Users To Toggle Trivia Mode Between Category And Topic\n\
                          By Default Mode Is Set To Category\n\
                          !trivia mode")
    async def switch_mode(ctx):
        topicizer.toggle_trivia_mode()
        response = "Trivia mode toggled"
        await ctx.send(response)

### Category Commands ######################################################################

    @topicizer.bot.group(name='category', invoke_without_command=True,
                         help="Allows Users To Specify Category\n\
                               !category \"category\"\n\
                               Example: !category \"Space\"")
    async def category(ctx, category):
        response = "New Category is: " + topicizer.fetch_category(category)
        await ctx.send(response)

    @category.command(name="add", help="Allows Users To Add New Categories\n\
                                       !category add \"category\"\n\
                                       Example: !category add \"Geography\"")
    async def add_category(ctx, category):
        topicizer.add_category(category)
        response = category + " has been added to Categories"
        await ctx.send(response)

    @category.command(name="list",
                      help="Allows Users To List All Categories\n\
                            !category list\n")
    async def list_categories(ctx):
        response = "List of Categories is: " + topicizer.list_category()
        await ctx.send(response)

### Bot Events ######################################################################

    @topicizer.bot.event
    async def on_ready():
        print(f'{topicizer.bot.user} has connected to Discord!')
