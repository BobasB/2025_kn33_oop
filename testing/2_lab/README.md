# Pytest

Команди для налаштування середовища
```bash
poetry new .
poetry add --dev pytest
poetry install
poetry run pytest -h
```

## Маркери тестів

Маркери доступні в окремих pytest-проєктах `testing/1_lab` і `testing/2_lab`;
команди потрібно запускати з каталогу відповідного проєкту.

| Маркер | Призначення |
| --- | --- |
| `unit` | Ізольовані тести окремої одиниці поведінки |
| `card_game` | Загальні приклади для `CardGame` |
| `game_initialization` | Створення `CardGame` та його атрибути |
| `card_attributes` | Атрибути карт |
| `card_combat` | Поведінка взаємодії карт у бою |
| `input_validation` | Перевірка аргументів взаємодії |
| `input_handling` | Обробка користувацького введення |
| `comparison` | Порівняння аргументів |
| `uses_fixtures` | Тести, що використовують pytest-фікстури |
| `parameterized` | Тести з кількома наборами параметрів |

Приклади запуску з `testing/2_lab`:

```bash
poetry run pytest -m unit
poetry run pytest -m card_combat
poetry run pytest -m "card_combat or input_validation"
poetry run pytest -m "unit and uses_fixtures"
```

Для `testing/1_lab` діють ті самі маркери; перейдіть до цього каталогу
перед запуском аналогічних команд. Наприклад:

```bash
poetry run pytest -m game_initialization
poetry run pytest -m "game_initialization or card_combat"
poetry run pytest -m "unit and input_validation"
```
