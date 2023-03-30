from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

d = -1


def extract_id(message: Message) -> int:
    """
    Извлекает ID юзера из хэштега в сообщении
    :param message: сообщение, из хэштега в котором нужно достать айди пользователя
    :return: ID пользователя, извлечённый из хэштега в сообщении
    """
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

    # Вырезаем ID
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    await message.copy_to(user_id)


async def stop_chatting(call: types.CallbackQuery, message: Message):
    click_sign = call.data*(-1)

    def create_keyboard_for_question(d):
        NOK = "❌"
        OK = "✅"
        if d == -1:
            buttons = [types.InlineKeyboardButton(text=NOK + " закончить диалог", callback_data=str(-d))]
        else:
            buttons = [types.InlineKeyboardButton(text=OK + " закончить диалог", callback_data=str(-d))]

        question_keyboard = types.InlineKeyboardMarkup(row_width=1)
        question_keyboard.add(*buttons)
        return question_keyboard

    text = "#question" + f"\n\n{message.html_text}" + f"\n\n#id{message.from_user.id}"
    await call.message.edit_text('\n'.join(text), reply_markup=create_keyboard_for_question(click_sign))


def register_admin(dp: Dispatcher):
    dp.register_message_handler(reply_to_user, state='*', is_reply=True, is_support=True)
    dp.register_callback_query_handler(stop_chatting, text=str(d), state="*")
