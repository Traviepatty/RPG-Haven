import lightbulb

from rpgBot.bot import Bot

plugin = lightbulb.Plugin("Meta")    
    
@plugin.command
@lightbulb.command("ping", "Get the average DWSP latency for the bot.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_ping(ctx: lightbulb.PrefixContext) -> None:
    await ctx.respond(
        f"Latency: {ctx.bot.heartbeat_latency * 1_000:,.0f} ms."
    )
    

    
def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)