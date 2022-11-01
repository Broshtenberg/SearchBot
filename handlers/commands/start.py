from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
storage = MemoryStorage()
TOKEN = "5553100526:AAHucm9HTtDsKmYz6N46H_e3usNX7e7Dc-M"
bot = Bot(TOKEN)
dp = Dispatcher(storage=storage)