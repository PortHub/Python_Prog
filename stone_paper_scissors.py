import random
import varianty

variki = ("Камінь", "Ножиці", "Папір")
def vibor(a):
    return random.choice(a)

print("Привіт, обери свій шлях. Для виходу напиши Вихід.")
print("""На вибір дано "Камінь", "Ножиці" та "Папір".""")
status = True

while status == True:
    text = input("Очікування вводу:")
    konest = vibor(variki)
    if text == "Вихід":
        status = False
    elif text == konest:
        print("Нічия))")
    elif text != konest:
        a = varianty.sravnenie(text, konest)
        if a == text:
            print("Перемога!")
        else:
            print("Випробуй удачу ще раз)")
else:
    print("Бувай")