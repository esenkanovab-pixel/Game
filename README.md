# Quiz CRUD — Django implementation

Это готовый шаблон проекта **Django** для учебной практики — веб-игра (викторина) с CRUD-функционалом для игроков, вопросов, игровых сессий и результатов.

## Что внутри
- Django проект `quiz_project`
- Django приложение `quizapp`
- Модели: Player, Question, Session, Result
- Простые шаблоны на Bootstrap 5
- SQLite база по умолчанию (`db.sqlite3` будет создан после миграций)
- Инструкции по запуску и список рекомендуемых коммитов

## Быстрый старт (локально)
1. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции и создайте суперпользователя:
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Запустите сервер:
```bash
python manage.py runserver
```
Перейдите по адресу http://127.0.0.1:8000

## Коммиты (рекомендуемый план для GitHub)
1. `init: django project scaffold`
2. `feat: add quizapp models`
3. `feat: add CRUD views and templates for players`
4. `feat: add CRUD for questions`
5. `feat: add sessions and play logic`
6. `chore: add README and requirements`

## Примечания
- Шаблон минимален и предназначен для учебной демонстрации. Можно расширить: multiple-choice, аутентификация игроков, REST API, Docker, тесты.
- Если нужно, могу сгенерировать ZIP-архив (уже готов) и добавить более продвинутую реализацию.

