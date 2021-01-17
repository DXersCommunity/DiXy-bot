import discord
import os
import json
import requests
import twitter
from keep_alive import keep_alive


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)



@client.event
async def on_ready():
  print('We have logged in as {0.user}\n'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    #don't respond to ourself
    return

  msg = message.content
  if msg.startswith('/quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('/listall'):
    channels = get_all_channels()

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))