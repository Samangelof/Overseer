from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F
from sqlalchemy import select, func
from db.database import AsyncSessionLocal
from db.models import Violation


router = Router()

@router.message(Command("устав"))
@router.message(F.text.lower() == "📊 устав")
async def ustav_stats(message: types.Message):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(func.count(Violation.id))
            .where(Violation.user_id == message.from_user.id)
        )
        total_violations = result.scalar() or 0

        last_violation = await session.execute(
            select(Violation.date)
            .where(Violation.user_id == message.from_user.id)
            .order_by(Violation.date.desc())
            .limit(1)
        )
        last = last_violation.scalar()

        msg = f"📊 Нарушения Устава:\nВсего: {total_violations}\n"
        if last:
            msg += f"Последнее: {last.strftime('%d.%m.%Y')}"
        else:
            msg += "Ты чист. Устав соблюдается."

        await message.answer(msg)
