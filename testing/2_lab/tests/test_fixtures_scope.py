import pytest

GLOBAL_VALUE = 1


# Для прикладу це оже бути лічильник запуску частин тестів, який буде змінюватися під час виконання тестів.
@pytest.fixture(scope="session")
def default_value():
    return {"value": GLOBAL_VALUE}

@pytest.fixture(scope="function")
def increment_in_function(default_value):
    default_value["value"] += 1
    return default_value

@pytest.fixture(scope="function")
def increment_with_yield(default_value):
    default_value["value"] += 1
    yield default_value
    # Цей код виконається після завершення тесту
    default_value["value"] -= 2

@pytest.fixture(scope="function")
def decrement_default_value(default_value):
    default_value["value"] -= 1
    return default_value

def test_first_invoke(default_value):
    # При першому виклику тут буде значення 1, бо це перший виклик фікстури default_value
    assert default_value["value"] == 1


def test_second_invoke(increment_with_yield):
    assert increment_with_yield["value"] == 2
    # Після завершення цього тесту, значення default_value["value"] буде зменшено на 2, 
    # тому наступний виклик фікстури default_value поверне значення 0

def test_after_yield(default_value):
    # Після завершення попереднього тесту, значення default_value["value"] буде зменшено на 2, 
    # тому тут буде значення 0
    assert default_value["value"] == 0

def test_third_invoke(increment_with_yield, decrement_default_value):
    # Пікстури запускаються в порядку їх оголошення, тому спочатку виконається increment_with_yield,
    # а потім decrement_default_value. 
    # 0 + 1 - 1 = 0
    assert increment_with_yield["value"] == 0
    assert decrement_default_value["value"] == 0


def test_fourth_invoke(default_value):
    # Через yield у фікстурі increment_with_yield, значення default_value["value"] було зменшено на 2 після завершення
    #  тесту test_second_invoke,
    # 0 - 2 = -2
    assert default_value["value"] == -2

@pytest.mark.skip(reason="Цей тест пропускається, бо він не потрібен для демонстрації роботи фікстур")
def test_pass():
    assert False, "Цей тест пропускається, бо він не потрібен для демонстрації роботи фікстур"

@pytest.mark.skipif(GLOBAL_VALUE < 0, reason="Цей тест пропускається, бо GLOBAL_VALUE менше 0")
def test_skipif():
    assert True, "Цей тест пропускається, бо GLOBAL_VALUE менше 0"
