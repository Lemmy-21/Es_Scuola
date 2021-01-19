'''

[es 2 - pag 201]

Data la parabola y = ax² + bx + c,
definisci due funzioni per calcolarne i punti significativi:
vertice e fuoco.
Le due funzioni ricevono come parametri a, b, c
e restituiscono il valore calcolato

'''

def fuoco(a, b ,c, delta):
    x_fuoco = -b/2*a
    y_fuoco = (1-delta)/(4*a)
    return x_fuoco, y_fuoco

def vertice(a, b, c, delta):
    x_vertice = -b/2*a
    y_vertice = -delta/4*a
    return x_vertice, y_vertice

a = int(input('inserire variabile a\n'))
if a == 0:
    while a ==0:
        a = int(input('inserire variabile a diversa da 0\n'))
b = int(input('inserire variabile b\n'))
c = int(input('inserire variabile c\n'))
delta = b**2 - 4*a*c
print("il fuoco della parabola e'", fuoco(a, b , c, delta), "\n il vertice della parabola e'", vertice(a, b, c, delta))