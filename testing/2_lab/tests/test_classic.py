import unittest
from lab.main import CardGame

class TestCardGame(unittest.TestCase):
    """Це класичні unitest тести"""  
    def setUp(self):
        self.game = CardGame()
        self.another_card = CardGame()

    def test_hit_another_card(self):
        """Це класичні unitest тести"""
        initial_health = self.another_card.health
        self.game.hit_another_card(self.another_card)
        self.assertLess(self.another_card.health, initial_health, "Health should decrease after being hit.")

class TestCardGameWithPytest:
    """Це pytest тести просто згруповані в клас, але без використання unittest.TestCase
    така організація дозволяє групувати тести, але pytest не потребує класів для тестів.
    """
    def test_hit_another_card(self):
        """Це pytest тест"""
        game = CardGame()
        another_card = CardGame()
        initial_health = another_card.health
        game.hit_another_card(another_card)
        assert another_card.health < initial_health, "Health should decrease after being hit."
