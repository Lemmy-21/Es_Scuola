'''

[es 29 - pag 73]
Dato un elenco di città, con l'indicazione per ciascuna di esse del nome
e delle temperature massima e minima registrate in un giorno, si devono 
contare quante città hanno superato nel giorno un valore prefissato 
per l'escursione termica, ottenuta per differenza tra temperatura massima e minima.
Organizza un programma che, dopo aver richiesto il valore da controllare dell'escursione termica,
per ogni città dell'elenco ripeta la richiesta dei dati (nome, temperatura massima e minima), 
calcoli l'escursione termica e controlli se l'escursione è maggiore del valore prefissato: 
in questo caso, incrementa il contatore delle città selezionate. Alla fine della ripetizione 
comunica il numero delle città registrato nel contatore.

'''
contatore = int(input("qual è il contatore?\n"))
numb_città = int(input("quante città vuoi inserire?\n"))
città_ls = []
temp_min_ls = []
temp_max_ls = []
esc_term = []
count_cicl = 0

for i in range(numb_città):
    città = input("città\n")
    temp_min = int(input("minime\n"))
    temp_max = int(input("massime\n"))
    prec_temp_max = temp_max
    if temp_min > temp_max:
        print("le temperature sono state invertite")
        temp_max = temp_min
        temp_min = prec_temp_max
    città_ls.append(città)
    temp_min_ls.append(temp_min)
    temp_max_ls.append(temp_max)
    esc_term.append(temp_max - temp_min)

while max(esc_term) > contatore:
    contatore += 1

for i in range(numb_città):
    print("l'escursione termica di", città_ls[i], "è:", esc_term[i],"\n")

print("contatore", contatore)


