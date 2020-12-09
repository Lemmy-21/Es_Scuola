num_parole = int(input("quante parole vuoi inserire?\n"))
parole = []
numeri = []

for i in range(num_parole):
    parola = input("inserici una parola\n")
    parole.append(parola)

for i in range(num_parole):
    lunghezza = len(parole[i])
    numeri.append(lunghezza)

print("parole:", parole, "\nlunghezza parole:", numeri, "\n")


    