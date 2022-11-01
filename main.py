from config import bot, dp
from handlers.commands.start import start_router
import asyncio


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


asyncio.run(main())
