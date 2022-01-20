from __future__ import annotations

import logging
from pathlib import Path

import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone, utc 

class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self.extensions = [p.stem for p in Path(".").glob("./rpgBot/bot/extensions/*.py")]
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone = utc)
        
        super().__init__(
            prefix="-",
            case_insensitive_prefix_commands=True,
            
        )
        
    def setup(self) -> None:
        for ext in self.extensions:
            self.load_extensions(f"rpgBot.bot.extensions.{ext}")
            logging.info(f"{ext} extension loaded")
            
    def run(self) -> None:
        self.setup()
        super().run(
            
        )
        