import logging
import subprocess #Чтобы взаимодействовать с bash консолью линукса
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6070379081:AAGrYcJlgTrVuoVAeRJjvHZjPwbxqSjfvJI' #тестить здесь @PrjctServerControllerBot

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Пример функции, которая обрабатывает команды
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# Пример функции, которая принимает любой текст и отправляет его же собеседнику
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(commands=['/backup_cur'])
async def backup(message: types.Message):
    subprocess.call("mv Current_Run/* Backup", shell=True)
    subprocess.call("cp Backup/* Current_Run", shell=True)
    #Буквально пишем баш команды через интерфейс этой библы

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
