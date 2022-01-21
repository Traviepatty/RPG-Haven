from __future__ import annotations

import logging
from pathlib import Path

import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone, utc
from rpgBot import __version__


class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self.extensions = [p.stem for p in Path(".").glob("./rpgBot/bot/extensions/*.py")]
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone = utc)
        
        with open("./secrets/token", mode = "r", encoding = "utf-8") as f:
            token = f.read().strip()
        
        super().__init__(
            prefix = "-",
            case_insensitive_prefix_commands = True,
            token = token,
            intents = hikari.Intents.ALL,
        )
        
            
    def run(self) -> None: # type: ignore
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)
        self.event_manager.subscribe(hikari.MessageCreateEvent, self.on_message_create)
        
        super().run(
            activity=hikari.Activity(
                name=f"-help | Version{__version__}",
                type=hikari.ActivityType.WATCHING
            )
        )
        
    async def on_starting(self, event: hikari.StartingEvent) -> None:
        for ext in self.extensions:
            self.load_extensions(f"rpgBot.bot.extensions.{ext}")
            logging.info(f"{ext} extension loaded")
    
    async def on_started(self, event: hikari.StartedEvent) -> None:
        self.scheduler.start()
        logging.info("BOT READY!")
        
    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        self.scheduler.shutdown()
        
    
    async def on_message_create(self, event: hikari.MessageCreateEvent) -> None:
        if isinstance(event.message.channel_id, hikari.DMChannel):
            return        