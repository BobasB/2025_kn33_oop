import random

class CardGame:
    CARD_NAMES = ["Flame Dragon", "Ice Golem", "Thunder Phoenix", "Shadow Assassin", "Earth Titan"]
    def __init__(self):
        """
        Ініціалізація об'єкта CardGame з трьома атрибутами: name, attack та health.
        """
        self.name = random.choice(CardGame.CARD_NAMES)
        self.attack = random.randint(1, 10)
        self.health = random.randint(20, 40)
        self._crit_chance = 3/7
    
    def hit_another_card(self, other_card):
        if isinstance(other_card, CardGame):
            current_attack = self.__calculate_critical_damage(self.attack)
            other_card.health -= current_attack
        else:
            msg = "Ми можемо атакувати лише інші карти!"
            print(msg)
            return msg
        print(f"""
{self.name} нанесла {other_card.name} удар {current_attack}.
    {self.name} здоровя: {self.health} 
    {other_card.name} здоров'я: {other_card.health}""")
    
    @staticmethod
    def __calculate_critical_damage(base_damage):
        "Це статичний і щей приватний метод"
        if random.random() < 3/7:  # 20% chance for a critical hit
            print(f"Наносимо критичний удар!")
            return base_damage * 2
        if random.random() < 0.1:
            print(f"Противник ухилився від удару!")
            return base_damage * 0.5
        if random.random() < 0.05:
            print(f"Ми зашпортались і промазали!")
            return 0
        return base_damage

    def incorrect_interraction(self, i: int):
        """
        Метод для демонстрації неправильної взаємодії з об'єктом.
        """
        if i < 0:
            raise ValueError("Значення не може бути від'ємним!")
        if not isinstance(i, int):
            raise TypeError("Значення повинно бути цілим числом!")
        return i * 2

    def example_with_input(self):
        """
        Метод для демонстрації взаємодії з користувачем через input.
        """
        user_input = input("Введіть число: ")
        try:
            number = int(user_input)
            print(f"Ви ввели число: {number}")
        except ValueError:
            return 1

def main():
    c = CardGame()
    print(f"{c.name} з характеристиками: атака {c.attack}, здоровя {c.health}")
    d = CardGame()
    print(f"{d.name} з характеристиками: атака {d.attack}, здоровя {d.health}")


    for turn in range(5):
        print(f"Хід {turn + 1}:")
        cards = [c, d]
        random.shuffle(cards)
        print(f"{cards[0].name} атакує першим!")
        cards[0].hit_another_card(cards[1])
        print(f"{cards[1].name} атакує другим!")
        cards[1].hit_another_card(cards[0])

if __name__ == "__main__":
    main()