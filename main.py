import asyncio
from config.config import *
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from Core.Config import *
from Core.Run import *
from admin import router as adm
from user import router as user
from callback import router as cs 

bot = Bot(TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(adm, user, cs)
    

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())