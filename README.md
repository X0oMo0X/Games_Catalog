# Gamer Catalog API

REST API для управления и пользованием играми на FastAPI + SQLAlchemy + SQLite.

## 🚀 Быстрый старт

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone <ваш-репозиторий>
   cd games_catalog_api

> 2. Создайте и активируйте виртуальное окружение (рекомендуется):
>    
>    
>    python -m venv venv
>    
>    * Для Windows:
>    
>    venv\Scripts\activate
>    
>    * Для Linux/Mac:
>    
>    source venv/bin/activate
>    
>
> 3. Установите зависимости:
>    
>    
>    pip install -r requirements.txt
>    
>    Если файла requirements.txt нет, установите вручную:
>    
>    pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose pydantic
>    

>
> 4. Запустите приложение:
>    
>    
>    uvicorn app.main:app --reload
>    
>    Приложение будет доступно по адресу: http://127.0.0.1:8000/
>
> 5. Документация API:
>    
>    Swagger UI: http://127.0.0.1:8000/docs  <br> ReDoc: http://127.0.0.1:8000/redoc
>  
>    
>
>## 🧪 Запуск тестов
>    
>    $env:PYTHONPATH = "."
>    pytest
>    
>## 📂 Структура проекта
games_catalog_api/<br>
│<br>
├── app/<br>
│   ├── routers/<br>
│   │   └── __init__.py<br>
│   ├── crud.py<br>
│   ├── database.py<br>
│   ├── main.py<br>
│   ├── models.py<br>
│   ├── schemas.py<br>
│   └── security.py<br>
│<br>
├── games.db<br>
└── requirements.txt<br>
 Основные возможности
Регистрация и аутентификация пользователей (JWT)

CRUD операции для:

Разработчиков игр (Developers)

Игр (Games)

Отзывов (Reviews)

Связи между сущностями:

Разработчик → Игры (один-ко-многим)

Игра → Отзывы (один-ко-многим)

Документированное API с автоматической генерацией документации
>##  Примечания
По умолчанию используется SQLite (games.db)

Все данные хранятся локально, база создаётся автоматически при первом запуске

Для доступа к защищённым эндпоинтам требуется JWT-токен (получается при логине)
>##  Частые команды
Запуск сервера:

bash
uvicorn main:app --reload
Инициализация базы данных (создание таблиц):

bash
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
>## 📝 Автор
> <b> Пупков Илья Константинович
