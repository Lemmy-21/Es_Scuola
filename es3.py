
stipendi = []
count = 0
somma = 0

while True:

    stipendio = int(input("stipendio\n"))
    if stipendio != 1:
        stipendi.append(stipendio)
    else: 
        break

while count < len(stipendi):

    somma += stipendi[count]
    count += 1

media = somma/ len(stipendi)

print("la media è ", media)
