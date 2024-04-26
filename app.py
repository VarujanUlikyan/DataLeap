import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
# from aiogram.types import BotCommand, BotCommandScopeDefault

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from common.bot_cmd_list import private

ALLOWED_UPDATES = ['message, edited_message']
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    logging.basicConfig(level=logging.INFO)
    
if __name__ == "__main__":
    asyncio.run(main())