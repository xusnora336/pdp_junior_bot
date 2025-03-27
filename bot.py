import asyncio
from os import getenv
from aiogram import Router, F

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot_menu import set_bot_menu
from handlers.commands import router as commands_router
from handlers.handlers import router as handlers_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(commands_router)
    dp.include_router(handlers_router)
    await set_bot_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot....")
    asyncio.run(main())
