nazioni = ['Italia', 'Germania', 'Moldavia', 'Congo']
capitali = ['Roma', 'Berlino', 'Chisinau', 'Kinshasa']
geo = {}

for stati in range(len(nazioni)):
    geo[nazioni[stati]] = capitali[stati]

print(nazioni)
nazione_richiesta = input('di quale nazione vuoi sapere la capitale?\n').capitalize()
if nazione_richiesta in geo:
    print('la capitale di', nazione_richiesta, "e':", geo[nazione_richiesta])
else:
    print('non è presente nella lista')