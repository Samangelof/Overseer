# REBOOT.OPS — Боевой Telegram-Бот Самодисциплины

**REBOOT.OPS** — тактический интерфейс для контроля состояния, поведения и выполнения протоколов спецоперации "REBOOT". Он не друг. Он не враг. Он система. Бот служит интерфейсом между тобой (юнитом M-23) и твоими ежедневными обязанностями.

---

## 📍 Цель проекта

Создать осознанную систему самоконтроля с автоматизированной обратной связью:

- Протокол дисциплины
- Слежение за ежедневным прогрессом
- Поддержка восстановления после срывов

---

## ⚙️ Стек технологий

- `aiogram 3.x`
- `SQLAlchemy 2.x` (async)
- `Alembic`
- `SQLite` (по умолчанию)

---

## 📅 Роадмап взаимодействия (день юнита)

### ☑️ `/start` — запуск бота

- Приветствие в стиле боевого интерфейса
- Вывод краткой информации
- Клавиатура: `📊 Отчет | 📈 Статус | 🧠 Кодекс | 🔁 Срыв`

### ⏰ Утро: напоминание

- Автоматическое сообщение: `"Юнит M-23. Новый день. Время выполнить протокол."`
- Кнопка запуска `/отчет`

### 🧾 `/отчет` — боевой протокол дня

FSM с пошаговым вводом:

1. Был ли срыв?
2. Сколько раз принял душ?
3. Сколько часов работал?
4. Настроение (0–10)
5. Свободный комментарий

**После:**

- Сохранение в БД (`DailyReport`)
- Вывод: % выполнения + краткий вердикт

### 📈 `/статус` — отчет о прогрессе

- Сводка по последней неделе:
  - Дни с протоколом
  - Срывы
  - Душ / работа / настроение

### 🧠 `/кодекс` — философия REBOOT

- Вывод установок:
  - "Я не животное. Я сознание."
  - "Я человек чести."
  - "Я не тюрьма. Я оружие."

### 🔁 `/срыв` — восстановительный протокол

- Без осуждения:
  - Фраза поддержки
  - План восстановления (душ, пауза, осмысление)
  - Закрытие: "Система вновь активна."

### 🏅 `/награда` — внутренняя мотивация

- 7 дней подряд: достижение стабильности
- 30 дней: достижение контроля

### ⌛ Вечер: автоматическое напоминание

- Если до 21:00 нет отчета:

```
Внимание. Протокол не завершен.
Ты обязан подать отчет. Устав — не просьба.
```

---

## 🔐 База данных (SQLite)

- `User`: хранит юнита
- `DailyReport`: ежедневные значения по дисциплине

---

## 🧩 Дополнительно

| Функция                        | Реализация                                                    |
| ------------------------------------- | ----------------------------------------------------------------------- |
| Автонапоминания        | `APScheduler` или `asyncio` циклы                           |
| История отчетов         | SELECT + фильтрация по дате                             |
| Механика достижений | Подсчет подряд дней + отметка в таблице |

---

## ⛓ Следующий шаг:

1. `/start` + welcome клавиатура
2. FSM для `/отчет`
3. Подключение `/статус`

REBOOT.OPS в действии. Юнит M-23, протокол активен.
