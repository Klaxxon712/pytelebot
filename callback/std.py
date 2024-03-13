from aiogram import Router,F
from aiogram.types import  Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from Core.Config import *
from Core.Run import *

router = Router(name=__name__)

class AttackStates(StatesGroup):
    NUMBER = State()
    ROUNDS = State()

    
@router.callback_query(F.data == 'std_1')
async def std_1(message: Message, state: FSMContext):
    phone_number = '998990000849'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
    
@router.callback_query(F.data == 'std_2')
async def std_2(message: Message, state: FSMContext):
    phone_number = '998997663420'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    

@router.callback_query(F.data == 'std_3')
async def std_3(message: Message, state: FSMContext):
    phone_number = '998977031669'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_4')
async def std_4(message: Message, state: FSMContext):
    phone_number = '998974555582'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)

@router.callback_query(F.data == 'std_5')
async def std_5(message: Message, state: FSMContext):
    phone_number = '998917753237'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_6')
async def std_6(message: Message, state: FSMContext):
    phone_number = '998909015900'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_7')
async def std_7(message: Message, state: FSMContext):
    phone_number = '998998912047'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_8')
async def std_8(message: Message, state: FSMContext):
    phone_number = '998900273861'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)

@router.callback_query(F.data == 'std_9')
async def std_9(message: Message, state: FSMContext):
    phone_number = '998971181908'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)

@router.callback_query(F.data == 'std_10')
async def std_10(message: Message, state: FSMContext):
    phone_number = '998977026648'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)

@router.callback_query(F.data == 'std_11')
async def std_11(message: Message, state: FSMContext):
    phone_number = '998946062785'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)

@router.callback_query(F.data == 'std_12')
async def std_12(message: Message, state: FSMContext):
    phone_number = '998933863170'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_13')
async def std_13(message: Message, state: FSMContext):
    phone_number = '998930783080'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_14')
async def std_14(message: Message, state: FSMContext):
    phone_number = '998908082235'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_15')
async def std_15(message: Message, state: FSMContext):
    phone_number = '998998867519'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_16')
async def std_16(message: Message, state: FSMContext):
    phone_number = '998909789057'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_17')
async def std_17(message: Message, state: FSMContext):
    phone_number = '998970021735'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_18')
async def std_18(message: Message, state: FSMContext):
    phone_number = '998998314967'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_19')
async def std_19(message: Message, state: FSMContext):
    phone_number = '998977036993'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_20')
async def std_20(message: Message, state: FSMContext):
    phone_number = '998938625545'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_21')
async def std_21(message: Message, state: FSMContext):
    phone_number = '998901162533'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_22')
async def std_22(message: Message, state: FSMContext):
    phone_number = '998990128844'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_23')
async def std_23(message: Message, state: FSMContext):
    phone_number = '998908065156'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_24')
async def std_24(message: Message, state: FSMContext):
    phone_number = '998901299697'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_25')
async def std_25(message: Message, state: FSMContext):
    phone_number = '998950668085'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    
@router.callback_query(F.data == 'std_26')
async def std_26(message: Message, state: FSMContext):
    phone_number = '998909326686'
    await state.update_data(phone_number=phone_number)
    await message.answer("Введите количество кругов (от 1 до 50):")
    await state.set_state(AttackStates.ROUNDS)
    