from lab.main import CardGame
import pytest

@pytest.fixture
def object_fixture():
    return CardGame()


def test_compare_input_arguments(object_fixture):
    #for a, b in [(5, 3), (4, 2), (7, 7), (10, 1), (0, -5)]:
    for a, b in [(5, 3), (4, 2), (10, 1), (0, -5)]:
        assert object_fixture.compare_input_arguments_original(a, b) == a, f"Впало бо {a} <= {b} (очікуємо {a} > {b})"


@pytest.mark.parametrize("a, b", [(5, 3), (-4, -8), (100, 1), (0, -5)])
def test_compare_input_arguments_parametrized(object_fixture, a, b):
    assert object_fixture.compare_input_arguments_original(a, b) == a, "Перше число не більше другого"
    assert object_fixture.compare_input_arguments_reduced(a, b) == a, "Перше число не більше другого"


@pytest.mark.parametrize("a, b", [(7,7), (0, 0), (-5, -5)])
def test_compare_input_arguments_equal(object_fixture, a, b):
    assert object_fixture.compare_input_arguments_original(a, b) is None, "Набори не рівні, очікуємо None"
    assert object_fixture.compare_input_arguments_reduced(a, b) is None, "Набори не рівні, очікуємо None"
