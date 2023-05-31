import aiogram
from aiogram import Bot, Dispatcher, types
import asyncio

BOT_TOKEN_1 = '6140481675:AAFiHM3uNLDyxBBl_eX9DtjY6Xl9eM4UkFM'
BOT_TOKEN_2 = '5814149639:AAF6ssqPFiLmoybHi5Xxa16ywDzT55joQRc'

bot1 = Bot(token=BOT_TOKEN_1)
bot2 = Bot(token=BOT_TOKEN_2)

dp1 = Dispatcher(bot1)
dp2 = Dispatcher(bot2)

async def start_command1(message: types.Message):
    await message.reply("Hello from bot 1!")

async def start_command2(message: types.Message):
    await message.reply("Hello from bot 2!")

dp1.register_message_handler(start_command1, commands=['start'])
dp2.register_message_handler(start_command2, commands=['start'])

async def main():
    asyncio.create_task(dp1.start_polling())
    asyncio.create_task(dp2.start_polling())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
