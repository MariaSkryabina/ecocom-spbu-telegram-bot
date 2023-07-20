from aiogram import Dispatcher, types
from aiogram.types import Message
from tgbot.keyboards.inline import create_keyboard_for_question
from aiogram.dispatcher import FSMContext


def extract_id(message: Message) -> int:

    # Получение списка сущностей (entities) из текста или подписи к медиафайлу в отвечаемом сообщении
    entities = message.entities or message.caption_entities
    # Если всё сделано верно, то последняя (или единственная) сущность должна быть хэштегом...
    if not entities or entities[-1].type != "hashtag":
        raise ValueError("Не удалось извлечь ID для ответа!")

    # ... более того, хэштег должен иметь вид #id123456, где 123456 — ID получателя
    hashtag = entities[-1].get_text(message.text or message.caption)
    if len(hashtag) < 4 or not hashtag[3:].isdigit():  # либо просто #id, либо #idНЕЦИФРЫ
        raise ValueError("Некорректный ID для ответа!")

    return int(hashtag[3:])


async def reply_to_user(message: Message):

    cb_data = int(message.reply_to_message.reply_markup.inline_keyboard[0][0].callback_data)
    # Вырезаем ID
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    buttons = [types.InlineKeyboardButton(text="⬅ Закрыть чат и вернуться назад", callback_data="START")]
    keyboard_for_user = types.InlineKeyboardMarkup(row_width=1)
    keyboard_for_user.add(*buttons)
    await message.copy_to(user_id, reply_markup=keyboard_for_user)
    await message.reply_to_message.edit_reply_markup(reply_markup=create_keyboard_for_question(d=cb_data*(-1)))


async def change_check_button_manually(call: types.CallbackQuery):
    cb_data = int(call.message.reply_markup.inline_keyboard[0][0].callback_data)
    await call.message.edit_reply_markup(reply_markup=create_keyboard_for_question(d=cb_data * (-1)))
    await call.answer()


def register_admin(dp: Dispatcher):
    dp.register_message_handler(reply_to_user, state='*', is_reply=True, is_support=True)
    dp.register_callback_query_handler(change_check_button_manually, state="*", text=["1", "-1"], is_support=True)

