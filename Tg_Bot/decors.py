from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from Utils.db_connector import db_admins
from .bot import bot


def admin(input_func):
    async def output_func(*args, **kwargs):
        msg = args[0]
        if type(msg) != Message:
            msg = msg.message  # каллбек
        if msg.chat.id in db_admins.get_admins():
            try:
                await input_func(*args)
            except:
                await input_func(state=kwargs['state'], *args)
        else:
            await bot.send_message(chat_id=msg.chat.id, text='У тебя нет прав на использование')

    return output_func
