from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Отчeт"), KeyboardButton(text="📈 Статус")],
            [KeyboardButton(text="📜 Кодекс"), KeyboardButton(text="🔁 Срыв")],
            [KeyboardButton(text="📅 История"), KeyboardButton(text="⚙️ Настройки")],
            [KeyboardButton(text="🧠 Советы"), KeyboardButton(text="🪪 Профиль")]
        ],
        resize_keyboard=True
    )