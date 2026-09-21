import unittest

from lab1.game import CardGame


class TestCardGameInitialization(unittest.TestCase):
    def setUp(self):
        """
        Метод setUp виконується перед кожним тестом.
        """
        print("\n--- Виконується setUp ---")
        self.card_game = CardGame()


    def tearDown(self):
        """
        Метод tearDown виконується після кожного тесту.
        """
        print("--- Виконується tearDown ---\n")
        del self.card_game

    @classmethod
    def setUpClass(cls):
        """
        Метод setUpClass виконується один раз перед усіма тестами.
        Тільки за умови що значення є ідемпотентними, тобто не змінюються під час тестів.
        """
        print("\n=== Виконується setUpClass ===")
        cls.test_names = ['name', 'attack', 'health']

    @classmethod
    def tearDownClass(cls):
        """
        Метод tearDownClass виконується один раз після усіх тестів.
        """
        print("=== Виконується tearDownClass ===\n")
        del cls.test_names

    def test_card_game(self):
        """
        Перевірка створення об'єкта CardGame та глобальних атрибутів класу.
        """
        print("!!!Тестуємо!!!")
        self.assertIsInstance(self.card_game, CardGame, "Об'єкт не є екземпляром класу CardGame")
        self.assertIsInstance(CardGame.CARD_NAMES, list, "CARD_NAMES не є списком")
        self.assertGreater(len(CardGame.CARD_NAMES), 0, "CARD_NAMES не може бути порожнім")

    def test_object_attributes(self):
        """
        Перевірка наявності атрибутів об'єкта CardGame.
        """
        
        self.assertTrue(hasattr(self.card_game, 'name'), "Об'єкт не має атрибуту 'name'")
        self.assertTrue(hasattr(self.card_game, 'attack'), "Об'єкт не має атрибуту 'attack'")
        self.assertTrue(hasattr(self.card_game, 'health'), "Об'єкт не має атрибуту 'health'")

        # буде використовуватися для демонстрації роботи unittest
        #self.assertTrue(False, "Навмисно провалений тест для демонстрації роботи unittest")

    def test_object_attributes_types(self):
        """
        Перевірка типів атрибутів об'єкта CardGame.
        """
        self.assertIsInstance(self.card_game.name, str, "Атрибут 'name' не є рядком")
        self.assertIsInstance(self.card_game.attack, int, "Атрибут 'attack' не є цілим числом")
        self.assertIsInstance(self.card_game.health, int, "Атрибут 'health' не є цілим числом")

    def test_object_attributes_with_assetrs(self):
        """
        Перевірка атрибутів об'єкта CardGame з використанням assert.
        """
        assert hasattr(self.card_game, 'name'), "Об'єкт не має атрибуту 'name'"
        assert hasattr(self.card_game, 'attack'), "Об'єкт не має атрибуту 'attack'"
        assert hasattr(self.card_game, 'health'), "Об'єкт не має атрибуту 'health'"

    def test_object_attributes_values(self):
        """
        Показати похибку при обчисленні
        """
        #assert self.card_game._crit_chance == 0.428571428571428571, "Атрибут '_crit_chance' не дорівнює 1/3"
        self.assertAlmostEqual(self.card_game._crit_chance, 3/7, places=5, msg="Атрибут '_crit_chance' не дорівнює 3/7")



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