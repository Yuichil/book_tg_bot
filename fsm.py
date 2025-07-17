from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from database import add_list,show_db
from keyboards.inline import your_list
from states import Form

fsm_router = Router()


@fsm_router.message(or_f(Command("form"), F.text == "Добавить в список книгу"))
async def sleep_to_replying(message: Message, state: FSMContext):
    await message.answer("Введите название книги", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.name)


@fsm_router.message(Form.name)
async def replying_to_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.author)
    await message.answer(text="Кто автор?")

@fsm_router.message(Form.author)
async def name_to_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(Form.genre)
    await message.answer(text="Какой жанр?")

@fsm_router.message(Form.genre)
async def  author_to_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(Form.autinfication)

@fsm_router.message(Form.autinfication)
async def process_add_or_not(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await message.answer(data['name'] + '-' + data['author'] + " добавлена ✅", reply_markup=your_list)
    user_id = message.from_user.id
    add_list(user_id, data['name'], data['author'], data['genre'])
    print(show_db())
    await state.clear()
