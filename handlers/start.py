from aiogram import Dispatcher, types
from aiogram.filters import Command

async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Это бот для отзывов о компаниях. Используйте /help для справки.")

async def cmd_help(message: types.Message):
    await message.answer("Команды:\n/start - Начать\n/help - Справка\n/search - Поиск компании\n/review - Оставить отзыв")

def register_start_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command(commands=["start"]))
    dp.message.register(cmd_help, Command(commands=["help"]))
