import os
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Приветствие"), KeyboardButton(text="Локация")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Это свадебный бот 💌", reply_markup=menu)

@router.message(lambda message: message.text == "Приветствие")
async def welcome(message: types.Message):
    await message.answer("Добро пожаловать на нашу свадьбу 💍")

@router.message(lambda message: message.text == "Локация")
async def location(message: types.Message):
    await message.answer(
        "📍 Локации:\n\n"
        "26 июля: Усадьба\n"
        "27 июля: Чернышевка, за точной локацией обратитесь к @nastasia_maslova 💌")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
