import pytest

@pytest.fixture
def card_game():
    """Фікстура для створення об'єкта CardGame"""
    from lab.main import CardGame
    return CardGame()

def test_incorrect_interraction_with_fixture(card_game):
    """Тестуємо функцію incorrect_interraction на об'єкті класу CardGame з використанням фікстури"""
    # Перевірка на правильне значення
    for i in [0, 1, 5, 10]:
        assert card_game.incorrect_interraction(i) == i * 2, f"Очікуваний результат: {i * 2}, отриманий результат: {card_game.incorrect_interraction(i)}"

    # Перевірка на від'ємне значення
    for i in [-1, -5, -10]:
        with pytest.raises(ValueError):
            card_game.incorrect_interraction(i)

    # Перевірка на неправильний тип даних
    for i in ["string", 3.14, None, [], {}]:
        with pytest.raises(TypeError):
            card_game.incorrect_interraction(i)