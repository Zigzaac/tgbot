import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = "6032356369:AAGvd9aNomdcpG__PGsHxttGV4sWI4FxbIk"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# choosebut = ReplyKeyboardMarkup(resize_keyboard=True)
# but1 = 'Рекомендовать клиента'
# but2 = 'Записаться на консультацию'
# choosebut.add(but1).add(but2)

class Ring(StatesGroup):
    name = State()



@dp.message_handler(commands=['start', 'help'])
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nЭто бот компании <b>RING estate</b>\nКак я могу к вам обращаться?", reply_markup="", parse_mode='HTML')
    await Ring.name.set()

@dp.message_handler(state=Ring.name)
async def radius(message: types.Message, state: FSMContext):
    name = message.text
    await bot.send_message(message.from_user.id, f"{message.text}, выберите что вы хотите сделать?", reply_markup="", parse_mode='HTML')
    await state.finish()





# @dp.message_handler(regexp='^[а-яА-Я]*$')
# async def start(message : types.Message):
#     await bot.send_message(message.from_user.id, f"{message.text} выберите что вы хотите сделать?", reply_markup="choosebut", parse_mode='HTML')
#     name = message.text






    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

