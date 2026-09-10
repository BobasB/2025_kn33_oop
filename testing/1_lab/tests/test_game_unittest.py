import unittest

from lab1.game import CardGame


class TestCardGame(unittest.TestCase):
    def test_card_game(self):
        obj = CardGame()

        self.assertIsInstance(obj, CardGame, "Об'єкт не є екземпляром класу CardGame")
        self.assertIsInstance(obj.CARD_NAMES, list, "CARD_NAMES не є списком")
        self.assertGreater(len(obj.CARD_NAMES), 0, "CARD_NAMES не може бути порожнім")
        self.assertTrue(False, "Тестування завершено успішно. Клас CardGame працює коректно.")


if __name__ == "__main__":
    unittest.main()