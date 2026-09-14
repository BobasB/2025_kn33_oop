import unittest

from lab1.game import CardGame


class TestCardGameInitialization(unittest.TestCase):
    def test_card_game(self):
        """
        Перевірка створення об'єкта CardGame та глобальних атрибутів класу.
        """
        obj = CardGame()
        self.assertIsInstance(obj, CardGame, "Об'єкт не є екземпляром класу CardGame")
        self.assertIsInstance(obj.CARD_NAMES, list, "CARD_NAMES не є списком")
        self.assertGreater(len(obj.CARD_NAMES), 0, "CARD_NAMES не може бути порожнім")

    def test_object_attributes(self):
        """
        Перевірка наявності атрибутів об'єкта CardGame.
        """
        obj = CardGame()
        self.assertTrue(hasattr(obj, 'name'), "Об'єкт не має атрибуту 'name'")
        self.assertTrue(hasattr(obj, 'attack'), "Об'єкт не має атрибуту 'attack'")
        self.assertTrue(hasattr(obj, 'health'), "Об'єкт не має атрибуту 'health'")

        # буде використовуватися для демонстрації роботи unittest
        #self.assertTrue(False, "Навмисно провалений тест для демонстрації роботи unittest")

    def test_object_attributes_types(self):
        """
        Перевірка типів атрибутів об'єкта CardGame.
        """
        obj = CardGame()
        self.assertIsInstance(obj.name, str, "Атрибут 'name' не є рядком")
        self.assertIsInstance(obj.attack, int, "Атрибут 'attack' не є цілим числом")
        self.assertIsInstance(obj.health, int, "Атрибут 'health' не є цілим числом")


class TestCardGameMethods(unittest.TestCase):
    def test_hit_another_card(self):
        """
        Перевірка методу hit_another_card.
        """
        card1 = CardGame()
        card2 = CardGame()
        initial_health = card2.health
        card1.hit_another_card(card2)
        self.assertLess(card2.health, initial_health, "Здоров'я іншої карти не зменшилось після атаки")
        self.assertEqual(type(card2.hit_another_card(1)), str, "Метод hit_another_card не повертає рядок при атаці не карти")


if __name__ == "__main__":
    unittest.main(verbosity=2)