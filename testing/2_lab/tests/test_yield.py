import pytest
from lab.main import SingleCardGame
from time import sleep

pytestmark = [pytest.mark.unit, pytest.mark.uses_fixtures, pytest.mark.card_attributes]


@pytest.fixture
def single_card_game_object():
    return SingleCardGame("Epic")
    # тут ніякий код не виконується після return
    print("Цей код не виконається після return, тому що фікстура вже повернула об'єкт SingleCardGame")

# кожного разу при виклику фікстури буде створюватися новий об'єкт SingleCardGame з рідкістю "Epic"
def test_single_card_game_object_attributes(single_card_game_object):
    assert single_card_game_object.name.startswith("Epic Single Card with rarity ")
    assert single_card_game_object.attack == 5
    assert single_card_game_object.health == 30
    assert single_card_game_object.rarity in SingleCardGame.RARITY_LEVELS or single_card_game_object.rarity == "Common"

# щоб не створювати новий об'єкт при кожному виклику фікстури, 
# можна використовувати yield у фікстурі, що дозволяє створювати об'єкт один раз 
# і після цього очистити його після завершення тестів
@pytest.fixture
def single_card_game_yield():
    game = SingleCardGame("Epic")
    sleep(3)
    yield game
    # Тут можна додати код для очищення або закриття ресурсів, якщо потрібно
    print("Фікстура завершила роботу, можна почати очищення")
    del game  # видаляємо об'єкт після завершення тестів
    sleep(2)

def test_single_card_game_yield_attributes(single_card_game_yield):
    assert single_card_game_yield.name.startswith("Epic Single Card with rarity ")
    assert single_card_game_yield.attack == 5
    assert single_card_game_yield.health == 30
    assert single_card_game_yield.rarity in SingleCardGame.RARITY_LEVELS or single_card_game_yield.rarity == "Common"
    # Це неправильно, бо якщо assert не пройде, то об'єкт не буде видалений і залишиться в пам'яті
    #del single_card_game_yield  # видаляємо об'єкт після завершення тесту
    assert single_card_game_yield._internal == "Пусто|"

@pytest.fixture
def single_card_game_yield_increment(single_card_game_yield):
    single_card_game_yield.increment()
    yield single_card_game_yield
    single_card_game_yield.decrement()  # зменшуємо атаку та здоров'я після завершення тесту

@pytest.fixture
def single_card_game_yield__increment_1(single_card_game_yield_increment):
    single_card_game_yield_increment.increment()
    yield single_card_game_yield_increment
    single_card_game_yield_increment.decrement()  # зменшуємо атаку та здоров'я після завершення тесту

def test_single_card_game_yield_increment(single_card_game_yield_increment):
    assert single_card_game_yield_increment.attack == 6
    assert single_card_game_yield_increment.health == 40
    assert single_card_game_yield_increment._internal == "Пусто|Збільшено|"

def test_single_card_game_yield_increment_1(single_card_game_yield_increment_1):
    assert single_card_game_yield_increment_1.attack == 7
    assert single_card_game_yield_increment_1.health == 50
    assert single_card_game_yield_increment_1._internal == "Пусто|Збільшено|Збільшено|"

def test_single_card_game_yield_test_origin(single_card_game_yield):
    assert single_card_game_yield.attack == 5
    assert single_card_game_yield.health == 30
    assert single_card_game_yield._internal == "Пусто|"
