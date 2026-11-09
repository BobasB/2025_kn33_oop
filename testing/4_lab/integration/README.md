## Інтеграційний тест для перевірки роботи SQL-запитів у нашому додатку.

> просто запуск програми, яка виконує SQL-запити та перевіряє їх результати.
```
cd testing/4_lab/integration
poetry install
poetry run python -m integration
```

> запуском тестів через pytest
```
cd testing/4_lab/integration
poetry install
poetry run pytest -v
```