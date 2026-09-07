import random

class CardGame:
    CARD_NAMES = ["Flame Dragon", "Ice Golem", "Thunder Phoenix", "Shadow Assassin", "Earth Titan"]
    def __init__(self):
        self.name = random.choice(CardGame.CARD_NAMES)
        self.attack = random.randint(1, 10)
        self.health = random.randint(20, 40)
    
    def hit_another_card(self, other_card):
        if isinstance(other_card, CardGame):
            current_attack = self.__calculate_critical_damage(self.attack)
            other_card.health -= current_attack
        else:
            print("Ми можемо атакувати лише інші карти!")
            return
        print(f"""
{self.name} нанесла {other_card.name} удар {current_attack}.
    {self.name} здоровя: {self.health} 
    {other_card.name} здоров'я: {other_card.health}""")
    
    @staticmethod
    def __calculate_critical_damage(base_damage):
        "Це статичний і щей приватний метод"
        if random.random() < 0.2:  # 20% chance for a critical hit
            print(f"Наносимо критичний удар!")
            return base_damage * 2
        if random.random() < 0.1:
            print(f"Противник ухилився від удару!")
            return base_damage * 0.5
        if random.random() < 0.05:
            print(f"Ми зашпортались і промазали!")
            return 0
        return base_damage

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