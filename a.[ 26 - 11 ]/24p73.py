'''

[es 24 - pag 73]
Alla fine della giornata di elezioni per il balottaggio tra due candidati, 
siacquisiscono i voti ottenuti dai candidati. Scrivi il programma che calcoli 
le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore.

'''

voti_1 = int(input("voti del primo candidato\n"))
voti_2 = int(input("voti del secondo candidato\n"))

voti_tot = voti_1 + voti_2
voti_1_percent = int((voti_1/ voti_tot )* 100)
voti_2_percent = (100 - voti_1_percent)

if voti_1_percent > voti_2_percent:
    print("ha vinto il candidato 1 con il", voti_1_percent, "%", "dei voti, il candidato 2 ha quindi ottenuto il", voti_2_percent, "%", "dei voti")
elif voti_2_percent > voti_1_percent:
    print("ha vinto il candidato 2 con il", voti_2_percent, "%", "dei voti, il candidato 1 ha quindi ottenuto il", voti_1_percent, "%", "dei voti")
else:
    print("pareggio")



