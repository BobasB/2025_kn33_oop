# Віртуальні середовища

### Команди в терміналі
```bash
python -m venv ./my_env
source my_env/Scripts/activate # для Windows
source ./my_env/bin/activate # для Linux/MacOS
pip list
pip install jikanpy-v4 Flask
pip freeze > requirements.txt

pip install -r requirements.txt
```

```bash
pipenv --python 3.13
pipenv install
pipenv graph

pipenv shell
pip list
python anime.py
deactivate
```