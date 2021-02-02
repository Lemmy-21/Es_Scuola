'''
[es 14 - pag 72]
Crea un programma che scriva la differenza 
di due numeri a e b se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10.
Esegui poi il programma con diverse coppie di valori per a e b:
(-5; 2), (5; -5), (10; 2), (-4; -5), (5; 4), (-3; -2).

'''
num_a = int(input("inserire un numero\n"))
num_b = int(input("inserirne un altro\n"))
prodotto = num_a * num_b

if prodotto > 10:
    print("la differenza dei numeri", num_a, "e", num_b, "e'", num_a - num_b)
else:
    print("la somma dei numeri", num_a, "e", num_b, "e'", num_a + num_b)