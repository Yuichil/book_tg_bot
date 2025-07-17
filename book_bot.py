import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from fsm import fsm_router
from handlers.callbacks import callbacks_router
from handlers.commands import command_router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
storage = MemoryStorage()

dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(callbacks_router)
dp.include_router(fsm_router)

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
