from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Дом 🏠"),
        KeyboardButton(text="Возможности"),
        KeyboardButton(text="Поиск 🔍")],
        [KeyboardButton(text="Рекомендации"),
        KeyboardButton(text="Подборка 📚")],
        [KeyboardButton(text="Ваш список 📋"),
        KeyboardButton(text="Отзывы и обсуждения 💬")]
    ],
    resize_keyboard=True
)



keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<-", callback_data="prev"),
         InlineKeyboardButton(text="->", callback_data="next")]
    ]
)
#  back = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="<-back", callback_data="back")]
#     ]
# )