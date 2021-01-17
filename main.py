import discord
from discord.ext import commands
import os
import json
import requests
from keep_alive import keep_alive

DISCORD_GUILD=os.getenv('DISCORD_GUILD')
DISCORD_TOKEN=os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.command(name='pinchme')
@commands.has_role('DXAdmin')
async def pinchme(ctx):
    print("auw!")
    await ctx.send("Auw!")

@bot.command(name='quote', help='Respond with a random qoute from someone famous.')
async def quote(ctx):
  quote = get_quote()
  print(f"Quote: {quote}")
  await ctx.send(quote)

@bot.command(name='server')
async def fetchServerInfo(ctx):
	guild = ctx.guild
	await ctx.send(f'Server Name: {guild.name}\nNumber of Users: {guild.member_count}\nNumber of Channels: {len(guild.channels)}')
	
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
  print(f'Bot has logged in as {bot.user}\n')
  guild = discord.utils.get(bot.guilds, name=DISCORD_GUILD)
  print(
      f'{bot.user} is connected to the following guild:\n'
      f'{guild.name}(id: {guild.id})'
  )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the DXers community.\n We hope you will enjoy yourself here!'
    )


keep_alive()
bot.run(DISCORD_TOKEN)
