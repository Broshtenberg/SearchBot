from aiogram import Router, types
from aiogram.filters.text import Text
from config import bot
from keyboards.parsing import create_main_menu, create_parse_menu, create_parse_members_menu

menu_router = Router()


@menu_router.callback_query(Text(text="main_menu"))
async def show_main_menu(callback: types.CallbackQuery):
    await bot.edit_message_text("Главное меню", callback.from_user.id, callback.message.message_id,
                                reply_markup=create_main_menu())


@menu_router.callback_query(Text(text="parsing"))
async def show_parsing_menu(callback: types.CallbackQuery):
    await bot.edit_message_text("Меню парсинга", callback.from_user.id, callback.message.message_id,
                                reply_markup=create_parse_menu())


@menu_router.callback_query(Text(text="parsing_menu"))
async def show_parsing_menu(callback: types.CallbackQuery):
    await bot.edit_message_text("Меню парсинга", callback.from_user.id, callback.message.message_id,
                                reply_markup=create_parse_members_menu())
