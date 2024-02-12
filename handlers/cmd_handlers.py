import requests
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message
from config import courses

cmd_router = Router()


@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    s = "Assalomu aleykum!\n"
    s += "Valyuta kurslari haqida ma'lumot beruvchi botimizga xush kelibsiz!\n"
    s += "Yordam uchun /help buyrug'ini bosing!"
    await message.answer(text=s)


@cmd_router.message(Command('help'))
async def cmd_help(message: Message):
    s = "Quyidagi komandalar yordamida botdan samarali foydalanishingiz mumkin!\n\n"
    s += "\t/kurslar - valyuta kurslarini bilish\n"
    s += "\t/dollar - dollar kurslarini bilish\n"
    s += "\t/yevro - yevro kurslarini bilish\n"
    s += "\t/rubl - rubl kurslarini bilish\n\n"
    s += "Agar biron summani jo'natsangiz, bot uni turli valyutalardagi qiymatini qaytaradi. (Masalan, 1_000_000)"

    await message.answer(text=s)


@cmd_router.message(Command('kurslar'))
async def cmd_kurslar(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugungi valyuta kurslari: \n"
    for kurs in response.json():
        if kurs['Ccy'] in ["USD","EUR","RUB"]:
            courses[kurs['Ccy']] = float(kurs['Rate'])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
    await message.reply(text=s)


@cmd_router.message(Command('dollar'))
async def cmd_dollar(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugungi dollar kurslari: \n"
    for kurs in response.json():
        if kurs['Ccy'] in ["USD"]:
            courses[kurs['Ccy']] = float(kurs['Rate'])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
    await message.reply(text=s)


@cmd_router.message(Command('yevro'))
async def cmd_yevro(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugungi yevro kurslari: \n"
    for kurs in response.json():
        if kurs['Ccy'] in ["EUR"]:
            courses[kurs['Ccy']] = float(kurs['Rate'])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
    await message.answer(text=s)


@cmd_router.message(Command('rubl'))
async def cmd_rubl(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugungi rubl kurslari: \n"
    for kurs in response.json():
        if kurs['Ccy'] in ["RUB"]:
            courses[kurs['Ccy']] = float(kurs['Rate'])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
    await message.reply(text=s)





