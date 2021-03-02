'''

[ es da 1 a 4 - pag 292 ]
Crea una classe Atleta attribuendogli un valore buleano visita_medica,
creando un metodo per assegnarli una squadra, per effettuare la visita medica
e per visualizzare i suoi dati.

'''

class Atleta:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.visita_medica = False
        self.team = input('in che squadra gioca?\n')

    def info(self):
        print('nome:', self.name, "\neta':", self.age, '\nsquadra:', self.team, '\nvisita:', self.visita_medica)

    def effettua_visita(self):
        print('\n', self.name, 'ha effettuato la visita medica\n')
        self.visita_medica = True


A0 = Atleta('Gino', 23)

A0.info()
A0.effettua_visita()
A0.info()