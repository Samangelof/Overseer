import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from core.handlers import common, report, status, rules, rules_stats, relapse


logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        common.router,
        report.router,
        status.router,
        rules.router,
        rules_stats.router,
        relapse.router,

    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
