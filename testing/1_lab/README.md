# Тестування

Команди потрібно виконувати з каталогу `testing/1_lab`.

## Встановлення залежностей

```bash
poetry install
```

## Запуск тестів

Запуск тесту, налаштованого як Poetry-скрипт:

```bash
poetry run test
```

Запуск тесту у форматі `unittest`:

```bash
PYTHONPATH=src python -m unittest tests.test_game_unittest -v
```

Або запуск unittest через автоматичне пошуку тестів:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_game_unittest.py" -v
```
