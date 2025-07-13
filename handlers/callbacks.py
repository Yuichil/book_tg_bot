from aiogram import Router, F
from aiogram.types import CallbackQuery

callbacks_router = Router()


@callbacks_router.callback_query(F.data == "show_help")
async def to_help(callback: CallbackQuery):
    await callback.answer()
    mes = "Помогу чем смогу."
    await callback.message.answer(text=mes)




