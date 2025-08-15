# This example requires the 'message_content' intent.
from secret_token import TOKEN

import discord
import random
import ia

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$hello':
        await message.channel.send('Hello!')

    elif message.content == '/random_number':
        await message.channel.send(random.randint(1, 100))

    else:
        await message.channel.send(ia.gpt(message.content))
        

client.run(TOKEN)
