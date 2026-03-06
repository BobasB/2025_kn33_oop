# Опис модулів та API

## Структура проекту

Проект складається з двох основних модулів, що демонструють різні аспекти роботи з зовнішніми API та веб-фреймворками.

---

## Модуль anime.py

### Призначення

Демонстрація роботи з Jikan API (неофіційний REST API для MyAnimeList) для отримання інформації про аніме та персонажів.

### Залежності

```python
from flask import Flask, render_template
from jikanpy import Jikan
```

### Основні компоненти

#### Jikan Client

```python
jikan = Jikan()
```

Створює екземпляр клієнта для взаємодії з Jikan API.

#### Flask Application

```python
app = Flask(__name__)
```

Ініціалізує Flask додаток (закоментовано в поточній версії).

### API запити

#### Отримання інформації про персонажів

```python
j = jikan.anime(57658, extension='characters')
```

**Параметри:**
- `57658` - ID аніме в базі MyAnimeList
- `extension='characters'` - розширення для отримання списку персонажів

**Повертає:**
Словник з ключем `data`, що містить масив персонажів.

### Структура відповіді

```json
{
  "data": [
    {
      "character": {
        "mal_id": int,
        "url": str,
        "images": {...},
        "name": str
      },
      "role": str,
      "favorites": int,
      "voice_actors": [...]
    }
  ]
}
```

### Закоментовані маршрути Flask

#### Головна сторінка

```python
@app.route('/')
def home():
    a = str()
    for episode in j["data"]:
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    return a
```

Генерує HTML з інформацією про епізоди.

#### Сторінка "Про нас"

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

Відображає шаблон `about.html`.

### Запуск

```python
if __name__ == '__main__':
    print(j["data"])
```

Виводить дані про персонажів у консоль.

---

## Модуль app.py

### Призначення

Демонстрація роботи зі змінними оточення та HTTP-клієнтами (httpx та requests).

### Залежності

```python
import os
import math
import httpx
import requests
```

### Робота зі змінними оточення

#### Читання змінної ENV_NAME

```python
print(f"Environment: {os.getenv('ENV_NAME')}")
```

Виводить значення змінної оточення `ENV_NAME`.

#### Читання URL

```python
url = os.getenv('URL')
```

Отримує URL з змінної оточення для виконання HTTP-запитів.

### HTTP клієнти

#### Використання httpx

```python
r = httpx.get(url)
print(r.status_code)
```

**httpx** - сучасний асинхронний HTTP-клієнт з підтримкою HTTP/2.

**Методи:**
- `get()` - виконує GET-запит
- `status_code` - HTTP статус-код відповіді

#### Використання requests

```python
r = requests.get(url)
print(r.status_code)
```

**requests** - популярна бібліотека для HTTP-запитів.

**Методи:**
- `get()` - виконує GET-запит
- `status_code` - HTTP статус-код відповіді

---

## Конфігурація проекту (pyproject.toml)

### Метадані проекту

```toml
[project]
name = "3-poetry"
version = "0.1.0"
description = "Це мій проект з poetry"
authors = [
    {name = "BobasB", email = "bugil.bogdan@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
```

### Основні залежності

```toml
dependencies = [
    "jikanpy-v4 (>=1.0.2,<2.0.0)",
    "flask (>=3.1.3,<4.0.0)"
]
```

- **jikanpy-v4**: версія 1.0.2 або новіша (але менша за 2.0.0)
- **flask**: версія 3.1.3 або новіша (але менша за 4.0.0)

### Групи залежностей

#### Група dev (розробка)

```toml
[dependency-groups]
dev = [
    "flake8 (>=7.3.0,<8.0.0)"
]
```

- **flake8**: інструмент для перевірки стилю коду

#### Група docs (документація)

```toml
docs = [
    "mkdocs (>=1.6.1,<2.0.0)"
]
```

- **mkdocs**: генератор статичної документації

---

## Зовнішні API

### Jikan API

**Базовий URL:** `https://api.jikan.moe/v4/`

#### Endpoint: Anime Characters

```
GET /anime/{id}/characters
```

Повертає список персонажів для вказаного аніме.

**Приклад відповіді:**

```json
{
  "data": [
    {
      "character": {
        "mal_id": 12345,
        "name": "Character Name",
        "images": {...}
      },
      "role": "Main",
      "favorites": 1234
    }
  ]
}
```

**Документація:** [https://docs.api.jikan.moe/](https://docs.api.jikan.moe/)

---

## Константи та налаштування

### Змінні оточення

Для коректної роботи додатку повинні бути визначені:

| Змінна | Опис | Приклад |
|--------|------|---------|
| `ENV_NAME` | Назва середовища | `development`, `production` |
| `URL` | URL для HTTP-запитів | `https://api.example.com` |

### Конфігурація Flask

```python
debug=True  # Режим налагодження (закоментовано)
```

---

## Обмеження та рекомендації

### Rate Limiting (Jikan API)

- Максимум 60 запитів на хвилину
- Максимум 3 запити на секунду
- Рекомендується кешувати відповіді

### Безпека

- Не зберігайте чутливі дані в коді
- Використовуйте `.env` файл для змінних оточення
- Додайте `.env` до `.gitignore`

### Продуктивність

- Використовуйте `httpx` для асинхронних запитів
- Кешуйте відповіді API
- Обробляйте помилки мережі належним чином
