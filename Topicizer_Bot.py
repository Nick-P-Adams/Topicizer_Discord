import discord
from env_loader import load_env

env = load_env()
token = env.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)



