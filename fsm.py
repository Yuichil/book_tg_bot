from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from states import Form

fsm_router = Router()


@fsm_router.message(or_f(Command("form"), F.text == "Добавить в список книгу"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Введите название книги", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.name)


@fsm_router.message(Form.name)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.author)
    await message.answer(text="Кто автор?")


@fsm_router.message(Form.author)
async def process_add_or_not(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    mylist = await state.get_data()
    print(mylist)
    await state.clear()
