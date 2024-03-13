from aiogram import Router, F
from aiogram.types import  Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from Core.Config import *
from Core.Run import *

router = Router(name=__name__)

class AttackStates(StatesGroup):
    NUMBER = State()
    ROUNDS = State()
    
@router.callback_query(F.data == 'tech_1')
async def attack_1(message: Message, state: FSMContext):
    phone_number = '998930067080'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'tech_2')
async def attack_2(message: Message, state: FSMContext):
    phone_number = '998900136603'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'tech_3')
async def attack_3(message: Message, state: FSMContext):
    phone_number = '998903596399'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'tech_4')
async def attack_4(message: Message, state: FSMContext):
    phone_number = '998977690029'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'tech_5')
async def attack_4(message: Message, state: FSMContext):
    phone_number = '998333552524'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'tech_6')
async def attack_4(message: Message, state: FSMContext):
    phone_number = '998935628778'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)