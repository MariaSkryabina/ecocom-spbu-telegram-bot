from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from tgbot.config import Config
from aiogram.dispatcher import FSMContext
import tgbot.misc.messages.messages as messages
import tgbot.keyboards.inline as keyboards


class UserStates(StatesGroup):
    initial_state = State()
    writing_question_to_forward = State()
    writing_feedback_to_forward = State()
    waiting_for_message_from_admin = State()
    feedback_forwarded = State()
    dialog_with_support_opened = State()


async def user_start(message: Message, state: FSMContext):
    text = messages.user_start
    keyboard = keyboards.user_start_keyboard()
    await message.answer('\n'.join(text), reply_markup=keyboard)
    await state.set_state(UserStates.initial_state.state)


async def user_start_back(call: types.CallbackQuery, state: FSMContext):
    text = messages.user_start
    keyboard = keyboards.user_start_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.initial_state.state)


async def sorting(call: types.CallbackQuery):
    text = messages.sorting
    keyboard = keyboards.sorting_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pet(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def glass(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def aluminium(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def paper(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pp_hard(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def pp_soft(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def tetra_pak(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def batteries(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def caps(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def bulbs(call: types.CallbackQuery):
    text = messages.sorting_search_options
    keyboard = keyboards.sorting_search_options()
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
    text = messages.ecocom_info
    keyboard = keyboards.ecocom_info_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def who(call: types.CallbackQuery):
    text = messages.who_we_are
    keyboard = keyboards.who_we_are_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def send_document_about_ecocom(call: types.CallbackQuery):
    text = messages.send_document
    keyboard = keyboards.send_doc_about_ecocom_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def projects(call: types.CallbackQuery):
    text = messages.projects
    keyboard = keyboards.projects_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def join(call: types.CallbackQuery):
    text = messages.join
    keyboard = keyboards.back_to_info_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()


async def message_to_support(call: types.CallbackQuery, state: FSMContext):
    text = messages.support_initial
    keyboard = keyboards.back_to_info_keyboard()
    await call.message.answer('\n'.join(text), reply_markup=keyboard)
    await call.answer()
    await state.set_state(UserStates.writing_question_to_forward.state)


# async def ask_question(call: types.CallbackQuery, state: FSMContext):
#     text = messages.question_initial
#     keyboard = keyboards.back_to_info_keyboard()
#
#
# async def give_feedback(call: types.CallbackQuery, state: FSMContext):
#     text = messages.feedback_initial
#     keyboard = keyboards.back_to_info_keyboard()
#     await call.message.answer('\n'.join(text), reply_markup=keyboard)
#     await call.answer()
#     await state.set_state(UserStates.writing_feedback_to_forward.state)


async def forward_feedback(message: Message, config: Config, state:FSMContext):
    text = messages.feedback_final
    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        "#feedback" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}", parse_mode="HTML"
    )
    keyboard = keyboards.forward_feedback()
    await message.answer('\n'.join(text), reply_markup=keyboard)
    await state.set_state(UserStates.feedback_forwarded.state)


async def forward_question(message: Message, config: Config, state: FSMContext):

    text = messages.question_final
    keyboard_for_support = keyboards.create_keyboard_for_question(d=-1)

    await message.bot.send_message(
        config.tg_bot.support_ids[0],
        f"#from_student (нажми на <b>Reply</b>, чтобы ответить)\n"
        "-----------------------------\n\n"
        f"{message.html_text}\n\n"
        f"#id{message.from_user.id}", parse_mode="HTML",
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
    dp.register_callback_query_handler(pp_hard, text="PP_HARD", state="*")
    dp.register_callback_query_handler(pp_soft, text="PP_SOFT", state="*")
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
    # dp.register_callback_query_handler(ask_question, text="ask question", state="*")
    # dp.register_callback_query_handler(give_feedback, text="feedback", state="*")
    dp.register_callback_query_handler(send_document_about_ecocom, text="send_document", state="*")
    dp.register_message_handler(forward_question, state=UserStates.writing_question_to_forward)
    dp.register_message_handler(forward_feedback, state=UserStates.writing_feedback_to_forward)
    # dp.register_callback_query_handler(stop_chatting, text="stop", state="*")
