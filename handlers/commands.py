import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup

from handlers.keyboard import company_about

router=Router()
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    img=FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    text="Assalomu Aleykom PDP Junior botiga xush kelibsiz!"
    await message.answer_photo(photo=img,caption=text, reply_markup=company_about)

