BOT_TOKEN = "***"
REDDIT_SECRET_KEY = "***"
REDDIT_CLIENT_ID = "***"
REDDIT_USERNAME = "***"
REDDIT_PW = "***"

import discord
import requests
import random

Reddit_auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY)

parameters = {
    "grant_type": "password",
    "username": REDDIT_USERNAME,
    "password": REDDIT_PW,
}

headers = {"User-Agent": "MyAPI/0.0.1"}
res = requests.post("https://www.reddit.com/api/v1/access_token"
                    , auth=Reddit_auth, data=parameters, headers=headers)

ACCESS_TOKEN = res.json()["access_token"]

headers["Authorization"] = f"bearer {ACCESS_TOKEN}"

test = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers).json()
print(requests.Response.status_code)

res = requests.get("https://oauth.reddit.com/r/dankmemes/hot",
                   headers=headers)

meme_data_list = res.json()['data']['children']
meme_url_databank = []

for item in meme_data_list:
    meme_url_databank.append(item['data']['url'])

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("hello!")

    if message.content.startswith("!meme"):
        meme_randomiser = random.randint(1, len(meme_url_databank) - 1)
        await message.channel.send(meme_url_databank[meme_randomiser])

client.run(BOT_TOKEN)
