#Example of creating custom client (Will come back to if needed)
import discord

class TopicizerClient(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
