import random
import varianty

variki = ("Камінь", "Ножиці", "Папір")
def vibor(a):
    return random.choice(a)

print("Привіт, обери свій шлях. Для виходу напиши Вихід. Введи Статистика для перегляду статистики")
print("""На вибір дано "Камінь", "Ножиці" та "Папір".""")
status = True
win = 0
lose = 0
nichiya = 0

while status == True:
    text = input("Очікування вводу:")
    konest = vibor(variki)
    if text == "Вихід":
        status = False
    elif text == "Статистика":
        print("У вас {0} перемог та {1} поразок.".format(win, lose), "Також у вас {0} нічиїх.".format(nichiya))
    elif text not in variki:
        print("Помилка введення")
    elif text == konest:
        nichiya += 1
        print("Нічия))")
    elif text != konest:
        a = varianty.sravnenie(text, konest)
        if a == text:
            win += 1
            print("Перемога!")
        else:
            lose += 1
            print("Випробуй удачу ще раз)")
else:
    print("Бувай")