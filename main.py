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


@dp.message_handler(commands=['backup_cur'])
async def backup(message: types.Message):
    subprocess.call("rm /home/ureshipan/Yandex.Disk/Color_Study/Backup/*", shell=True) #Чистим папку
    subprocess.call("cp -a /home/ureshipan/Yandex.Disk/Color_Study/Current_Run/* /home/ureshipan/Yandex.Disk/Color_Study/Backup/", shell=True) #Кидаем текущую версию в бек
    #subprocess.call("cp /home/ureshipan/Yandex.Disk/Color_Study/Backup/* /home/ureshipan/Yandex.Disk/Color_Study/Current_Run", shell=True) #Возвращаем из бека копию в лайв
    #Буквально пишем баш команды через интерфейс этой библы



# Пример функции, которая принимает любой текст и отправляет его же собеседнику
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
