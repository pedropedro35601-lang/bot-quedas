import discord, random, os
from discord.ext import commands, tasks

ID_CANAL = 1553497222107103282
ultima_msg = None
videos = [
  "https://youtu.be/hjSWVF6Rjcw?si=puW-ATUaCQQwP0iP",
  "https://youtu.be/ol0y3uYWBlo?si=2pC9c_2glzdwrkS1",
  "https://youtu.be/VJWtoCysWZ4?si=hBoM2OC4iUpTlm_F"
]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@tasks.loop(minutes=60)
async def auto():
    global ultima_msg
    canal = bot.get_channel(ID_CANAL)
    if not canal: return
    if ultima_msg:
        try: await ultima_msg.delete()
        except: pass
    ultima_msg = await canal.send(f"💥 QUEDA CLIPADA 💥\n{random.choice(videos)}")

@bot.event
async def on_ready():
    print("online")
    auto.start()

@bot.command()
async def queda(ctx):
    global ultima_msg
    canal = bot.get_channel(ID_CANAL)
    if ultima_msg:
        try: await ultima_msg.delete()
        except: pass
    ultima_msg = await canal.send(f"💥 QUEDA CLIPADA 💥\n{random.choice(videos)}")

bot.run(os.getenv("TOKEN"))
