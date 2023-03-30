from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from tgbot.config import Config
from aiogram.dispatcher import FSMContext


class UserStates(StatesGroup):
    initial_state = State()
    waiting_for_question_to_forward = State()
    waiting_for_feedback_to_forward = State()
    waiting_for_message_from_admin = State()


async def user_start(message: Message, state: FSMContext):
    text = ["Нажми на кнопку и выбери интересующий тебя раздел"]
    buttons = [types.InlineKeyboardButton(text="сортировка в СПБГУ", callback_data="sort"),
               types.InlineKeyboardButton(text="инфо о сообществе", callback_data="info"),
               types.InlineKeyboardButton(text="фидбек/вопрос", callback_data="message")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer('\n'.join(text), reply_markup=keyboard)
    await state.set_state(UserStates.initial_state.state)


async def user_start_back(call: types.CallbackQuery, state: FSMContext):
    text = ["Нажми на кнопку и выбери интересующий тебя раздел"]
    buttons = [types.InlineKeyboardButton(text="сортировка в СПБГУ", callback_data="sort"),
               types.InlineKeyboardButton(text="инфо о сообществе", callback_data="info"),
               types.InlineKeyboardButton(text="фидбек/вопрос", callback_data="message")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.initial_state.state)


async def sorting(call: types.CallbackQuery):
    text = ["В этом разделе ты можешь узнать подробнее о точках приема вторсырья на территории нашего "
            "университета.", "Выбери интересующую тебя фракцию из списка:"]

    buttons = [types.InlineKeyboardButton(text="♳ PET", callback_data="PET"),
               types.InlineKeyboardButton(text="🫙 стекло", callback_data="GL"),
               types.InlineKeyboardButton(text="🖇️ алюминий", callback_data="AL"),
               types.InlineKeyboardButton(text="📰 бумага", callback_data="PAPER"),
               types.InlineKeyboardButton(text="♷ PP", callback_data="PP"),
               types.InlineKeyboardButton(text="🧃 Tetra Pak", callback_data="TP"),
               types.InlineKeyboardButton(text="🔋батарейки", callback_data="BT"),
               types.InlineKeyboardButton(text="🔘 крышечки", callback_data="CAPS"),
               types.InlineKeyboardButton(text="💡 лампочки", callback_data="BULB"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pet(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма PET пластика:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def glass(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма стекла:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def aluminium(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма алюминия:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def paper(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма бумаги:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pp(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку 5 пластика:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def tetra_pak(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма Tetra Pak:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def batteries(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма батареек:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def caps(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма крышечек:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def bulbs(call: types.CallbackQuery):
    text = ["Выбери наиболее удобную точку приёма лампочек:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def info(call: types.CallbackQuery):
    text = ["В этом разделе ты можешь узнать подробнее о нашей деятельности:"]

    buttons = [types.InlineKeyboardButton(text="Кто мы", callback_data="WHO"),
               types.InlineKeyboardButton(text="Проекты", callback_data="PJ"),
               types.InlineKeyboardButton(text="Мероприятия семестра", callback_data="PLAN"),
               types.InlineKeyboardButton(text="Присоединиться", callback_data="JOIN"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def who(call: types.CallbackQuery):
    text = ["Кто мы такие? Кто знает нас.....никто:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def projects(call: types.CallbackQuery):
    text = ["Есть Vegan Week, Одеться на стипендию, сбор вторсырья"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def mero(call: types.CallbackQuery):
    text = ["20 ноября сбор вторсырья в пунке"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def join(call: types.CallbackQuery):
    text = ["Хочешь все время думать о нас?:"]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def message_to_support(call: types.CallbackQuery):
    text = ["Хотите дать обратную связь экокому? А может задать вопрос? Всегда рады!"]
    buttons = [types.InlineKeyboardButton(text="Задать вопрос", callback_data="ask question"),
               types.InlineKeyboardButton(text="Дать обратную связь", callback_data="feedback"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def ask_question(call: types.CallbackQuery, state: FSMContext):
    text = ["Напишите свой вопрос."]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.waiting_for_question_to_forward.state)


async def give_feedback(call: types.CallbackQuery, state: FSMContext):
    text = ["Напишите вашу обратную связь по работе экологического комитета."
            " Это может быть фидбек по мероприятию, идея по улучшению нашей деятельности"
            " или другая информация, которую вам кажется важным до нас донести."]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.waiting_for_feedback_to_forward.state)


async def forward_feedback(message: Message, config: Config):
    text = ["Ваше сообщение отправлено! Спасибо за помощь и вклад в улучшение нашей деятельности."]
    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        "#feedback" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}", parse_mode="HTML"
    )
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer('\n'.join(text), reply_markup=keyboard)


async def forward_question(message: Message, config: Config):
    text = ["Сообщение экокому отправлено. В ближайшее время вы получите ответ."]

    def create_keyboard_for_question(d):
        NOK = "❌"
        OK = "✅"
        if d == -1:
            buttons = [types.InlineKeyboardButton(text=NOK + " закончить диалог", callback_data=str(d))]
        else:
            buttons = [types.InlineKeyboardButton(text=OK + " закончить диалог", callback_data=str(d))]

        question_keyboard = types.InlineKeyboardMarkup(row_width=1)
        question_keyboard.add(*buttons)
        return question_keyboard

    keyboard = create_keyboard_for_question(d=-1)
    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        "#question" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}", parse_mode="HTML",
        reply_markup=keyboard
    )
    await message.answer('\n'.join(text))


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(user_start_back, text="START", state="*")
    dp.register_callback_query_handler(sorting, text="sort", state="*")
    dp.register_callback_query_handler(pet, text="PET", state="*")
    dp.register_callback_query_handler(glass, text="GL", state="*")
    dp.register_callback_query_handler(aluminium, text="AL", state="*")
    dp.register_callback_query_handler(paper, text="PAPER", state="*")
    dp.register_callback_query_handler(pp, text="PP", state="*")
    dp.register_callback_query_handler(tetra_pak, text="TP", state="*")
    dp.register_callback_query_handler(batteries, text="BT", state="*")
    dp.register_callback_query_handler(caps, text="CAPS", state="*")
    dp.register_callback_query_handler(bulbs, text="BULB", state="*")
    dp.register_callback_query_handler(info, text="info", state="*")
    dp.register_callback_query_handler(who, text="WHO", state="*")
    dp.register_callback_query_handler(projects, text="PJ", state="*")
    dp.register_callback_query_handler(mero, text="PLAN", state="*")
    dp.register_callback_query_handler(join, text="JOIN", state="*")
    dp.register_callback_query_handler(message_to_support, text="message", state="*")
    dp.register_callback_query_handler(ask_question, text="ask question", state="*")
    dp.register_callback_query_handler(give_feedback, text="feedback", state="*")
    dp.register_message_handler(forward_feedback, state=UserStates.waiting_for_feedback_to_forward)
    dp.register_message_handler(forward_question, state=UserStates.waiting_for_question_to_forward)
    # dp.register_callback_query_handler(stop_chatting, text="stop", state="*")
