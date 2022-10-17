from aiogram import Dispatcher, types
from aiogram.types import Message


async def user_start(message: Message):
    text = [
        f'Привет,  {message.from_user.first_name}!',
        'Нажми на кнопку и выбери интересующий тебя раздел']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['сортировка в СПБГУ', 'инфо о сообществе', 'фидбек/вопрос']
    keyboard.add(buttons[0], buttons[1])
    keyboard.add(buttons[2])
    await message.answer('\n'.join(text), reply_markup=keyboard)


async def sorting(message: Message):
    text = ["Окей, в этом разделе ты можешь узнать подробнее о точках приема вторсырья на территории нашего "
            "университета.", "Выбери интересующую тебя фракцию из списка"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons1 = ['♳ PET', '🫙 стекло', '🖇️ алюминий']
    keyboard.add(*buttons1)
    buttons2 = ['📰 бумага', '♷ PP', '🧃 Tetra Pak']
    keyboard.add(*buttons2)
    buttons3 = ['⬅ Назад']
    keyboard.add(*buttons3)
    await message.answer('\n'.join(text), reply_markup=keyboard)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(sorting, lambda message: message.text == "сортировка в СПБГУ", state="*")
