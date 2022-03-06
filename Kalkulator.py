for k in range(9999999999):
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")
    c = input("Czy mam je Dodać, Odjąć, Mnożyć czy Podzielić (D, O, M, P)? ")
    if c == "D":
        print(int(a) + int(b))
    elif c == "O":
        print(int(a) - int(b))
    elif c == "M":
        print(int(a) * int(b))
    elif c == "P":
        if int(b) == 0:
            print("Nie dzielimy przez zero!")
        else:
            print(int(a) / int(b))
    else:
        print("Nie wiem nic o takim działaniu!")
    print()
