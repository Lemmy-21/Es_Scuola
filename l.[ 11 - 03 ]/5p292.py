'''

[ es 5 e 6 - pag 292 ]
Elenca proprietà e metodi della classe Prodotto
Definisci il metodo assegna_prezzo alla classe Prodotto

'''

class Prodotto:
    def __init__(self, genere, nome, lotto, provenienza):
        self.nome = nome 
        self.lotto = lotto
        self.provenienza = provenienza
        self.genere = genere
        self.msg_prz = 'che prezzo si vuole assegnare al prodotto ' + self.genere + '?\n'
        self.prezzo = float(input(self.msg_prz))
        
    def info(self):
        print('genere:', self.genere, '\nnome:', self.nome, '\nlotto:', self.lotto, '\nprovenienza:', self.provenienza )

    def assegna_prezzo(self):
        self.prezzo = float(input(self.msg_prz))


mela = Prodotto('mela', 'Melinda', 46582, 'Napoli')
pasta = Prodotto('pasta', 'Barilla', 87456, 'Bergamo')
lampada = Prodotto('lampada', 'Aukey', 945823, 'Germania')
vino = Prodotto('vino', 'Lambrusco', 355456, 'Emilia-Romagna')

lista_generi = ['mela', 'pasta', 'lampada', 'vino']
lista_prod = [mela, pasta, lampada, vino]

for i in range(len(lista_generi)):
    print(str(i+1) + '. ', lista_generi[i])

selezione_prod = int(input('che prodotto si vuole visualizzare?\n'))
lista_prod[selezione_prod-1].info()

