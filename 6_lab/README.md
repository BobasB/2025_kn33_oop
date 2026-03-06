# Віртуальні середовища

### Команди в терміналі
#### приклад використання venv
```bash
python -m venv ./my_env
source my_env/Scripts/activate # для Windows
source ./my_env/bin/activate # для Linux/MacOS
pip list
pip install jikanpy-v4 Flask
pip freeze > requirements.txt

pip install -r requirements.txt
```
#### приклад використання pipenv
```bash
pipenv --python 3.13
pipenv install
pipenv graph

pipenv shell
pip list
python anime.py
deactivate
```

#### Пошук вразливостей
```bash
pipenv check --scan
pipenv audit
```

#### Файл .env
```bash
pipenv shell
python app.py
deactivate
```

### Менеджмент середовищ за допомогою Poetry
- якщо при інсталяції випадє помилку, додайте `package-mode = false` в секцію
```bash
[tool.poetry]
package-mode = false
```

```bash
poetry init
poetry install

poetry add jikanpy-v4 Flask

poetry show --tree

eval $(poetry env activate)
python anime.py
deactivate 

poetry add --group dev flake8

poetry add --group docs mkdocs

poetry env remove --all
poetry install --only docs
```

## Використання АІ
- задали АІ промпт щоб він зробив документацію для проекту, і він створив її з використанням MkDocs.
```bash
cd 6_lab/3_poetry
poetry install --only docs

eval $(poetry env activate)
mkdocs serve

```
Після запуску документація доступна за адресою http://127.0.0.1:8000/

# Далі доробляєте звіт самостійно
