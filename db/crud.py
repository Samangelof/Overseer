from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import User, DailyReport
from datetime import date


async def get_or_create_user(session: AsyncSession, user_id: int, username: str | None) -> User:
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if user:
        return user

    user = User(id=user_id, username=username)
    session.add(user)
    await session.commit()
    return user

async def save_daily_report(session: AsyncSession, user_id: int, relapse: bool, showers: int, worked_hours: float, mood: int, note: str | None = None) -> DailyReport:
    report = DailyReport(
        user_id=user_id,
        date=date.today(),
        relapse=relapse,
        showers=showers,
        worked_hours=worked_hours,
        mood=mood,
        note=note
    )
    session.add(report)
    await session.commit()
    await session.refresh(report)
    return report
