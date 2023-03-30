from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_load = KeyboardButton('')
button_delete = Keyboard('')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard = True).add(button_load)\
            .add(button_delete)