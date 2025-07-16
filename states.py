from aiogram import Router
from aiogram.fsm.state import State, StatesGroup

command_router = Router()


class Form(StatesGroup):
    name = State()
    author = State()
