import lightbulb

from rpgBot.bot import Bot

plugin = lightbulb.Plugin("Admin")

@lightbulb.check(lightbulb.owner_only)
@lightbulb.command("shutdown", "Gracefully shuts down RPG Bot", aliases = ("sd"))
async def shutdown_cmd(self, ctx: lightbulb.Context) -> None:
    await ctx.message.delete()
    await ctx.respond("Shutting down...")
    await self.bot.close()
        
def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)