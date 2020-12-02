lunghezza = int(input("numero cifre\n"))
cifre = []
decimale = 0

for i in range(lunghezza):
    cifra = int(input("cifra a partire da destra\n"))
    cifre.append(cifra)

for l in range(lunghezza):
    cifr_dec = cifre[l]*(2**l)
    decimale += cifr_dec

print("il decimale di", cifre, "è:", decimale)


