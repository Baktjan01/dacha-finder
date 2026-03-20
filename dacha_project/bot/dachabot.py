from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token="8684459718:AAFZW-a3Iae5BTQ6l82NzUZLr_OJwOQtsvY")
dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton(
            text="Найти дачу",
            web_app=WebAppInfo(url="https://your-site.com")
        )
    )
    await msg.answer("Открой мини приложение:", reply_markup=kb)
