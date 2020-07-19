import discord
from discord.ext import commands, tasks
import pokebase as pb
import praw
import random

reddit = praw.Reddit(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,password=PASSWORD,user_agent="DiscordConnection",username=USER)
client = discord.Client()
subreddit = reddit.subreddit("funny")
client = discord.Client()
myUserId = 458474704001433610       #User id from discord, enable developer mode to see id's
serverId = 592892913004969985       #Server id from discord
channelId = 731606578901418056

#CODE FOR REDDIT POSTS
@client.event
async def on_connect():
    print('Connected to discord servers')

@client.event
async def on_disconnect():
    print("Disconnected")

@client.event
async def on_ready():
    message_channel = client.get_channel(734178390868754533)    #reddit posts
    for submission in subreddit.stream.submissions():
        if submission.is_self == False:
            embed = discord.Embed(url="https://reddit.com/r/funny/comments/"+str(submission),title=submission.title)
            embed.add_field(name="Subreddit",value=subreddit.display_name)
            embed.set_image(url=submission.url)
            await message_channel.send(embed=embed)
            print("Link logged")
        else:
            embed = discord.Embed(url=submission.url,title=submission.title)
            await message_channel.send(embed=embed)

       
client.run(BOT_TOKEN)
