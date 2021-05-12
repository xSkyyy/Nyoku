from discord.ext import commands
import discord, nekos, var, config, random, datetime, os

bot = commands.Bot(command_prefix=config.prefix)
TOKEN = config.token

@bot.event
async def on_ready():
    os.system('clear')
    print('\n\x1b[35m ███╗   ██╗██╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗');
    print('\x1b[95m ████╗  ██║╚██╗ ██╔╝██╔═══██╗██║ ██╔╝██║   ██║');
    print('\x1b[35m ██╔██╗ ██║ ╚████╔╝ ██║   ██║█████╔╝ ██║   ██║');
    print('\x1b[95m ██║╚██╗██║  ╚██╔╝  ██║   ██║██╔═██╗ ██║   ██║');
    print('\x1b[35m ██║ ╚████║   ██║   ╚██████╔╝██║  ██╗╚██████╔╝');
    print('\x1b[95m ╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝')
    print(f'\x1b[35m\n Logged in as {bot.user}\n\x1b[0m')

## this embed no worky innit

## @bot.command()
## async def last(ctx):
## 	last = discord.Embed("[USER](https://nekos.cc/u/1000?mode=0).",colour=0x0000ff)
## 	last.description = f"[USER](https://nekos.cc/u/1000?mode=0)."
## 	last.add_field(name="Field2", value="hi2", inline=True)
## 	last.add_field(name="Field2", value="hi2", inline=True)
## 	last.set_image(url="https://assets.ppy.sh/beatmaps/1/covers/cover.jpg")
## 	await ctx.send(embed=last)

## the commands below are boring lol

@bot.command()
async def hi(ctx):
    await ctx.send('whats up twat')

## @bot.command()
## async def cum(ctx):
##     await ctx.send('https://cdn.discordapp.com/emojis/797469159403421774.png')

@bot.command()
async def sex(ctx):
    await ctx.send('go back to the gc!! https://i.redd.it/cah38y4p41f51.png')

@bot.command()
async def lolis(ctx):
    await ctx.send('https://media.very.co.uk/i/very/MFWPY_SQ1_0000000099_N_A_SLf?$550x733_standard$')

@bot.command()
async def women(ctx):
    await ctx.send('https://image.emojipng.com/54/12456054.jpg')

## @bot.command()
## async def nekosu(ctx):
##   await ctx.send('Pls play nekosu i am desperate https://nekos.cc/')

## @bot.command()
## async def cookiezi(ctx):
##   await ctx.send('Check if Cookiezi is up here: https://c.cookiezi.gay')

## end of boring commands and the start of the embeds

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="we do a little trolling", url="https://nekos.cc/", description="This is a sample embed. If you are seeing this matty actually did something right", colour=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def nekosu(ctx):
    embed=discord.Embed(title="Nekosu!", url="https://nekos.cc/", description="Nekosu! is an osu! private server basically based around catboys/catgirls. We also praise Astolfo", colour=0xfc03df)
    await ctx.send(embed=embed)

@bot.command()
async def cookiezi(ctx):
    embed=discord.Embed(title="osu!Cookiezi", url="https://cookiezi.gay/", description="osu!Cookiezi is matty's secondary server that runs gulag instead of ripple. This server is considered to be less important so won't get updates very often and there's no guarantee that it will always work. This server is the first dedicated cheating server running on Gulag.", colour=0xfc03df)
    await ctx.send(embed=embed)

@bot.command()
async def source(ctx):
    embed=discord.Embed(title="Nyoku source code!", url="https://github.com/mattylive/Nyoku", description="Linked above is the full Nyoku source code (usually kept up to date with the production code)", colour=0xfc03df)
    await ctx.send(embed=embed)

@bot.command()
async def catboy(ctx):
    embed=discord.Embed(title="Catboy", url="https://cdn.donmai.us/sample/ac/d4/sample-acd4d3388360a9b5a1bcd860a25bd438.jpg", description="Enjoy this catboy image")
    embed.set_image(url="https://cdn.donmai.us/sample/ac/d4/sample-acd4d3388360a9b5a1bcd860a25bd438.jpg")
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

@bot.command()
async def catgirl(ctx):
    embed=discord.Embed(title="Catgirl", url="https://nekos.life/", description="Not as good as catboys but still coot :3")
    embed.set_image(url=(nekos.img('neko')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

@bot.command()
async def pp(ctx):
    embed = discord.Embed(title="PEEPEE SIZE MACHINE", color=0xfc03df)
    embed.add_field(name=ctx.message.author.name + "'s pp size is:", value=" 8{}D".format(random.choice(var.ppSizes)), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def roll(ctx):
    embed = discord.Embed(title=":game_die: Roll the die.", color=0xfc03df)
    embed.add_field(name=ctx.message.author.name + "'s, roll:", value="{}".format(random.randint(var.minimum, var.maximum)), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ball(ctx):
    embed = discord.Embed(title=ctx.message.author.name + " asked: " + ctx.message.content[6:], description=":8ball: | " + random.choice(var.ball), color=0xfc03df)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx):
    embed = discord.Embed(color=0xfc03df, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.author.name, url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
    embed.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def blush(ctx):
    embed = discord.Embed(title=":two_hearts: " + ctx.message.author.name + " is blushing... awww!" , color=0xfc03df, timestamp=datetime.datetime.utcnow())
    embed.set_image(url="{}".format(random.choice(var.blushGifs)))
    await ctx.send(embed=embed)


@bot.command()
async def feet(ctx):
    embed=discord.Embed(title="Feet :flushed:", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="why did i make this - Matty 2021")
    embed.set_image(url=(nekos.img('feet')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

@bot.command()
async def trap(ctx):
    embed=discord.Embed(title="Traps", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="You have good taste")
    embed.set_image(url=(nekos.img('trap')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

@bot.command()
async def nsfwgif(ctx):
    embed=discord.Embed(title="Nsfw Neko Gif", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="it moves :flushed:")
    embed.set_image(url=(nekos.img('nsfw_neko_gif')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)   
    
    
@bot.command()
async def pat(ctx):
    embed=discord.Embed(title="Headpats", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="How cute :pleading_face:")
    embed.set_image(url=(nekos.img('pat')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)


@bot.command()
async def cum(ctx):
    embed=discord.Embed(title="Cum", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="Yummy cummies :yum:")
    embed.set_image(url=(nekos.img('cum')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)
    
@bot.command()
async def doggo(ctx):
    embed=discord.Embed(title="Doggo", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="Woof woof :3")
    embed.set_image(url=(nekos.img('woof')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)
    
@bot.command()
async def fox(ctx):
    embed=discord.Embed(title="Fox girl", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="Fox girls are cute :pleading_face:")
    embed.set_image(url=(nekos.img('fox_girl')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)
      
@bot.command()
async def cat(ctx):
    embed=discord.Embed(title="Cat", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="Cats are adorable :3")
    embed.set_image(url=(nekos.cat()))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

@bot.command()
async def cuddle(ctx):
    embed=discord.Embed(title="Cuddles", url="https://github.com/Nekos-life/nekos.py/blob/master/nekos/nekos.py#L18", description="so soft :pleading_face:")
    embed.set_image(url=(nekos.img('cuddle')))
    embed.set_author(name="Nyoku", url='https://nekos.cc/Nyoku', icon_url='https://a.nekos.cc/1689')
    await ctx.send(embed=embed)

bot.run(TOKEN)
