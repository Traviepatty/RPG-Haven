import lightbulb, random, math

from rpgBot.bot import Bot

plugin = lightbulb.Plugin("Fun") 

@plugin.command
@lightbulb.option('modifier','add or subtracts from the original roll', required=False, default=0)
@lightbulb.option('op','add or sub', required=False, default="+")
@lightbulb.option('sides', 'sides on the die')
@lightbulb.command('r', 'rolls a set of dice', aliases=("roll", "dice"))
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_roll(ctx):
    sides, op, mod = ctx.options.sides, ctx.options.op, ctx.options.modifier
    sides = sides.split("d")
    tDice = sides[0]
    tSides = sides[1]
    
    if op == "-":
        mod = int(mod)
        mod = 0 - mod
    else:
        mod = int(mod)

    if tDice == "": tDice = "1"
    
    tDice,tSides = int(tDice),int(tSides)
    tRoll = [random.randint(1,tSides) for i in range(tDice)]
    tRoll1 = int(math.fsum(tRoll))
    total = tRoll1 + mod
    
    await ctx.respond(" + ".join(str(r) for r in tRoll) + f" + {mod} = {total}")

@plugin.command
@lightbulb.command('randchar', 'rolls stats for a new character')
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_randchar(ctx):
    stats = []
    for i in range(6):
        stat = [random.randint(1,5) for i in range(4)]
        x = stat.index(min(stat))
        stat.pop(x)
        charstat = sum(stat)
        stats.append(charstat)
    await ctx.respond(f"These are your new stats {stats}")


def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)