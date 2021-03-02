'''

[ es 25 - pag 190 ]
Visualizza i voti assegnati a 30 studenti tramite un dizionario
che ha come chiavi le matricole e come valori i voti,
poi elenca i voti in ordine crescente e visualizza
tutti i voti che sono stati dati, riducendo a 1 gli uguali.

'''

print("Inserire il nome dello studente e il voto assegnato separandoli con uno spazio/ es. (Marco 8),\
premere 'INVIO' se si ha finito.")

giudizi = {}
voti_dati = []

while True:
    stud_voto = input('inserire studente e voto\n').split(' ')
    if stud_voto == ['']:
        break
    else:
        giudizi[stud_voto[0]] = stud_voto[1]

ord_voti = sorted(giudizi.values())

for i in range(len(ord_voti)):
    if ord_voti[i] not in voti_dati:
        voti_dati.append(ord_voti[i])

print('Tutti i voti assegnati in ord. crescente sono', ord_voti)
print('I voti assegnati sono', voti_dati)


''' 

[ es 26 - pag 190 ]
Tramite il dizionario dell'es precedente elenca
gli studenti che hanno ottenuto un voto superiore 
alla media generale.

'''


studenti = list(giudizi)
somma = 0

for i in range(len(giudizi)):
    somma += int(ord_voti[i])
media = int(somma/len(giudizi))

for i in range(len(giudizi)):
    if int(giudizi[studenti[i]]) > media:
        print(studenti[i])
