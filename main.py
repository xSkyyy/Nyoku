from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")
TOKEN = "NzQ1NjIzMDI5ODIzOTYzMjU2.Xz0djw.bUmwBi34rsadpcDOG1gWpoWmMdk"


@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

## this embed no worky innit

## @bot.command()
## async def last(ctx):
## 	last = discord.Embed("[USER](https://nekos.cc/u/1000?mode=0).",color=0x0000ff)
## 	last.description = f"[USER](https://nekos.cc/u/1000?mode=0)."
## 	last.add_field(name="Field2", value="hi2", inline=True)
## 	last.add_field(name="Field2", value="hi2", inline=True)
## 	last.set_image(url="https://assets.ppy.sh/beatmaps/1/covers/cover.jpg")
## 	await ctx.send(embed=last)

## the commands below are boring lol

@bot.command()
async def hi(ctx):
    await ctx.send('whats up twat')


@bot.command()
async def cum(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/797469159403421774.png')

@bot.command()
async def sex(ctx):
    await ctx.send('go back to the gc!! https://i.redd.it/cah38y4p41f51.png')

@bot.command()
async def lolis(ctx):
    await ctx.send('https://media.very.co.uk/i/very/MFWPY_SQ1_0000000099_N_A_SLf?$550x733_standard$')

@bot.command()
async def women(ctx):
    await ctx.send('https://image.emojipng.com/54/12456054.jpg')


@bot.command()
async def nekosu(ctx):
  await ctx.send('Pls play nekosu i am desperate https://nekos.cc/')

@bot.command()
async def cookiezi(ctx):
  await ctx.send('Check if Cookiezi is up here: https://c.cookiezi.gay')

## end of boring commands and the start of the embeds

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="we do a little trolling", url="https://nekos.cc/", description="This is a sample embed. If you are seeing this matty actually did something right", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def catboy(ctx):
  await ctx.send('https://media.japanesewithanime.com/uploads/cat-boy-re-zero.jpg')

bot.run(TOKEN)
