[![Build Status](https://github.com/PivnoyFei/task_for_vw/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/PivnoyFei/task_for_vw/actions/workflows/main.yml)

<h1 align="center"><a target="_blank" href="">Тестовое задание для VoxWeb Interactive</a></h1>

### Стек
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.10](https://img.shields.io/badge/3.10-blue?style=flat-square&logo=3.10)
![Django](https://img.shields.io/badge/Django-171515?style=flat-square&logo=Django)![4.1.7](https://img.shields.io/badge/4.1.7-blue?style=flat-square&logo=4.1.7)
![Django Rest Framework](https://img.shields.io/badge/Django--Rest--Framework-171515?style=flat-square&logo=Django)![3.14.0](https://img.shields.io/badge/3.14.0-blue?style=flat-square&logo=3.14.0)
![SQLite](https://img.shields.io/badge/SQLite-171515?style=flat-square&logo=SQLite)
![Admin-LTE-3](https://img.shields.io/badge/Admin--LTE--3-171515?style=flat-square&logo=Admin-LTE-3)

### Описание
1. Парсер //  Спарсить с использованием языка python 10 свежих новостей со следующих telegram ресурсов, проставить тэги (ozon, yandex).
- Яндекс.Маркет — https://t.me/market_marketplace
- OZON — https://t.me/ozonmarketplace
- Новостям проставить основные тэги по названиям ресурсов и внутреннюю информацию, например время поста, ссылки на вложения(картинки)

2. Админка // Сделать на Django админку для новостей с шаблоном Admin LTE 3 и занести данные из парсера в базу sqlite.
- https://adminlte.io/themes/v3/
- https://github.com/DucThanhNguyen/MaterialAdminLTE
- https://adminlte.io/premium/

3. "*" API // Сделать простой API запрос для frontend на получение структурированных новостей в формате JSON:
- все новости по дате,
- отдельно каналы/новости по тэгам.


### Маршруты
| Название | Метод | Описание | Авторизация |
|----------|-------|----------|-------------|
| /api/news | GET  | Возвращает список новостей | Да
| /api/news | POST | Парсит новость по тегу     | Да
| /api/tags | GET  | Возвращает список тегов    | Да
| /api/tags | POST | Создает новый тег          | Да


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_for_vw.git
cd task_for_vw
```

#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

### Перед запуском сервера, в папке &lt; backend &gt; необходимо создать .env файл со своими данными. Ниже представлены параметры по умолчанию.
```bash
SECRET_KEY='key' # Секретный ключ джанго
DEBUG='True' # Режим разработчика
ALLOWED_HOSTS='localhost' # Адрес

DB_ENGINE='django.db.backends.sqlite3'
DB_NAME='db.sqlite3' # имя БД
DB_USER='user' # логин для подключения к БД
DB_PASSWORD='password' # пароль для подключения к БД
DB_HOST='localhost' # название контейнера
DB_PORT='5432' # порт для подключения к БД

API_ID = 12345 # твой telegram ID можно получить по https://my.telegram.org/auth
API_HASH = '12345sdfh' # твой telegram HASH
```

#### Чтобы сгенерировать безопасный случайный секретный ключ, используйте команду:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Создайте шаблоны:
```bash
python manage.py collectstatic --noinput
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

#### При первом запуске парсера потребует ввести номер телефона и код из телеграм:

Теперь по адресу http://localhost:8000/admin/ доступна админка.

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)
