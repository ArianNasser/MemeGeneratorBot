
# BOT SETUP

BOT_TOKEN = "****"
import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('hello!')

client.run(BOT_TOKEN)


# MEME GRAB USING API --- example not a meme databank, need to find a suitable API

import requests

url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

querystring = {"top":"Top Text","bottom":"Bottom Text","meme":"Condescending-Wonka","font_size":"50","font":"Impact"}

headers = {
	"X-RapidAPI-Key": "****",
	"X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
