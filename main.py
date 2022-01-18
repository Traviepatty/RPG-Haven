import lightbulb, math, random, test
from secrets import token1, ID1

bot = lightbulb.BotApp(
    token = token1,
    default_enabled_guilds=(ID1),
    prefix = '$',
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
async def help(ctx):
    await ctx.respond(HELP_MESSAGE)
    
@bot.command
@lightbulb.option('modifier','add or subtracts from the original roll')
@lightbulb.option('op','add or sub')
@lightbulb.option('sides', 'sides on the die')
@lightbulb.command('r', 'rolls a set of dice')
@lightbulb.implements(lightbulb.PrefixCommand)
async def roll(ctx):
    sides = ctx.options.sides
    op = ctx.options.op
    mod = ctx.options.modifier
    sides = sides.split('d')
    if mod == '':
        mod = '0'
    if sides[0] == '':
        sides[0] = '1'
    if op == '-':
        mod = int(mod)
        mod = 0 - mod
    else:
        mod = int(mod)

    totalDice = int(sides[0])
    sides = int(sides[1])
    outcomes = [random.randint(1,sides) for i in range(totalDice)]
    outcome = int(math.fsum(outcomes))
    total = outcome + mod
    
    await ctx.respond(f"{total}") 

bot.run()