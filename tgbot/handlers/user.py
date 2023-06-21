from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from tgbot.config import Config
from aiogram.dispatcher import FSMContext
import tgbot.misc.messages.messages as messages


class UserStates(StatesGroup):
    initial_state = State()
    writing_question_to_forward = State()
    writing_feedback_to_forward = State()
    waiting_for_message_from_admin = State()
    feedback_forwarded = State()
    dialog_with_support_opened = State()


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
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text = "Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def glass(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width = 2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def aluminium(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width = 2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def paper(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pp(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def tetra_pak(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text = "Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def batteries(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text = "Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def caps(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text = "Показать все", callback_data = "LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await UserStates.next()


async def bulbs(call: types.CallbackQuery):
    text = ["Можно посмотреть список всех точек РСО или найти 5 рядом! Жми на кнопочку)"]
    buttons = [types.InlineKeyboardButton(text="Показать все", callback_data="LIST"),
               types.InlineKeyboardButton(text="Найти ближайшие", callback_data="NEAR"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def make_list(call: types.CallbackQuery):
    text = ["Здесь будет отсортированный список точек. "
            "Скорее всего делать отправку информации по цифре мы делать не будем."]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def show_near(call: types.CallbackQuery):
    text = ["Здесь будет отсортированный список точек. "
            "Скорее всего делать отправку информации по цифре мы делать не будем."]
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="sort")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def info(call: types.CallbackQuery):
    text = ["В этом разделе ты можешь узнать подробнее о нашей деятельности:"]

    buttons = [types.InlineKeyboardButton(text="Кто мы", callback_data="WHO"),
               types.InlineKeyboardButton(text="Проекты", callback_data="PJ"),
               types.InlineKeyboardButton(text="Присоединиться", callback_data="JOIN"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def who(call: types.CallbackQuery):
    text = messages.who_we_are
    buttons = [types.InlineKeyboardButton(text="Ознакомиться с документом", callback_data="send_document"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def send_document_about_ecocom(call: types.CallbackQuery):
    text = messages.send_document
    buttons = [types.InlineKeyboardButton(text="Задать вопрос", callback_data="ask question"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def projects(call: types.CallbackQuery):
    text = messages.projects
    buttons = [types.InlineKeyboardButton(text="Хочу с Вами!", callback_data="JOIN"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
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
    text = messages.support_initial
    buttons = [types.InlineKeyboardButton(text="Задать вопрос", callback_data="ask question"),
               types.InlineKeyboardButton(text="Дать обратную связь", callback_data="feedback"),
               types.InlineKeyboardButton(text="⬅ Назад", callback_data="START")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def ask_question(call: types.CallbackQuery, state: FSMContext):
    text = messages.question_initial
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.writing_question_to_forward.state)


async def give_feedback(call: types.CallbackQuery, state: FSMContext):
    text = messages.feedback_initial
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="info")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.writing_feedback_to_forward.state)


async def forward_feedback(message: Message, config: Config, state:FSMContext):
    text = messages.feedback_final
    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        "#feedback" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}", parse_mode="HTML"
    )
    buttons = [types.InlineKeyboardButton(text="⬅ Назад", callback_data="message")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer('\n'.join(text), reply_markup=keyboard)
    await state.set_state(UserStates.feedback_forwarded.state)


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


async def forward_question(message: Message, config: Config, state: FSMContext):

    text = messages.question_final
    keyboard_for_support = create_keyboard_for_question(d=-1)

    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        "#question" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}", parse_mode="HTML",
        reply_markup=keyboard_for_support
    )
    await message.answer('\n'.join(text))
    # await state.set_state(UserStates.dialog_with_support_opened.state)


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
    dp.register_callback_query_handler(make_list, text="LIST", state="*")
    dp.register_callback_query_handler(show_near, text= "NEAR", state="*")
    dp.register_callback_query_handler(info, text="info", state="*")
    dp.register_callback_query_handler(who, text="WHO", state="*")
    dp.register_callback_query_handler(projects, text="PJ", state="*")
    dp.register_callback_query_handler(join, text="JOIN", state="*")
    dp.register_callback_query_handler(message_to_support, text="message", state="*")
    dp.register_callback_query_handler(ask_question, text="ask question", state="*")
    dp.register_callback_query_handler(give_feedback, text="feedback", state="*")
    dp.register_callback_query_handler(send_document_about_ecocom, text="send_document", state="*")
    dp.register_message_handler(forward_question, state=UserStates.writing_question_to_forward)
    dp.register_message_handler(forward_feedback, state=UserStates.writing_feedback_to_forward)
    # dp.register_callback_query_handler(stop_chatting, text="stop", state="*")
