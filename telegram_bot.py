from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    chat_id = message.from_user.id
    if message.is_command():
        await bot.send_message(chat_id=chat_id, text="Welcome to Polkadot\nIt's a service for calculation")
    else:
        try:
            result = eval(message.text)
            await message.reply(text=f"Result: {result}")
        except NameError:
            await message.reply("You must only type numbers for calculation: ")

    


executor.start_polling(dp, skip_updates=True)
