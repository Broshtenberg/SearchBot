from config import bot, dp
import aiogram
from aiogram.filters.command import Command
from aiogram import Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

start_router = Router()


class Search(StatesGroup):
    chat_title = State()


@start_router.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Search.chat_title)
    await bot.send_message(chat_id=message.from_user.id, text="Введи название чата/канала")
    await state.set_state(Search.chat_title)


@start_router.message(Search.chat_title, aiogram.F.text)
async def proceed_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    search_input = await state.get_data()
    print(search_input)
