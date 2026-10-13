import pytest
from lab.main import SingleCardGame

pytestmark = [pytest.mark.unit, pytest.mark.uses_fixtures, pytest.mark.card_attributes]


# Створюємо фікстуру для створення об'єкта SingleCardGame з різними рівнями рідкості
@pytest.fixture
def default_attack():
    return 5

@pytest.fixture
def default_health():
    return 30

@pytest.fixture
def expected_rarity():
    return SingleCardGame.RARITY_LEVELS

@pytest.fixture(params=["Common", "Rare", "Epic", "Legendary", "Invalid"])
def single_card_game(request):
    return SingleCardGame(request.param)

##### Дві фікстури для створення об'єкта SingleCardGame з різними префіксами
@pytest.fixture
def default_prefixes():
    return {"rarity": "Rare", "prefix": "Epic"}

@pytest.fixture
def single_card_game_with_custom_prefix(default_prefixes):
    return SingleCardGame(default_prefixes["rarity"], unic_prefix=default_prefixes["prefix"])

@pytest.mark.parameterized
def test_single_card_game_object_with_correct_attributes(
        single_card_game, 
        default_attack, 
        default_health
        ):
    # Перевіряємо, що об'єкт створений і має правильні атрибути
    assert single_card_game.name.startswith("Epic Single Card with rarity ")
    assert single_card_game.attack == default_attack
    assert single_card_game.health == default_health
    assert single_card_game.rarity in SingleCardGame.RARITY_LEVELS or single_card_game.rarity == "Common"


def test_single_card_game_with_custom_prefix(
        single_card_game_with_custom_prefix,
        default_prefixes):
    assert " Single Card with rarity " in single_card_game_with_custom_prefix.name
    assert single_card_game_with_custom_prefix.name.startswith(default_prefixes["prefix"] + " Single Card with rarity " + default_prefixes["rarity"])


@pytest.mark.parameterized
def test_single_card_game_rarity_assignment(expected_rarity, single_card_game):
    assert single_card_game.rarity in expected_rarity
    