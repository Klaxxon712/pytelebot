from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router(name=__name__)

@router.message(Command('adm'))
async def adm(message: types.Message):
    id = message.from_user.id
    if id == 6381777336 or 5400033711:
        btn_bomb = InlineKeyboardButton(text="Бомбер🔝", callback_data='bomber')
        row = [btn_bomb]
        rows = [row]
        markup = InlineKeyboardMarkup(inline_keyboard=rows)
        await message.answer(text=f'Привет {message.from_user.first_name}', reply_markup=markup)