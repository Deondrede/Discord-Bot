import discord
from discord.ext import commands, tasks
import praw
import os

reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),client_secret=os.getenv("CLIENT_SECRET"),password=os.getenv("PASSWORD"),user_agent="DiscordConnection",username=os.getenv("USERNAME"))
client = discord.Client()
myUserId = 458474704001433610       #User id from discord, enable developer mode to see id's
serverId = 592892913004969985
subredditArray = []
started = False
messageChannel = 0

#CODE FOR REDDIT POSTS
@client.event
async def on_connect():
    print('Bot has infiltrated servers ÒwÓ')

@client.event
async def on_disconnect():
    print("Disconnected")

@client.event
async def on_ready():
    # Check to see if file exists
    # Read subreddits from file
    # Add subreddits to subredditArray
    # Close file
    global started
    global messageChannel
    if started is False:
        if path.exists("serverChannels.csv") is False:
            started = True
            for item in subredditArray:
                subreddit = reddit.subreddit(item)
                for submission in subreddit.stream.submissions():
                    if submission.is_self == False:
                        embed = discord.Embed(url="https://reddit.com/r/" + item + "/comments/" + str(submission),title=submission.title)
                        embed.add_field(name="Subreddit",value=subreddit.display_name)
                        embed.set_image(url=submission.url)
                        await messageChannel.send(embed=embed)
                        print("Link posted")
                        await asyncio.sleep(8)
                    else:
                        embed = discord.Embed(url=submission.url,title=submission.title)
                        await messageChannel.send(embed=embed)
                        print("Link posted")
                        await asyncio.sleep(8)
            
@client.event
async def on_message(message):
    # !add /r/pics
    # Open/ create file
    # Add new subreddit to file (Comma separated CSV)
    # Save file with new subreddit
    global messageChannel
    if message.content.startswith("!register"):
        if path.exists("serverChannels.csv") == False:
            with open ("serverChannels.csv",mode='x') as subredditFile:
                subredditWriter = csv.writer(subredditFile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                subredditWriter.writerow([message.content.split()[1]])
                subredditFile.close()
            await on_ready()
        else:
            with open ("serverChannels.csv",mode='a',newline='\n') as subredditFile:
                subredditWriter = csv.writer(subredditFile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                subredditWriter.writerow([message.content.split()[1]])
                subredditFile.close()
            await on_ready()
 
        
    if message.content.startswith("!channel"):
        for channel in client.get_allChannels():
            if channel.name == message.content.split()[1]:
                messageChannel = channel
                await on_ready()
    
    if message.content.startswith("!delete"):
        deleteRow = []
        with open ("serverChannels.csv",mode='r') as SubredditFile:
            reader = csv.reader(SubredditFile)
            for row in reader:
                deleteRow.append(row)
                for field in row:
                    if field == message.content.split()[1]:
                        deleteRow.remove(row)
        with open ("serverChannels.csv",mode='w') as SubredditFile:
            subredditWriter = csv.writer(SubredditFile)
            subredditWriter.writerows(deleteRow)
       
client.run(os.getenv("BOT_TOKEN"))
