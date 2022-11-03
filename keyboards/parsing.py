from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


# Main menu has been created
def create_main_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Поиск чатов", callback_data="search"))
    keyboard.add(types.InlineKeyboardButton(text="Парсинг", callback_data="parsing"))
    keyboard.add(types.InlineKeyboardButton(text="Рассылка", callback_data="mailing"))
    keyboard.add(types.InlineKeyboardButton(text="Ивайтинг", callback_data="inviting"))
    keyboard.adjust(2)
    return keyboard.as_markup()


# Parsing Menu created
def create_parse_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Участников чата/группы", callback_data="chat_members"))
    keyboard.add(types.InlineKeyboardButton(text="Участников обсуждений на канале", callback_data="discussion_members"))
    keyboard.add(types.InlineKeyboardButton(text="Назад в Главное меню", callback_data="main_menu"))
    keyboard.adjust(1)
    return keyboard.as_markup()


# Parsing members Menu created
def create_parse_members_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Всех", callback_data="all_members"))
    keyboard.add(types.InlineKeyboardButton(text="Активных", callback_data="active_members"))
    keyboard.add(types.InlineKeyboardButton(text="Авторов сообщений", callback_data="authors"))
    keyboard.add(types.InlineKeyboardButton(text="Админов", callback_data="admins"))
    keyboard.add(types.InlineKeyboardButton(text="Назад в Главное меню", callback_data="main_menu"))
    keyboard.adjust(2)
    return keyboard.as_markup()



