from aiogram import F
from aiogram import Router
from aiogram.filters import Command, or_f
from aiogram.types import Message

from keyboards.inline import start

command_router = Router()


@command_router.message(or_f(Command("start"), (F.text == "Дом 🏠")))
async def command_start_handler(message: Message) -> None:
    text = (
        "Привет, я BookBuddy! Я твой книжный ассистент! "
        "Готов помочь найти, порекомендовать рекомендациями или ответить на любые вопросы о книгах. "
        "Ещё я предоставляю информацию о книгах и помогу тебе создать списки для чтения. \n\n "
        "Какую книгу ты ищешь сегодня?")

    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("opportunities"), (F.text == "Возможности")))
async def command_opportunities(message: Message) -> None:
    text = ("Вот, что я могу: \n\n"
            "<b>1. Поиск книг:</b>\n- Вы можете ввести название книги, автора или жанр, чтобы получить информацию о книге, рейтинг, отзывы и доступные форматы (например, электронная книга, аудиокнига).\n\n"
            "<b>2. Рекомендации:</b>\n- Я составлю рекомендации на основе ваших предпочтений. Вы можете ответить на несколько вопросов о своих интересах, и я сгенерирует список книг, которые могут возможно вам понравиться.\n\n"
            "<b>3. Списки для чтения:</b>\n- Вы можете создавать и управлять своими списками для чтения.\n\n"
            "<b>4. Обсуждения и рецензии:</b>\n- Вы можете оставлять рецензии на прочитанные книги и/или участвовать в обсуждениях с другими пользователями. Можно организовать опросы и голосования на тему любимых книг.\n\n"
            "<b>5. Интеграция с библиотеками и сервисами:</b>\n- Я могу предоставлять информацию о местных библиотеках и онлайн-сервисах для покупки или аренды книг.\n\n"
            "<b>6. Подборка по настроению:</b>\n- Вы можете выбрать настроение (например: для вдохновения, для расслабления), и бот предложит книги, соответствующие этому настроению.\n\n")

    await message.answer(text, reply_markup=start, parse_mode="HTML")


@command_router.message(or_f(Command("search"), (F.text == "Поиск 🔍")))
async def command_opportunities(message: Message) -> None:
    text = "Введите фИО автора и навание книги"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("recommendations"), (F.text == "Рекомендации")))
async def command_rec(message: Message) -> None:
    text = "Вот что популярно у пользователей в последнее время"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("compilation"), (F.text == "Подборка 📚")))
async def command_compilation(message: Message) -> None:
    text = "Вот подборка основанная на ваших интересах"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("yourlist"), (F.text == "Ваш список 📋")))
async def command_yourlist(message: Message) -> None:
    text = "Список ваших закладок"
    await message.answer(text, reply_markup=start)


@command_router.message(or_f(Command("reviews"), (F.text == "Отзывы и обсуждения 💬")))
async def command_reviews(message: Message) -> None:
    text = "Последние новости и отзывы о книгах"
    await message.answer(text, reply_markup=start)


@command_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    text = ("I am book assistant. This is my commands: \n"
            "/start \n"
            "/about \n"
            "/help \n")
    await message.answer(text)
