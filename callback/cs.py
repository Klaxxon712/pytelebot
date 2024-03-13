from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

router = Router(name=__name__)

@router.callback_query(F.data == 'cheat')
async def cheats(callback: types.CallbackQuery):
    hpp_v5_btn = InlineKeyboardButton(text='Hpp V5', url='https://oxy.name/d/rZJh')
    hpp_v6_btn = InlineKeyboardButton(text='Hpp V6', url='https://oxy.st/d/sZJh')
    hpp_v5_alt_btn = InlineKeyboardButton(text='Hpp V5 by AltFix', url='https://oxy.st/d/tZJh')
    alternate_btn = InlineKeyboardButton(text='Alternate', url='https://oxy.st/d/wZJh')
    interium_btn = InlineKeyboardButton(text='Interium', url='https://oxy.name/d/vZJh')
    sakura_btn = InlineKeyboardButton(text='Sakura', url='https://oxy.name/d/BZJh')
    skeet_btn = InlineKeyboardButton(text='Skeet', url='https://oxy.st/d/xZJh')
    midnight_btn = InlineKeyboardButton(text='Midnight', url='https://midnight.im/store/chity-cs-1-6/')
    back_btn = InlineKeyboardButton(text='↩️ Back ↩️', callback_data='back')
    row_1 = [hpp_v5_btn, hpp_v5_alt_btn, hpp_v6_btn]
    row_2 = [alternate_btn, skeet_btn,sakura_btn ,interium_btn]
    row_3 = [midnight_btn]
    row_4 = [back_btn]
    rows = [row_1, row_2, row_3, row_4]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await callback.answer()
    await callback.message.edit_text(text='<b>Вы выбрали читы</b>',parse_mode='html' , reply_markup=markup)
    