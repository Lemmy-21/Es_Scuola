''' 

[ es 17 - pag 189 ]
crea un nuovo dizionario ottenuto dall'es 16 invertendo pero'
chiavi e valori, e che dia il nome della nazione a partire dalla capitale

'''

nazioni = ['Italia', 'Germania', 'Moldavia', 'Congo']
capitali = ['Roma', 'Berlino', 'Chisinau', 'Kinshasa']
geo_1 = {}
geo_2 = {}

for stati in range(len(nazioni)):
    geo_1[nazioni[stati]] = capitali[stati]

for k in range(len(geo_1)):
    geo_2[list(geo_1.values())[k]] = list(geo_1)[k]

print(list(geo_2))
capitale_richiesta = input('di quale capitale vuoi sapere la nazione?\n').capitalize() 

if capitale_richiesta in geo_2:
    print('la nazione di appartenenza della', capitale_richiesta, "e':", geo_2[capitale_richiesta])
else:
    print('non è presente nella lista')
    
    



