'''
[es 32 - pag 73]
Implemente l'algoritmo per il calcolo della
soluzione di un'equazione di primo grado 
(a * x + b = 0). Il processo risolutivo dipende
dai valori assunti dai coefficienti a e b secondo 
la tabella che segue.

se a = 0 e b = 0 è indeterminata
se a = 0 e b != 0 è impossibile
se a != 0 e b = 0 x = 0
se a != 0 e b != 0 x = -b/a

'''
print("verra' svolta questa equazione:\n[ a * x + b = 0 ]\n\n")

try:

    a = int(input("inserire il numero a\n"))
    b = int(input("inserire il numero b\n"))

    if a == 0 and b == 0:
        print("equazione indeterminata")
    elif a == 0 and b != 0:
        print("equazione impossibile")
    elif a != 0 and b == 0:
        print("x = 0")
    else:
        print(a, "* x =", -b)
        print("x =", -(a / b))

except:
    print("inserire un numero intero")