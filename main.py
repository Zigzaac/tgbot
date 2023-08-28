import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

API_TOKEN = "6032356369:AAGvd9aNomdcpG__PGsHxttGV4sWI4FxbIk"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


choosebut = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = 'Рекомендовать клиента'
but2 = 'Записаться на консультацию'
choosebut.add(but1).add(but2)



@dp.message_handler(commands=['start', 'help'])
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nЭто бот компании <b>RING estate</b>\nКак я могу к вам обращаться?", reply_markup="", parse_mode='HTML')




@dp.message_handler(regexp='^[а-яА-Я]*$')
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, f"{message.text} выберите что вы хотите сделать?", reply_markup="choosebut", parse_mode='HTML')






    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

