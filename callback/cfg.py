from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

router = Router(name=__name__)

@router.callback_query(F.data == 'cfg')
async def cfg(callback: types.CallbackQuery):
    rage_btn = InlineKeyboardButton(text='Rage cfg', url='https://oxy.st/d/OZJh')
    legit_btn = InlineKeyboardButton(text='legit cfg', url='https://oxy.st/d/PZJh')
    back_btn = InlineKeyboardButton(text='↩️ Back ↩️', callback_data='back')
    row_1 = [rage_btn]
    row_2 = [legit_btn]
    row_3 = [back_btn]
    rows = [row_1, row_2, row_3]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await callback.answer()
    await callback.message.edit_text(text='<b>Вы выбрали CFG</b>',parse_mode='html' , reply_markup=markup)