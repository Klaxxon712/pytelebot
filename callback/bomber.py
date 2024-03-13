from aiogram import Router,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from .tech import router as tech
from .std import router as std
from Core.Config import *
from Core.Run import *

router = Router(name=__name__)

class AttackStates(StatesGroup):
    NUMBER = State()
    ROUNDS = State()

@router.callback_query(F.data == 'back_1')
async def call_command(call: CallbackQuery, state: FSMContext):
    std = InlineKeyboardButton(text='👨🏻‍🎓 Ученики 👨🏻‍🎓', callback_data='std')
    tech = InlineKeyboardButton(text='👩‍🏫 Учетеля 👩‍🏫', callback_data="tech")
    row = [std]
    row_2 = [tech]
    rows = [row, row_2]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.edit_text("Введите номер без знака '+':", reply_markup=markup)
    await state.set_state(AttackStates.NUMBER)

@router.callback_query(F.data == 'bomber')
async def call_command(call: CallbackQuery, state: FSMContext):
    std = InlineKeyboardButton(text='👨🏻‍🎓 Ученики 👨🏻‍🎓', callback_data='std')
    tech = InlineKeyboardButton(text='👩‍🏫 Учетеля 👩‍🏫', callback_data="tech")
    row = [std]
    row_2 = [tech]
    rows = [row, row_2]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.edit_text("Введите номер без знака '+':", reply_markup=markup)
    await state.set_state(AttackStates.NUMBER)
    

@router.callback_query(F.data =='tech')
async def call_command(call: CallbackQuery, state: FSMContext):
    tech_1 = InlineKeyboardButton(text='Равшан Алишерович',callback_data='tech_1')
    tech_2 = InlineKeyboardButton(text='Эльвира Джанбеквона',callback_data='tech_2')
    tech_3 = InlineKeyboardButton(text='Ольга Георгиевна',callback_data='tech_3')
    tech_4 = InlineKeyboardButton(text='Нигора Эркинбаева',callback_data='tech_4')
    tech_5 = InlineKeyboardButton(text='Динара Собировна',callback_data='tech_5')
    tech_6 = InlineKeyboardButton(text='Алишер Абдурауфович',callback_data='tech_6')
    back_1 = InlineKeyboardButton(text='Back',callback_data='back_1')
    row_1 = [tech_1]
    row_2 = [tech_2]
    row_3 = [tech_3]
    row_4 = [tech_4]
    row_5 = [tech_5]
    row_6 = [tech_6]
    row_back = [back_1]
    rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.answer()
    await call.message.edit_text("Выбери учителя", reply_markup=markup)
    await state.set_state(AttackStates.NUMBER)

@router.callback_query(F.data =='std')
async def call_command(call: CallbackQuery, state: FSMContext):
    std_1 = InlineKeyboardButton(text='Сарвиноз',callback_data="std_1")
    std_2 = InlineKeyboardButton(text='Артур',callback_data="std_2")
    std_3 = InlineKeyboardButton(text='Фазиль',callback_data="std_3")
    std_4 = InlineKeyboardButton(text='Сарвар',callback_data="std_4")
    std_5 = InlineKeyboardButton(text='Нигина',callback_data="std_5")
    std_6 = InlineKeyboardButton(text='Борий',callback_data="std_6")
    std_7 = InlineKeyboardButton(text='Мустаф',callback_data="std_7")
    std_8 = InlineKeyboardButton(text='Шмакова',callback_data="std_8")
    std_9 = InlineKeyboardButton(text='Настя',callback_data="std_9")
    std_10 = InlineKeyboardButton(text='Самир',callback_data="std_10")
    std_11 = InlineKeyboardButton(text='Сагдиана',callback_data="std_11")
    std_12 = InlineKeyboardButton(text='Дильроза',callback_data="std_12")
    std_13 = InlineKeyboardButton(text='Ким',callback_data="std_13")
    std_14 = InlineKeyboardButton(text='Канава',callback_data="std_14")
    std_15 = InlineKeyboardButton(text='Куринова',callback_data="std_15")
    std_16 = InlineKeyboardButton(text='Слава',callback_data="std_16")
    std_17 = InlineKeyboardButton(text='Аделя',callback_data="std_17")
    std_18 = InlineKeyboardButton(text='Данил',callback_data="std_18")
    std_19 = InlineKeyboardButton(text='Умар',callback_data="std_19")
    std_20 = InlineKeyboardButton(text='Камила',callback_data="std_20")
    std_21 = InlineKeyboardButton(text='Судакова',callback_data="std_21")
    std_22 = InlineKeyboardButton(text='Гузель',callback_data="std_22")
    std_23 = InlineKeyboardButton(text='Малик',callback_data="std_23")
    std_24 = InlineKeyboardButton(text='Ибрагим',callback_data="std_24")
    std_25 = InlineKeyboardButton(text='Алишер',callback_data="std_25")
    std_26 = InlineKeyboardButton(text='Муслима',callback_data="std_26")
    back_1 = InlineKeyboardButton(text='Back',callback_data="back_1")
    row_1 = [std_1, std_2, std_3]
    row_2 = [std_4, std_5]
    row_3 = [std_6, std_7, std_8]
    row_4 = [std_9, std_10, std_11, std_12]
    row_5 = [std_13, std_14, std_15]
    row_6 = [std_16, std_17]
    row_7 = [std_18, std_19, std_20]
    row_8 = [std_21, std_22, std_23, std_24]
    row_9 = [std_25, std_26]
    row_back = [back_1]
    rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9,row_back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.answer()
    await call.message.edit_text("Выберити ученика", reply_markup=markup)
    await state.set_state(AttackStates.NUMBER)
    
router.include_router(tech)
router.include_router(std)

@router.message(AttackStates.NUMBER)
async def process_number(message: Message, state: FSMContext):
    if message.text.isdigit() and len(message.text) == 12:
        phone_number = str(message.text)
        await state.update_data(phone_number=phone_number)
        await message.answer("Введите количество кругов (от 1 до 50):")
        await state.set_state(AttackStates.ROUNDS)
    else:
        await message.answer("Введите корректный номер!")

@router.message(AttackStates.ROUNDS)
async def process_rounds(message: Message, state: FSMContext):
    data = await state.get_data()
    phone_number = data.get('phone_number')
    print(phone_number)
    if message.text.isdigit() and 1 <= int(message.text) <= 50:
        num = str(message.text)
        await message.answer("Атака запущена...")
        change_config('attack', 'True')
        try:
            await start_async_attacks(phone_number, num)
        except Exception as e:
            print(e)
        change_config('attack', 'False')
        await message.answer("Атака завершена!")
        await state.clear()
    else:
        await message.answer("Введите корректное количество кругов!")