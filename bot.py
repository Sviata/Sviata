from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import asyncio
import datetime

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['toast'])
async def process_toast_command(message: types.Message):
    tday = datetime.date.today()

    gazoprovodday = datetime.date(2021, 8, 26) 
    landay = datetime.date(2021, 8, 27) 
    genday = datetime.date(2021, 8, 28)
    
    hayday = datetime.date(1, 1, 1)
    heyday = datetime.date(1, 1, 1)
    
    daone = heyday - hayday
    
    if (gazoprovodday - tday) == daone:
        await message.reply("26 августа в 2009 году был запущен самый высокогорный газопровод «Дзуарикау — Цхинвал». \n\n День рождения у @kindalikemyselfalot! ❤️")
    
    if (landay - tday) == daone:
     await message.reply ("27 августа в 1936 был рожден Лянь Чжань, тайваньский государственный и политический деятель, премьер-министр и вице-президент Китайской Республики (Тайваня).")

    if (genday - tday) == daone:
     await message.reply ("28 августа в 1936 году в Массачусетсе был впервые синтезирован искусственный ген.") 

    if (genday - tday) == daone:
     await message.reply ("29 августа в 1926 году в Непале было отменено рабство.") 

    if (genday - tday) == daone:
     await message.reply ("30 августа в 1954 был рождён Александр Лукашенко, президент Белоруссии с 1994.") 


    if (genday - tday) == daone:
     await message.reply ("31 августа в 1898 официально был открыт Киевский политехнический институт.")     


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здраствуйте!\n\nНастоятельно рекомендуем больше не трогать ничего.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Сами себе помогите.")



if __name__ == '__main__':
    executor.start_polling(dp)