from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

load_dotenv()  # загружаем .env
TOKEN = os.environ.get("Telegram_token")

if not TOKEN:
    raise ValueError("TOKEN NOT FOUND")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏠 Главная")],  # первая строка кнопок
            [KeyboardButton(text="ℹ️ Информация")],  # вторая строка кнопок
            [KeyboardButton(
                text="Найти дачу",
                web_app=WebAppInfo(url="https://dacha-finder.onrender.com")
            )]  # третья строка кнопок
        ],
        resize_keyboard=True
    )

    await msg.answer("123", reply_markup=kb)


async def main():
    print("BOT STARTED")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
