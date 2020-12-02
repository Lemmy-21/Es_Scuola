studenti = []
lanci = []
vincitori = []



start = int(input("quanti studenti vuoi immettere?\n\n"))
for i in range(start):
    studente = input("studente\n\n")
    lancio = int(input("lancio\n\n"))
        
    studenti.append(studente)
    lanci.append(lancio)

lancio_max = max(lanci)
massimi = lanci.count(lancio_max)

'''for i in range(massimi):
    
    index_pos = lanci.index(lancio_max)
    vincitore = studenti[index_pos]
    vincitori.append(vincitore)
    lanci.remove(lanci[index_pos])
    studenti.remove(studenti[index_pos])
    '''


for i in range(len(lanci)):
    if lanci[i] == lancio_max:
        vincitori.append(studenti[i])
        
print("ha/hanno vinto:", vincitori, "facendo", lancio_max)


