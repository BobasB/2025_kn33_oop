# Встановлення та налаштування

## Вимоги до системи

- Python >= 3.13
- pip (менеджер пакетів Python)
- poetry (опціонально, для роботи з poetry)

## Варіанти встановлення

### Варіант 1: Використання venv

#### 1. Створення віртуального середовища

```bash
python -m venv ./my_env
```

#### 2. Активація середовища

**Для Windows:**
```bash
source my_env/Scripts/activate
```

**Для Linux/MacOS:**
```bash
source ./my_env/bin/activate
```

#### 3. Встановлення залежностей

```bash
pip install jikanpy-v4 Flask
```

#### 4. Збереження залежностей

```bash
pip freeze > requirements.txt
```

#### 5. Встановлення з файлу requirements.txt

```bash
pip install -r requirements.txt
```

---

### Варіант 2: Використання pipenv

#### 1. Створення середовища з певною версією Python

```bash
pipenv --python 3.13
```

#### 2. Встановлення залежностей

```bash
pipenv install
```

#### 3. Перегляд дерева залежностей

```bash
pipenv graph
```

#### 4. Активація середовища

```bash
pipenv shell
```

#### 5. Перевірка встановлених пакетів

```bash
pip list
```

#### 6. Запуск програми

```bash
python anime.py
```

#### 7. Деактивація середовища

```bash
deactivate
```

#### Пошук вразливостей

```bash
pipenv check --scan
pipenv audit
```

---

### Варіант 3: Використання Poetry (рекомендовано)

#### 1. Встановлення Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### 2. Ініціалізація проекту

```bash
poetry init
```

#### 3. Встановлення залежностей

```bash
poetry install
```

#### 4. Додавання нових пакетів

```bash
poetry add jikanpy-v4 Flask
```

#### 5. Перегляд дерева залежностей

```bash
poetry show --tree
```

#### 6. Активація середовища

```bash
eval $(poetry env activate)
```

#### 7. Запуск програми

```bash
python anime.py
```

#### 8. Деактивація

```bash
deactivate
```

#### Додавання залежностей для документації

```bash
poetry add --group docs mkdocs
```

#### Видалення всіх середовищ

```bash
poetry env remove --all
```

#### Встановлення лише залежностей для документації

```bash
poetry install --only docs
```

## Налаштування pyproject.toml

**Важливо!** Якщо при інсталяції виникає помилка, додайте в секцію `[tool.poetry]`:

```toml
[tool.poetry]
package-mode = false
```

## Перевірка встановлення

Після встановлення перевірте, що всі пакети встановлені коректно:

```bash
pip list
```

Очікувані пакети:
- jikanpy-v4
- Flask
- mkdocs (для групи docs)
