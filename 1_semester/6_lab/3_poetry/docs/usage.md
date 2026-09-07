# Використання проекту

## Робота з модулем anime.py

Модуль `anime.py` демонструє роботу з Jikan API для отримання інформації про персонажів аніме.

### Запуск

```bash
python anime.py
```

### Що робить програма

1. Створює екземпляр Jikan API клієнта
2. Отримує інформацію про персонажів аніме (ID: 57658)
3. Виводить дані про персонажів у консоль

### Приклад коду

```python
from jikanpy import Jikan

jikan = Jikan()
j = jikan.anime(57658, extension='characters')
print(j["data"])
```

### Структура відповіді API

Відповідь містить масив `data` з інформацією про персонажів:
- `mal_id` - унікальний ідентифікатор
- `name` - ім'я персонажа
- `role` - роль в аніме
- `favorites` - кількість користувачів, що додали в обране

---

## Робота з модулем app.py (Flask)

Модуль `app.py` демонструє створення Flask веб-додатку з використанням змінних оточення.

### Налаштування змінних оточення

Створіть файл `.env` в кореневій директорії проекту:

```env
ENV_NAME=production
URL=https://api.example.com
```

### Запуск Flask додатку

```bash
# Активуйте віртуальне середовище
pipenv shell
# або
eval $(poetry env activate)

# Запустіть додаток
python app.py
```

### Що робить програма

1. Читає змінну оточення `ENV_NAME`
2. Читає URL з змінної `URL`
3. Виконує HTTP-запити за допомогою `httpx` та `requests`
4. Виводить HTTP статус-коди відповідей

### Приклад коду

```python
import os
import httpx
import requests

print(f"Environment: {os.getenv('ENV_NAME')}")

url = os.getenv('URL')

# Використання httpx
r = httpx.get(url)
print(r.status_code)

# Використання requests
r = requests.get(url)
print(r.status_code)
```

---

## Робота з документацією MkDocs

### Запуск локального сервера документації

```bash
# Встановіть залежності для документації
poetry install --with docs

# Запустіть сервер
mkdocs serve
```

Документація буде доступна за адресою: `http://127.0.0.1:8000`

### Збірка статичної документації

```bash
mkdocs build
```

Статичні HTML файли будуть згенеровані в папці `site/`.

### Деплой документації на GitHub Pages

```bash
mkdocs gh-deploy
```

---

## Управління залежностями

### Додавання нової бібліотеки

```bash
# За допомогою poetry
poetry add <package-name>

# За допомогою pipenv
pipenv install <package-name>

# За допомогою pip
pip install <package-name>
pip freeze > requirements.txt
```

### Оновлення залежностей

```bash
# Poetry
poetry update

# Pipenv
pipenv update
```

### Видалення бібліотеки

```bash
# Poetry
poetry remove <package-name>

# Pipenv
pipenv uninstall <package-name>
```

---

## Перевірка безпеки

### Аудит залежностей

```bash
# Pipenv
pipenv check --scan
pipenv audit

# Poetry (вимагає додаткового плагіна)
poetry show --outdated
```

---

## Типові проблеми та їх вирішення

### Проблема: Poetry не може встановити залежності

**Рішення:** Додайте `package-mode = false` в `pyproject.toml`:

```toml
[tool.poetry]
package-mode = false
```

### Проблема: Модуль не знайдено

**Рішення:** Переконайтесь, що віртуальне середовище активоване:

```bash
# Перевірка
which python

# Повинен вказувати на Python у віртуальному середовищі
```

### Проблема: Конфлікт версій залежностей

**Рішення:** Використовуйте `poetry show --tree` або `pipenv graph` для аналізу дерева залежностей.
