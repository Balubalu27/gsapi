Проект в рамках тестового задания компании Каналсервис.

Для запуска проекта необходимо использователь Docker (https://www.docker.com/get-started/)

Когда Docker будет успешно установлен необходимо, находясь в корневой директории (simple_stripe), 
воспользоваться командой docker-compose build для создания образа проекта.

После сборки образа воспользоваться командой docker-compose up. 

Запустятся 2 контенера: 
google_sheets_api - контейнер с джанго проектом 
google_sheets_api-pg_db-1 - контейнер с PostgreSQL. 

Сервер будет автоматически запущен, для проверки можно перейти на url http://127.0.0.1:8000/admin. 
Если панель администратора открывается - значит проект успешно запущен.

Для запуска скрипта, отслеживающего изменения в GoogleSheets необходимо выполнить команду:
docker exec -it google_sheets_api python /usr/src/google_sheets_api/sheets_app/db_update.py

Для проверки значений в БД можно воспользоваться панелью администратора, предварительно его создав:
docker exec -it google_sheets_api python /usr/src/google_sheets_api/manage.py createsuperuser 

А также на главной странице:
http://127.0.0.1:8000

По вопросам можно обращаться в Telegram @Balu_user или на почту balushow123@gmail.com.
