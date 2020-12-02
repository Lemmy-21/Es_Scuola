
''''
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

'''

def convertitore(num):
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else:
        dec_bin(num)

def dec_bin(num):
    if num > 1:
        dec_bin(num/2)

print(num,%2, end = "")

