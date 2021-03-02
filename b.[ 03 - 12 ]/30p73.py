'''

[es 30 - pag 73]
Fornisci una rappresentazione in decimale di un numeri binario. 
All'inizio si richiede il numero di cifre di cui è composto il 
numero binario (lunghezza); si esegue poi una ripetizione 
che richiedere le cifre del numero binario una a una a partire 
da destra e per ciascuna calcola il prodotto della cifra binaria
per la potenza di 2 corrispondente alla posizione della cifra binaria
e aggiunge il risultato alla somma; la ripetizione viene eseguita per
il contatore che va dal valore 0 al valore di lunghezza diminuito di 1.
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita
del linguaggio per convertire un numero binario in decimale.

'''
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


