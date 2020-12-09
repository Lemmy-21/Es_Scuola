parola = input("inserisci una parola\n").lower()
lettere = []
lett_rev = []

for l in parola:
    lettere.append(l)
    lett_rev.append(l)

lett_rev.reverse()

if lettere == lett_rev:
    print(parola, "è una parola palindroma\n")
else:
    print(parola,"non è una palindroma\n")

print(lettere)
print(lett_rev)
