'''

[ es 27 - pag 190 ]
Crea una rubrica telefonica e tramite il nome 
del contatto visualizza il numero oppure un messaggio,
nel caso non sia prensente.

'''

rubrica = {
    'Marco': '0522 420 777',
    'Luca': '0542 619 008',
    'Idraulico': '0522 568 991',
    'Bruno': '0810 556 892'
}

for i in range(len(rubrica)):
    indice = str(i+1) + '.'
    print(indice, list(rubrica)[i])

while True:
    persona = input('chi vuole visualizzare?\n').capitalize()
    if persona in rubrica:
        print(persona, ':', rubrica[persona])
    elif persona == '':
        break
    else:
        print('Non presente in rubrica')

