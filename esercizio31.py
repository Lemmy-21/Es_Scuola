numero = int(input("numero:\n"))
binari = []

while numero != 0:
    binari.append(numero%2)
    numero = int(numero/2)

binari.reverse()
print("il binario del tuo numero è", binari)