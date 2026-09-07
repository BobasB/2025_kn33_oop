import importlib

module = importlib.import_module("1_lab.game")
CardGame = module.CardGame

obj = CardGame()

print("Починаємо тестування класу CardGame...")
assert isinstance(obj, CardGame), "Об'єкт не є екземпляром класу CardGame"
assert isinstance(obj.CARD_NAMES, list), "CARD_NAMES не є списком"
assert len(obj.CARD_NAMES) > 0, "CARD_NAMES не може бути порожнім"
print("Тестування завершено успішно. Клас CardGame працює коректно.")