# Описание

Пульт охраны банка. Скрипт только производит выборку из данных БД.

### Как установить

1. Python3 должен быть уже установлен.

2. Склонировать проект и установить зависимости.

```
git clone https://github.com/dej-e/django-orm-watching-storage.git
cd django-orm-watching-storage
pip install -r requirements.txt
```

3. После клонирования проекта создайте в корень файл ```.env``` с таким содержимым.

```
DB_HOST=__your_host__
DB_PORT=__your_port__
DB_NAME=__your_name__
DB_USER=__your_username__
DB_PASSWORD=__your_password__
```

### Пример запуска

```
python main.py
```

Далее перейти по адресу http://127.0.0.1:8000/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
