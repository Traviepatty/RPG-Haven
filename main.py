import lightbulb, asyncio, random, time
from secrets import token1, ID1

bot = lightbulb.BotApp(
    token = token1,
    default_enabled_guilds=(ID1),
    prefix = '+',
    help_class = None
)

HELP_MESSAGE = """
Commands Available:
`Ping` - says Pong!
`help` - Gets list of Commands.
"""

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    await ctx.respond('Pong!')
    
@bot.command
@lightbulb.command('help', 'Gets list of Commands')
@lightbulb.implements(lightbulb.PrefixCommand)
async def Help(ctx):
    await ctx.respond(HELP_MESSAGE)
    

bot.run()