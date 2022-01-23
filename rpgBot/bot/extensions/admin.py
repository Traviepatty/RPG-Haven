import lightbulb

from rpgBot.bot import Bot

plugin = lightbulb.Plugin("Admin")

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only )
@lightbulb.command(name = "shutdown", description = "Gracefully shuts down RPG Bot", aliases = ("sd"))
@lightbulb.implements(lightbulb.PrefixCommand)
async def shutdown_cmd(ctx) -> None:
    await ctx.respond("Shutting down...")
    await ctx.bot.close()
        
def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)