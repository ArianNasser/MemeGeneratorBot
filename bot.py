BOT_TOKEN = "***"
REDDIT_SECRET_KEY = "***"
REDDIT_CLIENT_ID = "***"
REDDIT_USERNAME = "***"
REDDIT_PW = "***"

import discord
import requests

#------------------------------------------------------ DISCORD BOT SETUP BLOCK ----------------------------------------------------------------------#

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

#---------------------------------------------------- REDDIT API CONNECTION BLOCK --------------------------------------------------------------------#

Reddit_auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY)

parameters = {
    'grant_type': 'password',
    'username': REDDIT_USERNAME,
    'password': REDDIT_PW,
}

headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token'
, auth=Reddit_auth, data=parameters, headers=headers)

ACCESS_TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {ACCESS_TOKEN}'


#----------------------------------------------------- CONNECTION STATUS CODE TEST -------------------------------------------------------------------#

test = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()
print(requests.Response.status_code)








