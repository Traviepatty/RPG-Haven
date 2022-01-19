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
@lightbulb.option('modifier','add or subtracts from the original roll', required=False)
@lightbulb.option('op','add or sub', required=False)
@lightbulb.option('sides', 'sides on the die')
@lightbulb.command('r', 'rolls a set of dice')
@lightbulb.implements(lightbulb.PrefixCommand)
async def roll(ctx):
    sides, op, mod = ctx.options.sides, ctx.options.op, ctx.options.modifier
    sides = sides.split("d")
    tDice = sides[0]
    tSides = sides[1]

    if mod == "": mod = 0
    if op == "-":
        mod = 0 - mod
    elif op == "":
        op = "+"
    else:
        pass
    if tDice == "": tDice = "1"
    
    tDice,tSides = int(tDice),int(tSides)
    tRoll = [random.randint(1,tSides) for i in range(tDice)]
    tRoll1 = int(math.fsum(tRoll))
    total = tRoll1 + mod
    
    await ctx.respond(f"{total}") 

#@bot.command
#@lightbulb.option('sides', 'sides on a die')
#@lightbulb.command('roll','rolls a single die')
#@lightbulb.implements(lightbulb.PrefixCommand)
#async def roll1(ctx):
#    sides = ctx.options.sides
#    sides = sides.split('d')
#    if sides[0] == '':
#        sides[0] = '1'
#    tSides = sides[1]
#    dice = sides[0]
#    tSides = int(tSides)
#    dice = int(dice)
#
#    outcome = [random.randint(1,tSides) for i in range(dice)]
#    
#    await ctx.respond(f"{outcome}")

bot.run()