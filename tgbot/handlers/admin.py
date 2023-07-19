from aiogram import Dispatcher, types
from aiogram.types import Message
from tgbot.keyboards.inline import create_keyboard_for_question
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from tgbot.keyboards.reply import CANCEL_BOARD
from .user import user_start
from tgbot.db.requests import add_point
from sqlalchemy.ext.asyncio import AsyncSession
from tgbot.db.models.points import Points
from sqlalchemy.sql import exists


class AdminStates(StatesGroup):
    photo = State()
    address = State()
    route = State()
    latitude = State()
    longitude = State()
    paper = State()
    pat = State()
    glass = State()
    alum = State()
    pp_h = State()
    pp_s = State()
    batteries = State()
    cups = State()
    bulbs = State()
    notes = State()


async def upload(message: Message, state: FSMContext):
    await state.set_state(AdminStates.photo.state)
    await message.answer('\nЗагрузите фото точки РСО', reply_markup=CANCEL_BOARD)


async def upload_photo(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    #elif session.select(exists().where(Points.photo_id==message.photo[0].file_id)).scalar() is not None:
        await message.answer('Точка уже зарегистрирована!')
        return
    await state.update_data(point_photo_id=message.photo[0].file_id)
    await state.set_state(AdminStates.address.state)
    await message.answer('Хорошо! Введите точный адрес.', reply_markup=CANCEL_BOARD)


async def upload_address(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    await state.update_data(point_address=message.text)
    await state.set_state(AdminStates.route.state)
    await message.answer('Хорошо! Введите ориентир и подробный маршрут.', reply_markup=CANCEL_BOARD)


async def upload_route(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    await state.update_data(point_route=message.text)
    await state.set_state(AdminStates.latitude.state)
    await message.answer('Хорошо! Введите широту.', reply_markup=CANCEL_BOARD)


async def upload_latitude(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    lati: float
    try:
        lati = float(message.text)
    except ValueError:
        return await message.answer('Введите широту через точку.')
    await state.update_data(point_latitude=lati)
    await state.set_state(AdminStates.longitude.state)
    await message.answer('Хорошо! Введите долготу.', reply_markup=CANCEL_BOARD)


async def upload_longitude(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    long: float
    try:
        long = float(message.text)
    except ValueError:
        return await message.answer('Введите долготу через точку.')
    await state.update_data(point_longitude=long)
    await state.set_state(AdminStates.paper.state)
    await message.answer('Перерабатывается ли здесь макулатура? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_paper(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    paper: bool
    try:
        paper = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_paper=paper)
    await state.set_state(AdminStates.pat.state)
    await message.answer('Перерабатывается ли здесь ПЭТ? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_pat(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    pat: bool
    try:
        pat = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_pat=pat)
    await state.set_state(AdminStates.glass.state)
    await message.answer('Перерабатывается ли здесь стекло? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_glass(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    glass: bool
    try:
        glass = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_glass=glass)
    await state.set_state(AdminStates.alum.state)
    await message.answer('Перерабатывается ли здесь алюминий? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_alum(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    alum: bool
    try:
        alum = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_alum=alum)
    await state.set_state(AdminStates.pp_h.state)
    await message.answer('Перерабатывается ли здесь PP(твердый)? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_pp_h(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    pp_h: bool
    try:
        pp_h = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_pp_h=pp_h)
    await state.set_state(AdminStates.pp_s.state)
    await message.answer('Перерабатывается ли здесь PP(мягкий)? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_pp_s(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    pp_s: bool
    try:
        pp_s = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_pp_s=pp_s)
    await state.set_state(AdminStates.batteries.state)
    await message.answer('Перерабатывается ли здесь батарейки? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_batteries(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    bat: bool
    try:
        bat = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_bat=bat)
    await state.set_state(AdminStates.cups.state)
    await message.answer('Перерабатывается ли здесь крышечки? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_cups(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    cups: bool
    try:
        cups = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_cups=cups)
    await state.set_state(AdminStates.bulbs.state)
    await message.answer('Перерабатывается ли здесь лампочки? Укажите 0 - нет, 1 - да.', reply_markup=CANCEL_BOARD)


async def upload_bulbs(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    bul: bool
    try:
        bul = bool(int(message.text))
    except ValueError:
        return await message.answer('Введите 0 или 1.')
    await state.update_data(point_bul=bul)
    await state.set_state(AdminStates.notes.state)
    await message.answer('Почти готово! Укажите дополнительную информацию)', reply_markup=CANCEL_BOARD)


async def upload_notes(message: types.Message, state: FSMContext, session: AsyncSession,):
    if message.text == 'Отмена':
        await state.finish()
        return await user_start(message, state)
    await state.update_data(point_notes=message.text)
    data = await state.get_data()
    point = await add_point(
        session=session,
        photo_id=data['point_photo_id'],
        address=data['point_address'],
        route=data['point_route'],
        latitude=data['point_latitude'],
        longitude=data['point_longitude'],
        paper=data['point_paper'],
        pat=data['point_pat'],
        glass=data['point_glass'],
        alum=data['point_alum'],
        pp_h=data['point_pp_h'],
        pp_s=data['point_pp_s'],
        batteries=data['point_bat'],
        cups=data['point_cups'],
        bulbs=data['point_bul'],
        notes=data['point_notes']
    )
    await state.finish()
    if point is not None:
        await message.answer('Точка успешно создана!')
    else:
        await message.answer('В ходе создания точки произошла ошибка. О ней сообщено администрации.')
    return await user_start(message, state)


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
    dp.register_message_handler(upload, commands=["admin"], state="*")
    dp.register_message_handler(upload_photo, state=AdminStates.photo, content_types=["photo"], is_admin=True)
    dp.register_message_handler(upload_address, state=AdminStates.address, is_admin=True)
    dp.register_message_handler(upload_route, state = AdminStates.route, is_admin=True)
    dp.register_message_handler(upload_latitude, state=AdminStates.latitude, is_admin=True)
    dp.register_message_handler(upload_longitude, state=AdminStates.longitude, is_admin=True)
    dp.register_message_handler(upload_paper, state=AdminStates.paper, is_admin=True)
    dp.register_message_handler(upload_pat, state=AdminStates.pat, is_admin=True)
    dp.register_message_handler(upload_glass, state=AdminStates.glass, is_admin=True)
    dp.register_message_handler(upload_alum, state=AdminStates.alum, is_admin=True)
    dp.register_message_handler(upload_pp_h, state=AdminStates.pp_h, is_admin=True)
    dp.register_message_handler(upload_pp_s, state=AdminStates.pp_s, is_admin=True)
    dp.register_message_handler(upload_batteries, state = AdminStates.batteries, is_admin=True)
    dp.register_message_handler(upload_cups, state=AdminStates.cups, is_admin=True)
    dp.register_message_handler(upload_bulbs, state=AdminStates.bulbs, is_admin=True)
    dp.register_message_handler(upload_notes, state=AdminStates.notes, is_admin=True)

