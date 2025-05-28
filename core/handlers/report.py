from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from core.keyboards.main_menu import main_menu_kb
from db.crud import get_or_create_user, save_daily_report
from db.database import AsyncSessionLocal


router = Router()

class ReportState(StatesGroup):
    relapse = State()
    showers = State()
    worked_hours = State()
    mood = State()
    note = State()

@router.message(F.text.lower() == "📊 отчёт")
async def report_start(message: types.Message, state: FSMContext):
    await state.set_state(ReportState.relapse)
    await message.answer("Срыв был сегодня? (да/нет)")

@router.message(ReportState.relapse)
async def report_relapse(message: types.Message, state: FSMContext):
    await state.update_data(relapse=message.text.lower() == "да")
    await state.set_state(ReportState.showers)
    await message.answer("Сколько раз принял душ? (0/1/2)")

@router.message(ReportState.showers)
async def report_showers(message: types.Message, state: FSMContext):
    await state.update_data(showers=int(message.text))
    await state.set_state(ReportState.worked_hours)
    await message.answer("Сколько часов работал/учился сегодня?")

@router.message(ReportState.worked_hours)
async def report_hours(message: types.Message, state: FSMContext):
    await state.update_data(worked_hours=float(message.text))
    await state.set_state(ReportState.mood)
    await message.answer("Оцени настроение от 0 до 10")

@router.message(ReportState.mood)
async def report_mood(message: types.Message, state: FSMContext):
    await state.update_data(mood=int(message.text))
    await state.set_state(ReportState.note)
    await message.answer("Хочешь добавить заметку? (можно пропустить)")

@router.message(ReportState.note)
async def report_note(message: types.Message, state: FSMContext):
    await state.update_data(note=message.text)
    data = await state.get_data()

    async with AsyncSessionLocal() as session:
        await get_or_create_user(session, message.from_user.id, message.from_user.username)
        await save_daily_report(
            session,
            user_id=message.from_user.id,
            relapse=data["relapse"],
            showers=data["showers"],
            worked_hours=data["worked_hours"],
            mood=data["mood"],
            note=data["note"]
        )

    await state.clear()
    await message.answer("Отчёт принят. Протокол соблюдён.", reply_markup=main_menu_kb())
