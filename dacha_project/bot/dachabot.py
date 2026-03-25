# bot/bot.py
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.environ.get("Telegram_token")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
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
    await msg.answer("123", reply_markup=kb)
