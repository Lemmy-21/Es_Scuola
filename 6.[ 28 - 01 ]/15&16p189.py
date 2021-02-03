nazioni = ['Italia', 'Germania', 'Moldavia', 'Congo']
capitali = ['Roma', 'Berlino', 'Chisinau', 'Kinshasa']
geo_1 = {}

for stati in range(len(nazioni)):
    geo_1[nazioni[stati]] = capitali[stati]

print(nazioni)
nazione_richiesta = input('di quale nazione vuoi sapere la capitale?\n').capitalize() 

if nazione_richiesta in geo_1:
    print('la capitale di', nazione_richiesta, "e':", geo_1[nazione_richiesta])
else:
    print('non è presente nella lista')