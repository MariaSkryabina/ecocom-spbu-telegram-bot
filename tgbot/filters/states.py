from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    main_menu = State()
    recyclables = State()
    PET = State()
