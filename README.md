## Проект блог-платформы с возможностью создвать посты, сгруппированные по темам

Клонировать репозиторий и перейти в него в командной строке:

```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

```

Выполнить миграции: в cd yatube

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
