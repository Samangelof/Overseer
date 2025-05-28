from aiogram import Router, types, F
from datetime import date, timedelta
from db.database import AsyncSessionLocal
from db.models import DailyReport
from sqlalchemy.future import select
from aiogram.filters import Command


router = Router()

@router.message(Command("статус"))
@router.message(F.text == "📈 Статус")
async def status_handler(message: types.Message):
    async with AsyncSessionLocal() as session:
        today = date.today()
        week_ago = today - timedelta(days=7)

        result = await session.execute(
            select(DailyReport)
            .where(DailyReport.user_id == message.from_user.id)
            .where(DailyReport.date >= week_ago)
            .order_by(DailyReport.date)
        )

        reports = result.scalars().all()

        if not reports:
            await message.answer("Нет данных за последние 7 дней. Протокол не активен.")
            return

        success_days = sum(1 for r in reports if not r.relapse and r.worked_hours >= 6 and r.showers >= 2)
        total = len(reports)
        avg_mood = round(sum(r.mood for r in reports) / total, 1)

        response = (
            f"📆 Протокол за 7 дней:\n"
            f"Всего отчeтов: {total}\n"
            f"Стабильных дней: {success_days} ✅\n"
            f"Среднее настроение: {avg_mood} 😐\n"
        )

        await message.answer(response)
