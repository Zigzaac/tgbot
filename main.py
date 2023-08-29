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


choosebut = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = 'Рекомендовать клиента и получить до 100 тыс руб'
but2 = 'Записаться на консультацию'
choosebut.add(but1).add(but2)

class Ring(StatesGroup):
    name = State()
    number = State()
    client_number = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nЭто бот компании <b>RING estate</b>\nКак я могу к вам обращаться?", reply_markup="", parse_mode='HTML')
    await Ring.name.set()

@dp.message_handler(state=Ring.name)
async def radius(message: types.Message, state: FSMContext):
    global name
    name = message.text
    await bot.send_message(message.from_user.id, f"{message.text}, выберите что вы хотите сделать?", reply_markup=choosebut, parse_mode='HTML')
    await state.finish()


    
@dp.message_handler(lambda message:'рекомендовать' in message.text.lower())
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, "Укажите номер телефона клиента", reply_markup=types.ReplyKeyboardRemove(), parse_mode='HTML')
    await Ring.client_number.set()


@dp.message_handler(lambda message:'записаться' in message.text.lower())
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, "Введите свой номер и тогда наш менедджер свяжется с вами", reply_markup=types.ReplyKeyboardRemove(), parse_mode='HTML')
    await Ring.number.set()

@dp.message_handler(state=Ring.number)
async def radius(message: types.Message, state: FSMContext):
    number = message.text
    await bot.send_message(message.from_user.id, "Спасибо за оставленную заявку, наш менеджер свяжется с вами", reply_markup="", parse_mode='HTML')
    await state.finish()
    await bot.send_message(1995228159, f"Пользователь {name} с номером {number} оставил заявку", reply_markup="", parse_mode='HTML')



@dp.message_handler(state=Ring.client_number)
async def radius(message: types.Message, state: FSMContext):
    global client_number
    client_number = message.text
    await bot.send_message(message.from_user.id, "Спасибо за вашу отзывчивость,с клиентом обязательно свяжется наш менеджер, вы обязательно будете отблагодарены", reply_markup="", parse_mode='HTML')
    await state.finish()
    try:
        await bot.send_message(1995228159, f"Пользователь {name} пригласил клиента с номером {client_number}", reply_markup="", parse_mode='HTML')
    except:
        print("not work")





    

if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
