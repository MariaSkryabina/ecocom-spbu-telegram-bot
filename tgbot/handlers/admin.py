from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot

async def admin_start(message: Message):
    """

    :type message: object
    """
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
