from lab1.game import CardGame


def test_card_game():
    obj = CardGame()

    print("Починаємо тестування класу CardGame...")
    assert isinstance(obj, CardGame), "Об'єкт не є екземпляром класу CardGame"
    assert isinstance(obj.CARD_NAMES, list), "CARD_NAMES не є списком"
    assert len(obj.CARD_NAMES) > 0, "CARD_NAMES не може бути порожнім"
    print("Тестування завершено успішно. Клас CardGame працює коректно.")

    print("Перевірка типу CARD_NAMES...")
    if isinstance(obj.CARD_NAMES, list):
        print(f"Тест пройшов та CARD_NAMES є списком: {obj.CARD_NAMES}")
    else:
        raise AssertionError("CARD_NAMES не є списком")
    print("Тестування типу CARD_NAMES завершено успішно.")


if __name__ == "__main__":
    test_card_game()
