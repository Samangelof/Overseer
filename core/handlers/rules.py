from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F


router = Router()

USTAV_TEXT = """
📜 Кодекс REBOOT.OPS

1. Каждый день минимум:
   • 6 часов работы
   • 2 душа
   • 1 отчет

2. Запрещено:
   ❌ Никотин
   ❌ Алкоголь
   ❌ Порно
   ❌ Прокрастинация
   ❌ Самобичевание

3. Уважай себя, соблюдай дисциплину.
"""

@router.message(Command("кодекс"))
@router.message(F.text.lower().strip() == "📜 кодекс")
async def show_ustav(message: types.Message):
    await message.answer(USTAV_TEXT)
