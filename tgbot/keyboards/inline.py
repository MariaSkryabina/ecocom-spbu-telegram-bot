from aiogram import Dispatcher, types


def create_keyboard_for_question(d):

    NOK = "❌"
    OK = "✅"
    if d == -1:
        buttons = [types.InlineKeyboardButton(text=NOK + "сообщение без ответа", callback_data=str(d))]
    else:
        buttons = [types.InlineKeyboardButton(text=OK + "отвечено", callback_data=str(d))]

    question_keyboard = types.InlineKeyboardMarkup(row_width=1)
    question_keyboard.add(*buttons)
    return question_keyboard


def user_start_keyboard():
    buttons = [types.InlineKeyboardButton(text="сортировка в СПБГУ", callback_data="sort"),
               types.InlineKeyboardButton(text="инфо о сообществе", callback_data="info"),
               types.InlineKeyboardButton(text="фидбек/вопрос", callback_data="message")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def sorting_keyboard():
    sorting_categories = {"PET": "♳ PET", "GL": "🫙 стекло", "AL": "🖇️ алюминий", "PAPER": "📰 бумага",
                          "PP_HARD": "♷ PP (твердый)", "PP_SOFT": "♷ PP (мягкий)", "TP": "🧃 Tetra Pak", "BT": "🔋батарейки",
                          "CAPS": "🔘 крышечки", "BULB": "💡 лампочки", "START": "⬅ Назад"}
    buttons = []
    for key in sorting_categories:
        buttons.append(types.InlineKeyboardButton(text=sorting_categories[key], callback_data=key))
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def sorting_search_options():
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def ecocom_info_keyboard():
    button_data = {"WHO": "Кто мы", "PJ": "Проекты", "JOIN": "Присоединиться", "START": "⬅ Назад"}
    buttons = []
    for key in button_data:
        buttons.append(types.InlineKeyboardButton(text=button_data[key], callback_data=key))
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def who_we_are_keyboard():
    buttons = [types.InlineKeyboardButton(text="Ознакомиться с документом", callback_data="send_document"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard


def send_doc_about_ecocom_keyboard():
    buttons = [types.InlineKeyboardButton(text="Задать вопрос", callback_data="ask question"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def projects_keyboard():
    buttons = [types.InlineKeyboardButton(text="Хочу с Вами!", callback_data="JOIN"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard


def back_to_info_keyboard():
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)


def message_to_support_keyboard():
    buttons = [types.InlineKeyboardButton(text="Задать вопрос", callback_data="ask question"),
               types.InlineKeyboardButton(text="Дать обратную связь", callback_data="feedback"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard

def forward_feedback():

    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="message")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    return keyboard