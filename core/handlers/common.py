from aiogram import Router, types
from aiogram.filters import CommandStart
from core.keyboards.main_menu import main_menu_kb


router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "REBOOT.OPS активирован.\n"
        "Юнит: M-23\n"
        "Цель: контроль, отчетность, дисциплина.\n\n"
        "Выбери протокол:",
        reply_markup=main_menu_kb()
    )
