import dp as dp
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from tgbot.data_base.sqlite_db import sql_add_command
from tgbot.keyboards import admin_kb

async def admin_start(message: Message):
    """

    :type message: object
    """
    await message.reply("Hello, admin!")


class FSMAdmin(StatesGroup):
    photo = State()
    address = State()
    longitude = State()
    latitude = State()
    paper = State()
    pet = State()
    glass = State()
    aluminium = State()
    pp = State()
    tetrapak = State()
    batteries = State()
    caps = State()
    bulbs = State()
    description = State()

#Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands = 'Загрузить', state = None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото точки РСО')




#Выход из состояний
# @dp.message_handler(state = "*", commands = 'отмена')
# @dp.message_handler(Text(equals = 'отмена', ignore_case = True), state = "*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

#Ловим первый ответ и пишем в словарь
#@dp.message_handler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Введите адрес с комментариями")

#Ловим второй ответ
#@dp.message_handler(state = FSMAdmin.address)
async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите долготу")

#@dp.message_handler(state = FSMAdmin.longitude)
async def load_longitude(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['longitude'] = float(message.text)
    await FSMAdmin.next()
    await message.reply("Введите широту")

#@dp.message_handler(state = FSMAdmin.latitude)
async def load_latitude(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['latitude'] = float(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать бумагу? Да - 1, Нет - 0")

#@dp.message_handler(state = FSMAdmin.paper)
async def load_paper(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['paper'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать pet? Да - 1, Нет - 0")

# @dp.message_handler(state = FSMAdmin.pet)
async def load_pet(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pet'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать стекло? Да - 1, Нет - 0")

# @dp.message_handler(state = FSMAdmin.glass)
async def load_glass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['glass'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать алюминий? Да - 1, Нет - 0")

# @dp.message_handler(state = FSMAdmin.aluminium)
async def load_aluminium(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['aluminium'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать pp? Да - 1, Нет - 0")


# @dp.message_handler(state = FSMAdmin.pp)
async def load_pp(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pp'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать батарейки? Да - 1, Нет - 0")



# @dp.message_handler(state = FSMAdmin.batteries)
async def load_batteries(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['batteries'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать крышечки? Да - 1, Нет - 0")


# @dp.message_handler(state = FSMAdmin.caps)
async def load_caps(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['caps'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Можно ли сдать лампочки? Да - 1, Нет - 0")


# @dp.message_handler(state = FSMAdmin.bulbs)
async def load_bulbs(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bulbs'] = int(message.text)
    await FSMAdmin.next()
    await message.reply("Введите заметки и подробное описание маршрута")


# @dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await sql_add_command(state)
    await state.finish()






def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(cm_start, commands = ["Загрузить"], state = None, is_admin=True)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена', is_admin=True)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*", is_admin=True)
    dp.register_message_handler(load_photo, content_types = ['photo'], state = FSMAdmin.photo, is_admin=True)
    dp.register_message_handler(load_address, state = FSMAdmin.address, is_admin=True)
    dp.register_message_handler(load_longitude, state=FSMAdmin.longitude, is_admin=True)
    dp.register_message_handler(load_latitude, state=FSMAdmin.latitude, is_admin=True)
    dp.register_message_handler(load_paper, state=FSMAdmin.paper, is_admin=True)
    dp.register_message_handler(load_pet, state = FSMAdmin.pet, is_admin=True)
    dp.register_message_handler(load_glass, state=FSMAdmin.glass, is_admin=True)
    dp.register_message_handler(load_aluminium, state=FSMAdmin.aluminium, is_admin=True)
    dp.register_message_handler(load_pp, state=FSMAdmin.pp, is_admin=True)
    dp.register_message_handler(load_batteries, state=FSMAdmin.batteries, is_admin=True)
    dp.register_message_handler(load_caps, state=FSMAdmin.caps, is_admin=True)
    dp.register_message_handler(load_bulbs, state=FSMAdmin.bulbs, is_admin=True)
    dp.register_message_handler(load_description, state=FSMAdmin.description, is_admin=True)





