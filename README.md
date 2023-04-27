# Проект интернет-зоомагазина

### Модели:
Catalog:
* Category(-+-)
* Item(-+-)

Cart:
* Position(-+-)
* Order(-+-)
* Cart(-+-)

###### Легенда:
* `первый плюс - наличие views, templates и urls для CRUD`
* `второй плюс - наличие модели в админке`
* `третий плюс - запросы к БД оптимизированы`

#### Для самостоятельного запуска в тестовом режиме:
* Установить зависимости командой `python -m pip install -r requirements.txt`
* Создать файлы миграций для БД командой `python manage.py makemigrations`
* Применить миграции БД командой `python manage.py migrate`
* Создать супер-пользователя для доступа к админ-панели командой `python manage.py createsuperuser`
* Запустить сервер командой `python manage.py runserver`

### Необходимые ссылки для обзора проекта:
* Панель администратора - http://127.0.0.1:8000/admin
* Главная страница сайта - http://127.0.0.1:8000
