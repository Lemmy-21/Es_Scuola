'''
[es 33 - pag 191]
Crea un programma che dia l'ordine con cui devono essere
visitati dei pazienti secondo l'ordine con cui sono arrivati.

'''

attesa = []

print("Elenca uno a uno l'ordine con cui arrivano i pazienti, \
se non ne arrivano piu' digita 'N'")

while True:
    paziente = input('nome del paziente\n').capitalize()
    if paziente == 'N':
        break
    else:
        attesa.append(paziente)

print("un qualsiasi tasto per visualizzare il prossimo in coda,\
altrimenti premere 'N' per uscire")

for i in range(len(attesa)):
    queue = input('prossimo in coda:\n').capitalize()
    if queue == 'N':
        break
    else:
        print(attesa.pop(0))
        


