def sravnenie(a, b):
    if a == "Камінь" and b == "Ножиці":
        return a
    elif a == "Камінь" and b == "Папір":
        return b 
    elif a == "Ножиці" and b == "Камінь":
        return b
    elif a == "Ножиці" and b == "Папір":
        return a
    elif a == "Папір" and b == "Камінь":
        return a
    elif a == "Папір" and b == "Ножиці":
        return  b  