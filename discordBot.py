import discord
import random

client = discord.Client()
myUserId = 458474704001433610       #User id from discord, enable developer mode to see id's
serverId = 592892913004969985       #Server id from discord

@client.event
async def on_connect():
    print('Bot has infiltrated the discord servers ÒwÓ')

@client.event
async def on_ready():
    print('Bot ready')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if 'you feel it' in message.content:
        await message.channel.send('Likelyhood of them \'feeling it\' is ' + str(random.randint(1,100)) + '%')
        print(message.author)

    if message.content.startswith('!members'):
        client.get_all_members()

    if message.content.startswith('!respond') and message.author == client.get_user(myUserId):
        await message.channel.send(client.get_emoji(714176747125342218)) #id for weirdchamp

    if str(client.get_guild(serverId).get_member(myUserId).status) != "online" and client.get_user(myUserId).mentioned_in(message):     #.status returns a Status object as a status, converted to string to check the conditional
        await message.channel.send("He's currently unavailable, please try again later")
        
    if client.get_user(myUserId).mentioned_in(message) and str(client.get_guild(serverId).get_member(myUserId).status) == "online":
        print(client.get_guild(serverId).get_member(myUserId).status)
        await message.channel.send("You don't need to ping him to get his attention <:weirdChamp:714176747125342218>")

    if message.content.startswith('!xur'):
        await message.channel.send("https://wherethefuckisxur.com/")
    
    if message.content.startswith("!map"):
        await message.channel.send(file=discord.File("Hollow Knight Map.jpg"))      #attaching files 
       
client.run('')
