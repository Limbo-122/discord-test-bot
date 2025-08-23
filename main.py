# This example requires the 'message_content' intent.
from secret_token import TOKEN
import asyncio
import discord
import random
import ia
from datetime import timedelta

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

#@bot.message_handler(content_types=['new_chat_members'])
    #def make_some(message):
        #bot.send_message(message.chat.id, 'I accepted a new user!')
        #bot.approve_chat_join_request(message.chat.id, message.from_user.id)
        #код не подходит к дискорду

    elif message.content == '/random_number':
        await message.channel.send(random.randint(1, 100))

    elif '<@992042142912495676>' in message.content:
            await message.author.timeout(timedelta(seconds = 15), reason = "Don't ping creator")
            await message.channel.send("You have been timed out for: Don't ping creator (15 seconds)")


    else:
        await message.channel.send(ia.gpt(message.content))
        print(message.content)

    
        

client.run(TOKEN)
