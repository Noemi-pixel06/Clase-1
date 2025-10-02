import discord
from discord.ext import commands
import os, random, requests, io

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def meme(ctx):
    try:
        img_list = os.listdir("images")
        if not img_list:
            await ctx.send("No hay imágenes en la carpeta 'images'.")
            return

        img_name = random.choice(img_list)

        with open(f"images/{img_name}", "rb") as archivo:
            picture = discord.File(archivo)

        await ctx.send(file=picture)

    except FileNotFoundError:
        await ctx.send("La carpeta 'images' no existe.")
    except Exception as e:
        await ctx.send(f"Ocurrió un error: {str(e)}")

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url).json()
    image_url = res["url"]

    image_data = requests.get(image_url).content
    file = discord.File(io.BytesIO(image_data), filename="duck.jpg")
    return file

@bot.command()
async def duck(ctx):
    await ctx.send(file=get_duck_image_url())

bot.run("token")
