from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Отчёт"), KeyboardButton(text="📈 Статус")],
            [KeyboardButton(text="🧠 Кодекс"), KeyboardButton(text="🔁 Срыв")],
        ],
        resize_keyboard=True
    )
