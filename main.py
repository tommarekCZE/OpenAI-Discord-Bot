import discord
from discord.ext import commands
import time
import datetime
import requests
import random
import openai



DCtoken = ''
AItoken = ''
DCtokenTest = ''

OwnerID = ''

openai.api_key = AItoken

prefix = "."

txtmodels=['text-davinci-003']

intents = discord.Intents.default()
intents.message_content = True

def getfilter():
    fileobj=open("inawords.txt")
    lines=[]
    for line in fileobj:
        lines.append(line.strip())

    badwords_normal = lines

    print(f"Inappropriate filter file loaded")

    upper_case_badwords = [word.upper() for word in badwords_normal]

    lower_case_badwords = [word.lower() for word in badwords_normal]

    badwords = badwords_normal + upper_case_badwords + lower_case_badwords

    return(badwords)

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
client = bot

class CustomException(Exception):
    """Your request contain inappropriate content!"""

@bot.event
async def on_ready():
    print("Ready")
    #await Bot.activity
    #bot.change_presence(status=discord.Status.idle, activity=game)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Prefix: '.' / .help"))

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000, 1)
    await ctx.send(f"Pong! {latency}ms")

"""
@bot.command()
async def Rfilter(ctx):
    print(ctx.author.id)
    try:
        if ctx.author.id == 691007640007868487:
            fileobj=open("inawords.txt")
            lines=[]
            for line in fileobj:
                lines.append(line.strip())

            badwords_normal = lines

            upper_case_badwords = [word.upper() for word in badwords_normal]

            lower_case_badwords = [word.lower() for word in badwords_normal]

            badwords = badwords_normal + upper_case_badwords + lower_case_badwords
        
            print(f"inappropriate filter file reloaded")
            embed = discord.Embed(title='🛃 Inappropriate Filter 🛃', description='> 🔄 Inappropriate Filter Reloaded 🔄')
            msg = await ctx.reply("", embed=embed)
        else:
            raise CustomException('User id dont match the alowed id')
    except Exception as e:
        embed = discord.Embed(title='🟥 Unknow Error! 🟥', description='>This is staff command!\n>Check if you have permissions')
        embed.set_footer(text=e)
        msg = await ctx.reply("", embed=embed)
        """

@bot.command()
async def maintenance(ctx):
    print(ctx.author.id)
    if ctx.author.id == OwnerID:
        embed = discord.Embed(title='🚧 Maintenance 🚧', description='>Maintenance Mode Enabled!\n>Bot will shutdown soon!')
        msg = await ctx.reply("", embed=embed)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="🚧 Maintenance 🚧"))
        print('Maintenance Mode Enabled!')
        time.sleep(2)
        await client.close()
        print('Bot Offline...')
        quit()
    else:
        embed = discord.Embed(title='❗ Error ❗', description='>You dont have permissions to enable Maintenance')
        msg = await ctx.reply("", embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='❔ Help ❔', description='> :one: .ask *Content* | Reply to Content\n> :two: .img *Content* | Create images with requested content\n> :three: .imgVar (Attach Picture) | Create different picture with same content')
    msg = await ctx.reply("", embed=embed)

@bot.command()
async def helpSTAFF(ctx):
    embed = discord.Embed(title='🔧 Help 🔧', description='> :one: .maintenance | Shutdown the bot')
    msg = await ctx.reply("", embed=embed)

@bot.command()
async def ask(ctx, *args):
    try:
        if args:
            res = any(ele in " ".join(args[:]) for ele in getfilter())
            if str(res) == "True":
                print(f"Inappropriate content blocked \n")
                raise CustomException('Your request contain inappropriate content!')

            embed = discord.Embed(title='🕐 Awating.... 🕐', description='>Please wait on OpenAI to respond, Thanks \n>You will be mentioned')
            msg = await ctx.reply("", embed=embed)
            response = openai.Completion.create(
                engine=random.choice(txtmodels),
                prompt=" ".join(args[:]),
                max_tokens=3000,
                temperature=0.5,
            )

            channel = discord.utils.get(ctx.guild.channels, name=ctx.channel.name)
            now = datetime.datetime.now()
            print("------------\n>Request: " +" ".join(args[:]) + " \n>Respond: " + response.choices[0].text + f"\n>Time: {str(now)}" + f"\n>Model: {response.model}" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------")
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write("------------\n>Request: " +" ".join(args[:]) + " \n>Respond: " + response.choices[0].text + f"\n>Time: {str(now)}" + f"\n>Model: {response.model}" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------")
            ##await ctx.reply(response.choices[0].text + f"\n(Model {response.model})")
            await msg.delete()
            embed = discord.Embed(title='📜 Generated Text 📜', description=response.choices[0].text)
            embed.set_footer(text=f"Model: {response.model}")
            msg = await ctx.reply("", embed=embed)
        else:
            embed = discord.Embed(title='🟨 Warning 🟨', description='>To your request you dont add the arguments \n>❌ .ask \n>✅ .ask Whats the weather in London?')
            msg = await ctx.reply("", embed=embed)
    except Exception as e:
          embed = discord.Embed(title='🟥 Unknow Error! 🟥', description='>Answer to your question may was too long!\n>Try to remove "Detailed" from your question')
          embed.set_footer(text=e)
          msg = await ctx.reply("", embed=embed)

@bot.command()
async def img(ctx, *args):
    try:
        if args:
            res = any(ele in " ".join(args[:]) for ele in getfilter())
            if str(res) == "True":
                print(f"Inappropriate content blocked \n")
                raise CustomException('Your request contain inappropriate content!')
            
            embed = discord.Embed(title='🕐 Awating.... 🕐', description='>Please wait on OpenAI to respond, Thanks\n>You will be mentioned\n>If your request will be awaited longer than expected, try: Request less difficult image')
            msg = await ctx.reply("", embed=embed)
            response = openai.Image.create(
                prompt=" ".join(args[:]),
                n=1,
                size="1024x1024"
            )

            image_url = response['data'][0]['url']
            ##print(" ".join(args[:]))
            channel = discord.utils.get(ctx.guild.channels, name=ctx.channel.name)
            now = datetime.datetime.now()
            print("------------\n>Request: " +" ".join(args[:]) + " \n>Respond: " + image_url + f"\n>Time: {str(now)}" + "\n>Model: DALLE2-ImageGeneration" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------" )
            with open('log.txt', 'a') as f:
             f.write("------------\n>Request: " +" ".join(args[:]) + " \n>Respond: " + image_url + f"\n>Time: {str(now)}" + "\n>Model: DALLE2-ImageGeneration" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------")
            await ctx.reply(image_url)
            await msg.delete()
        else:
            embed = discord.Embed(title='🟨 Warning 🟨', description='>To your request you dont add the arguments \n>❌ .img \n>✅ .img Dog')
            msg = await ctx.reply("", embed=embed)
    except Exception as e:
         embed = discord.Embed(title='🟥 Unknow Error! 🟥', description='>Image to your Request was generating too long! \n>Try to remove Details from your request')
         embed.set_footer(text=e)
         msg = await ctx.reply("", embed=embed)

@bot.command()
async def imgVar(ctx):
    try:
        if ctx.message.attachments:
            embed = discord.Embed(title='🕐 Awating.... 🕐', description='>Please wait on OpenAI to respond, Thanks \n>You will be mentioned')
            msg = await ctx.reply("", embed=embed)
            attachment = ctx.message.attachments[0]
            img_data = requests.get(attachment.url).content
            with open('ImageGet.png', 'wb') as handler:
                handler.write(img_data)

            response = openai.Image.create_variation(
                image=open('ImageGet.png', 'rb'),
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            channel = discord.utils.get(ctx.guild.channels, name=ctx.channel.name)
            now = datetime.datetime.now()
            print("------------\n>Request: " + attachment.url + " \n>Respond: " + image_url + f"\n>Time: {str(now)}" + "\n>Model: DALLE2-ImageVariations" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------" )
            with open('log.txt', 'a') as f:
             f.write("------------\n>Request: " + attachment.url + " \n>Respond: " + image_url + f"\n>Time: {str(now)}" + "\n>Model: DALLE2-ImageVariations" + "\n>User: " + ctx.author.name + "#" + ctx.author.discriminator + f"\n>User ID: {ctx.author.id}" + "\n>Channel: " +  ctx.channel.name + f"\n>Channel ID: {channel.id}" + f"\n>Server: {ctx.guild.name}" + f"\n>Server ID: {ctx.guild.id}\n------------")
            await ctx.reply(image_url)
            await msg.delete()
        else:
            embed = discord.Embed(title='🟨 Warning 🟨', description='>To your request you dont add the Attachment \n>❌ .imgVar (without Attachment) \n>✅ .img Dog (Added Attachment)')
            msg = await ctx.reply("", embed=embed)
    except Exception as e:
            print(ctx.message.attachments)
            embed = discord.Embed(title='🟥 Unknow Error! 🟥', description='>Check if you add image\n>Check if the image is PNG and have less than 4MB\n>Great works with .img Generated Pictures',)
            embed.set_footer(text=e)
            msg = await ctx.reply("", embed=embed)

bot.run(DCtoken)