# bot/bot.py
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Загружаем токен
load_dotenv('../.env')  # путь к .env
TOKEN = os.environ.get("Telegram_token")
bot = Bot(token=TOKEN)
dp = Dispatcher()

print("TOKEN =", TOKEN)  # проверка токена


# Правильный хэндлер для команды /start
@dp.message(Command("start"))
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏠 Главная")],
            [KeyboardButton(text="ℹ️ Информация")],
            [KeyboardButton(
                text="Найти дачу",
                web_app=WebAppInfo(url="https://dacha-finder.onrender.com")
            )]
        ],
        resize_keyboard=True
    )
    await msg.answer("Привет! Я работаю ✅", reply_markup=kb)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
