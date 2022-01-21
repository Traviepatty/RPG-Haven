import os

from rpgBot import __version__
from rpgBot.bot import Bot



if os.name != "nt":
    import uvloop
    uvloop.install()

if __name__ == "__main__":
    bot = Bot()
    bot.run()
    