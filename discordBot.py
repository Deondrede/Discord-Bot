import discord
from discord.ext import commands, tasks
import pokebase as pb
import random

client = discord.Client()
myUserId = 458474704001433610       #User id from discord, enable developer mode to see id's
serverId = 592892913004969985       #Server id from discord
channelId = 731606578901418056

@client.event
async def on_connect():
    print('Bot has infiltrated servers ÒwÓ')
@client.event
async def on_ready():
    print('Bot ready')

@tasks.loop(minutes=30)
async def repost():
    random.seed()
    message_channel = client.get_channel(channelId)
    randomPoke = random.randint(1,700)
    pokeName = pb.APIResource('pokemon',randomPoke).name
    sprite = str(pb.APIResource('pokemon',randomPoke).sprites.front_default)     #URL for the sprite
    embed = discord.Embed()
    embed.set_image(url=sprite)
    await message_channel.send(embed = embed)
    print("Pokemon logged: " + pokeName)

@repost.before_loop
async def before():
    await client.wait_until_ready()
repost.start()

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

    if message.content.startswith('!sprite'):
        random.seed()
        sprite = str(pb.APIResource('pokemon',random.randint(1,500)).sprites.front_default)     #URL for the sprite
        embed = discord.Embed()
        embed.set_image(url=sprite)
        await message.channel.send(embed = embed)   

       
client.run(BOT_TOKEN)
