'''

[ es 29 - pag 190 ]
calcola le imposte sul reddito basandoti 
sui valori della tabella del libro

'''

imposte = {
    15000: 23,
    28000: 27,
    55000: 38,
    75000: 41,
    10**12: 43,
}

imposta = 0
stip = int(input("a quanto ammonta lo stipendio mensile?\n"))

if stip < 10**12:

    for i in range(len(imposte)):
        fascia = list(imposte)[i]
        fascia_prec = list(imposte)[i-1]

        if stip > fascia - fascia_prec:

            if i == 0:
                imposta += fascia * list(imposte.values())[i] / 100
                stip -= fascia
            else:
                imposta += (fascia - fascia_prec) * list(imposte.values())[i] / 100
                stip -= fascia - fascia_prec

        else:
            imposta += stip * list(imposte.values())[i] / 100
            stip = 0
    print(imposta)
    
else:
    print('dichiari troppo: inizia ad evadere le tasse')           

            

