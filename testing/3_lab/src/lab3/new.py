import random

def new_2():
    # немає тестів для цієї функції, вона не покрита coverage
    return "Це нова функція з lab3/new.py"

def new_function() -> str:
    # тут є покриття тестами
    n = random.randint(1, 100)
    return f"Повернене випадкове число: {n}"

def new_3():
    # немає тестів для цієї функції, вона не покрита coverage
    return "Це ще одна нова функція з lab3/new.py"

def new_none():
    # тут можемо протустувати що код був запущений, але функція повертає None
    a = 10
    b = a + 1

def new_4():
    # немає тестів для цієї функції, вона не покрита coverage
    return "Це четверта нова функція з lab3/new.py"
