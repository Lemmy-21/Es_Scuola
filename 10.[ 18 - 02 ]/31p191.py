'''

[ es 30 - pag 191 ]
Calcola il fatturato totale e percentuale
di un'azienda che commercia in tutta Italia.

'''

tot = 0
fatt_perc = {}
fatturato = {
    'Nord': 0,
    'Centro': 0,
    'Sud': 0,
    'Isole': 0
}


incassi = input('scrivi in ordine e separando con 1 spazio gli \
incassi di Nord, Centro, Sud e isole\n').split(' ')

for i in range(4):
    tot += int(incassi[i])

for i in range(4):
    fatturato[list(fatturato)[i]] = int(incassi[i])
    fatt_perc[list(fatturato)[i]] = round(int(incassi[i]) * 100 / tot, 3)

print(tot, fatt_perc)








