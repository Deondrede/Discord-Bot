import discord
from datetime import date
from pathlib import WindowsPath

lostSectors = []
client = discord.Client()
lostSectorFile = open(WindowsPath("C:/Users/deond/OneDrive/Documents/Python Scripts/lostsectors.tsv"))

for line in lostSectorFile:
    legendsector,mastersector = line.split("\t",1)
    lostSectors.append((legendsector,mastersector))

@client.event
async def on_ready():
    print("Bot is ready to shitpost")

@client.event
async def on_message(message):
    if "!lostsector" in message.content:
        arrayIndex = (date.today() - date(2020, 11, 11)).days
        await message.channel.send("```Legend: " + lostSectors[arrayIndex][0] + "\nMaster: " + lostSectors[arrayIndex][1] + "```")

client.run('NTkyODgyOTU4NDc4ODY4NDkx.Xw0ogA.CQGRSo9uLFouc5ZbgmjdSB_ftcs')
