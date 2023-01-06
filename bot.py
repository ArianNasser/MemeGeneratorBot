
# BOT SETUP

BOT_TOKEN = "****"

import discord
import requests

client = discord.Client(intents=discord.Intents.all())

#bot login alert
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

def Hello():
    #bot says hello
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('hello!')



client.run(BOT_TOKEN)


# MEME GRAB USING API --- example not a meme databank, need to find a suitable API

# end point
url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

#parameters
querystring = {"top":"Top Text","bottom":"Bottom Text","meme":"Condescending-Wonka","font_size":"50","font":"Impact"}

#authentication
headers = {
	"X-RapidAPI-Key": "****",
	"X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
