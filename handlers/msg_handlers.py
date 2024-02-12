import requests
from aiogram import Router
from aiogram.types import Message
from config import courses

msg_router = Router()


@msg_router.message()
async def convert_sum(message: Message):
    try:
        x = int(message.text)
        s = f"{x} UZS : \n"
        s += f"\t-{x / courses['USD']: .2f} 🇺🇸 USD\n"
        s += f"\t-{x / courses['EUR']: .2f} 🇪🇺 EUR\n"
        s += f"\t-{x / courses['RUB']: .2f} 🇷🇺 RUB\n"
        await message.reply(text=s)
    except:
        await message.reply("Iltimos, faqat son kiriting yoki /help ni bosing.")


# @msg_router.message()
# async def convert_sum_dollar(message: Message):
#     try:
#         x = str(message.text)
#         s = f"{x + '$'} USD : \n"
#         s += f"\t-{x * courses['USD']: .2f} UZS\n"
#         await message.reply(text=s)
#     except:
#         await message.reply(f"Iltimos, faqat son yoki /help ni bosing.")
#





