"""Ball Controll Bot"""

from __future__ import annotations
from typing import NoReturn
import asyncio

from core import Bot, Reporter
from model.status import BotStatusQueue

class Main:
    """Main"""

    def __init__(self) -> None:
        self.status_queue = BotStatusQueue()

        self.bot = Bot(self.status_queue)
        self.reporter = Reporter(self.status_queue)

    async def run(self) -> NoReturn:
        """run bot and reporter"""
        asyncio.gather(self.bot.run(), self.reporter.run())


if __name__ == "__main__":
    asyncio.run(Main().run())
