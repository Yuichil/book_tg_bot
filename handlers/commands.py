from aiogram import F
from aiogram import Router
from aiogram.filters import Command, or_f
from aiogram.types import Message

from database import get_user_books, add_list
from keyboards.inline import start, your_list, compilation

command_router = Router()


@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    text = ("Привет, я <i>BookBuddy</i>!"
            " Я твой книжный ассистент! Готов помочь найти и порекомендовать книги. Ещё я предоставляю информацию о книгах и помогу тебе создать списки для чтения. \n\n "
            "Что вас интересует?")

    await message.answer(text, reply_markup=start, parse_mode="HTML")


@command_router.message(or_f(Command("home"), (F.text == "Дом 🏠")))
async def command_start_handler(message: Message) -> None:
    text = "Дом 🏠"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("opportunities"), (F.text == "Возможности")))
async def command_opportunities(message: Message) -> None:
    text = ("Вот, что я могу: \n\n"
            "<b>1. Поиск книг:</b>\n- Вы можете ввести название книги, автора, чтобы получить информацию о книге.\n\n"
            "<b>2. Списки для чтения:</b>\n- Вы можете создавать и управлять своими списками для чтения.\n\n"
            "<b>3. Подборка по жанрам:</b>\n- Вы можете выбрать жанр и бот предложит книги.\n\n")

    await message.answer(text, reply_markup=start, parse_mode="HTML")


@command_router.message(or_f(Command("search"), (F.text == "Поиск 🔍")))
async def command_opportunities(message: Message) -> None:
    text = "Введите фИО автора и навание книги"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("compilation"), (F.text == "Подборка 📚")))
async def command_compilation(message: Message) -> None:
    text = "Какой жанр хотите почитать сегодня"
    await message.answer(text, reply_markup=compilation)


@command_router.message(or_f(Command("your_list"), (F.text == "Ваш список 📋")))
async def command_your_list(message: Message) -> None:
    text = "Вывести весь список или добавитть новую книгу?"
    await message.answer(text, reply_markup=your_list)


@command_router.message(or_f(Command("watch_list"), (F.text == "Посмотреть список книг")))
async def command_your_list(message: Message) -> None:
    user_id = message.from_user.id
    l = get_user_books(user_id)
    user_list = "Ваш список книг: \n"
    for line in l:
        user_list += f"{line[1]} - {line[2]} \n"
    await message.answer(user_list)

@command_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    text = ("/start - перезапустить бота\n"
            "/help - помощь\n"
            "/opportunities - что умеет этот бот\n"
            "/search - поиск книг\n"
            "/compilation - поборка по жанрам\n"
            "/your_list - добавить или посмотреть список\n"
            "/form - добавить книгу в список\n"
            )
    await message.answer(text)
