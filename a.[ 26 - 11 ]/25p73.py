'''

[es 25 - pag 73]
A un concorso pubblico hanno partecipato due candidati 
prima in ordine alfabetico e poi in ordine decrescente 
di punteggio.

'''
nome_1 = input("nome primo candidato\n").upper()
nome_2 = input("nome seconddo candidato\n").upper()
lista = [nome_1, nome_2]
voti_1 = int(input("voti del primo candidato\n"))
voti_2 = int(input("voti del secondo candidato\n"))

voti_tot = voti_1 + voti_2
voti_1_percent = int((voti_1/ voti_tot )* 100)
voti_2_percent = (100 - voti_1_percent)

lista.sort()


print("i candidati in ordine alfabetico sono", lista, "\n")

if voti_1_percent > voti_2_percent:
    print("ha vinto", nome_1,"con il", voti_1_percent, "%", "dei voti", nome_2, "ha quindi ottenuto il", voti_2_percent, "%", "dei voti")
elif voti_2_percent > voti_1_percent:
    print("ha vinto", nome_2, "con il", voti_2_percent, "%", "dei voti", nome_1, "ha quindi ottenuto il", voti_1_percent, "%", "dei voti")
else:
    print("pareggio")

