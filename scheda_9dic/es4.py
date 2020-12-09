scelta = 5
while scelta > 4:
    scelta = int(input("che area vuoi calcolare?\n 1. Quadrato\n 2. Triangolo\n 3. Rettangolo\n 4. Cerchio\n\n"))

if scelta == 1:
    print("\n\nQUADRATO\n\n")
    lato = int(input("lato del quadrato\n"))
    area = lato*lato
    print("area =", area)
elif scelta == 2:
    print("\n\nTRIANGOLO\n\n")
    base = int(input("base del triangolo\n"))
    altezza = int(input("altezza del triangolo\n"))
    area = (base*altezza)/2
    print("area =", area)
elif scelta == 3:
    print("\n\nRETTANGOLO\n\n")
    base = int(input("base del rettangolo\n"))
    altezza = int(input("altezza del rettangolo\n"))
    area = base*altezza
    print("area =", area)
elif scelta == 4:
    print("\n\nCERCHIO\n\n")
    raggio = int(input("raggio del cerchio\n"))
    area = (raggio**2)*3.14
    print("area =", area)