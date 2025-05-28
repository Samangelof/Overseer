import os


project_path = "reboot_bot"

base_dirs = [
    "core/handlers",
    "core/middlewares",
    "core/services",
    "core/keyboards",
    "core/utils",
    "db",
    "state"
]

files = {
    "bot.py": "# Точка входа для aiogram\n",
    "config.py": "# Конфигурация проекта (dotenv, BaseSettings)\n",
    "main.py": "# Запуск приложения\n",

    "core/handlers/common.py": "# Хендлеры: /start, /help и т.п.\n",
    "core/handlers/report.py": "# Хендлеры: отчёты пользователя\n",
    "core/handlers/status.py": "# Хендлеры: статус, срывы\n",
    "core/handlers/rewards.py": "# Хендлеры: награды и достижения\n",

    "core/middlewares/auth.py": "# Middleware: авторизация или логгирование\n",

    "core/services/reporter.py": "# Бизнес-логика: работа с отчётами\n",
    "core/services/tracker.py": "# Логика расчёта прогресса\n",
    "core/services/awards.py": "# Логика поощрений\n",

    "core/keyboards/report_kb.py": "# Клавиатура для отчётов\n",
    "core/keyboards/main_menu.py": "# Главное меню\n",

    "core/utils/date.py": "# Утилиты: работа с датами\n",

    "db/database.py": "# Инициализация базы данных\n",
    "db/models.py": "# Модели: User, Report\n",
    "db/crud.py": "# CRUD-операции\n",

    "state/report_state.py": "# Состояния FSM для диалога отчёта\n",

    ".env": "# BOT_TOKEN=your_token_here\n",
    "requirements.txt": "aiogram==3.*\npython-dotenv\nSQLAlchemy\n"
}

for dir_path in base_dirs:
    full_dir_path = os.path.join(project_path, dir_path)
    os.makedirs(full_dir_path, exist_ok=True)
    print(f"Создана директория: {full_dir_path}")

for file_path, content in files.items():
    full_path = os.path.join(project_path, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Создан файл: {full_path}")

print("Структура проекта успешно создана!")