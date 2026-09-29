from lab.main import CardGame
import pytest

def test_obj_incorrect_interraction_correct_return():
    """Тестуємо функцію incorrect_interraction на об'єкті класу CardGame"""
    card = CardGame()
    # Перевірка на правильне значення
    
    for i in [0, 1, 5, 10]:
        assert card.incorrect_interraction(i) == i * 2, f"Очікуваний результат: {i * 2}, отриманий результат: {card.incorrect_interraction(i)}"

    # убезпечуємо себе від неправильних арифметичних операцій, використовуючи кортежі для тестування
    test_tuples = [(0, 0), (1, 2), (5, 10), (10, 20)]
    for input_value, expected_output in test_tuples:
        assert card.incorrect_interraction(input_value) == expected_output, f"Очікуваний результат: {expected_output}, отриманий результат: {card.incorrect_interraction(input_value)}"

def test_obj_incorrect_interraction_value_error():
    """Тестуємо функцію incorrect_interraction на об'єкті класу CardGame"""
    card = CardGame()
    # Перевірка на від'ємне значення
    for i in [-1, -5, -10]:
        with pytest.raises(ValueError):
            card.incorrect_interraction(i)

def test_obj_incorrect_interraction_type_error():
    """Тестуємо функцію incorrect_interraction на об'єкті класу CardGame"""
    card = CardGame()
    # Перевірка на неправильний тип даних
    for i in ["string", 3.14, None, [], {}]:
        with pytest.raises(TypeError):
            card.incorrect_interraction(i)
