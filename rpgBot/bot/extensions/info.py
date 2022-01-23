import lightbulb

from rpgBot.bot import Bot

plugin = lightbulb.Plugin("Info")

@plugin.command
@lightbulb.command('Campaign', 'Displays current campaign Info')
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_Campaign(ctx) -> None:
    title = "   ** \"Princes of the Apocalypse\"**"
    ent_summary =f"""
    {title.center(50)}
    > ```Abolish an ancient evil threatening devastation
    > in this adventure for the world's greatest roleplaying game!
    > Called by the Elder Elemental Eye to serve,
    > four corrupt prophets have risen from the depths of anonymity
    > to claim mighty weapons with direct links to the power of the elemental princes.
    > Each of these prophets has assembled a cadre of cultists and creatures to serve
    > them in the construction of four elemental temples of lethal design.
    > It is up to adventurers from heroic factions such as the Emerald Enclave 
    > and the Order of the Gauntlet to discover where the true power of each prophet lay,
    > and dismantle it before it comes boiling up to obliterate the Realms.```
    """
    
    await ctx.respond(ent_summary)
    


def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)