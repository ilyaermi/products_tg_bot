from aiogram.dispatcher.filters.state import StatesGroup, State


class AddComing(StatesGroup):
    product = State()
    count = State()


class AddExpenditure(StatesGroup):
    product = State()
    flow_direction = State()
    count = State()
    price = State()
