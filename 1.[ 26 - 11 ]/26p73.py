'''

[es 26 - pag 73]
Calcola la media degli stipendi dei dipendenti di un'azienda,
acquisiti con una ripetizione fino a quando si inserisce il 
valore -1 per segnalare la fine dell'input dei dati.

'''
stipendi = []
count = 0
somma = 0

while True:

    stipendio = int(input("stipendio\n"))
    if stipendio != 1:
        stipendi.append(stipendio)
    else: 
        break

while count < len(stipendi):

    somma += stipendi[count]
    count += 1

media = somma/ len(stipendi)

print("la media è ", media)
