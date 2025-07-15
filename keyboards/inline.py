from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Дом 🏠"),
         KeyboardButton(text="Возможности"),
         KeyboardButton(text="Поиск 🔍")],
        [KeyboardButton(text="Подборка 📚"),
         KeyboardButton(text="Ваш список 📋")]
    ],
    resize_keyboard=True
)

your_list = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить в список книгу"),
         KeyboardButton(text="Посмотреть список книг")]
    ]
)

yes_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="yes"),
         KeyboardButton(text="no")]
    ],
    resize_keyboard=True
)

add_not = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yes"),
         KeyboardButton(text="No")]
    ],
    resize_keyboard=True
)

reviews_discussions = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отзывы"),
         KeyboardButton(text="Обсуждения")]
    ],
    resize_keyboard=True
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<-", callback_data="prev"),
         InlineKeyboardButton(text="->", callback_data="next")]
    ]
)

compilation = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Автобиография"),
         KeyboardButton(text="Проза"),
         KeyboardButton(text="Детектив")],
        [KeyboardButton(text="Роман"),
         KeyboardButton(text="Фантастика"),
         KeyboardButton(text="Фэнтези")],
        [KeyboardButton(text="Драма"),
         KeyboardButton(text="Триллер"),
         KeyboardButton(text="Мистика/ужасы")]
    ],
    resize_keyboard=True
)
