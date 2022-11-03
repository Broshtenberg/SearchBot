from config import bot
import aiogram
from aiogram.filters.command import Command
from aiogram import Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import add_user, check_user
from keyboards.parsing import create_main_menu
start_router = Router()


class Search(StatesGroup):
    chat_title = State()


@start_router.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    if not check_user(message):
        add_user("parser", message)
    await bot.send_message(message.from_user.id, "Выбери что нужно сделать:", reply_markup=create_main_menu())
