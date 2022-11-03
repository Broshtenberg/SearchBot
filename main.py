from config import bot, dp
from handlers.commands.start import start_router
from handlers.callbacks.menu import menu_router
import asyncio


async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    await dp.start_polling(bot)


asyncio.run(main())
