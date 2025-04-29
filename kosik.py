nabidka = ["Velikonoční beránek", "Vajíčka", "Pomlázky", "Čokoláda", "Kinder vajíčka"]
kosik = []

print("Vítejte v aplikaci Koledník")

while True: 
    print("Ahoj koledníku, co bys rád do košíku?")
    print("-----------------------------------------")
    print("Zde máme výběr: ")

    for i in range(len(nabidka)): 
        print(f"{i+1}. {nabidka[i]}")

    volba = input("Zadejte vaší volbu koledy: ")

    volba_int = -1
    if volba.isdigit():
        volba_int = int(volba)

    for i in range(len(nabidka)):
        if volba == nabidka[i-1] or volba_int == i: 
            kosik.append(nabidka[i-1])
            nabidka.pop(i-1)
            break
    else: 
        print("Tohle v nabídce nemáme :(")

    print("-----------------------------------------")
    print("Obsah vašeho košíku: ")
    for i in range(len(kosik)): 
        print(f"{i+1}. {kosik[i]}")