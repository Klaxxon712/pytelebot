from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

router = Router(name=__name__)

@router.callback_query(F.data == 'back')
async def back(callback: types.CallbackQuery):
    cheat_btn = InlineKeyboardButton(text='👩‍💻 Читы 👩‍💻',callback_data='cheat')
    cfg_btn = InlineKeyboardButton(text='☁️ CFG ☁️',callback_data='cfg')
    tg_channel_btn = InlineKeyboardButton(text='💬 Telegram Channel 💬',url='https://t.me/Sasuukes67')
    youtube_btn = InlineKeyboardButton(text='🎥 YouTube 🎥',url='https://www.youtube.com/@6-7cs')
    row_1 = [youtube_btn]
    row_2 = [tg_channel_btn]
    row_3 = [cheat_btn, cfg_btn] 
    rows = [row_1, row_2, row_3]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await callback.answer()
    await callback.message.edit_text(
        "Добро пожаловать в бот <a href='https://www.youtube.com/@6-7cs'>Sasuukes</a>\nВыберы что-то",
        parse_mode='html',
        reply_markup=markup
    )