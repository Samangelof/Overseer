# core/handlers/relapse.py
from aiogram import Router, types, F
from aiogram.filters import Command
from core.keyboards.main_menu import main_menu_kb


router = Router()

@router.message(Command("срыв"))
@router.message(F.text == "🔁 Срыв")
async def relapse_handler(message: types.Message):
    text = (
        "⚠️ *Сбой протокола зафиксирован.*\n\n"
        "Юнит M-23 допустил отклонение от устава. Это не конец.\n"
        "REBOOT.OPS активирует аварийный протокол восстановления.\n\n"
        "🔧 *Шаги для восстановления:*\n"
        "1. Прими холодный душ.\n"
        "2. Убери помещение (10 минут).\n"
        "3. Выключи отвлекающие устройства (телефон, YouTube, Telegram).\n"
        "4. Выйди на 15 минут на улицу. Без наушников.\n"
        "5. Запусти простое действие: мытье посуды, чтение, прогулка.\n\n"
        "🛡 Когда будешь готов — нажми 'Вернуться в строй'."
    )

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🛡 Вернуться в строй")],
            [types.KeyboardButton(text="📊 Отчeт"), types.KeyboardButton(text="📈 Статус")],
        ],
        resize_keyboard=True
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")


@router.message(Command("вернуться в строй"))
@router.message(F.text.lower().strip() == "🛡 вернуться в строй")
async def return_to_duty(message: types.Message):
    await message.answer("💠 Протокол REBOOT повторно активирован. Действуй, юнит M-23.", reply_markup=main_menu_kb())
