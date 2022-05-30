import discord

class TopicizerClient(discord.Client):
    def __init(self):
        super()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')