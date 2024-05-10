import random

class Taikinys:
    def __init__(self):
        self.x = random.randint(-10, 10)
        self.y = random.randint(-10, 10)

    def ar_pataike(self, x, y):
        return self.x == x and self.y == y

class Tankas:
    def __init__(self):
        self.x = random.randint(-10, 10)
        self.y = random.randint(-10, 10)
        self.kryptis = random.choice(['primyn', 'atgal', 'kairėn', 'dešinėn'])

    def tanko_judėjimas(self, kryptis):
        if kryptis == 'pirmyn':
            self.y += 1
        elif kryptis == 'atgal':
            self.y -= 1
        elif kryptis == 'kairėn':
            self.x -= 1
        elif kryptis == 'dešinėn':
            self.x += 1

    def sauti(self, taikinys):
        if taikinys.ar_pataike(self.x, self.y):
            print('Pataikei ')
            taikinys = Taikinys()
        else:
            print('Nepataikei')

    def informacija(self):
        print('Tanko kryptis:', self.kryptis)
        print('Tanko kordinatės: ({}, {})'.format(self.x,self.y))

taikinys = Taikinys()
tank = Tankas()

while True:
    print('\nPasirinkite veiksmą')
    print('1. Judėti')
    print('2. Šaudyti')
    print('3. Informacija')
    print('4. Baigti programą')

    pasirinkimas = input('Įveskite pasirinkimą:')

    if pasirinkimas == '1':
        tanko_kryptis = input('Įveskite judėjimo kryptį (pirmyn, atgal, kairėn, dešinėn):')
        tank.tanko_judėjimas(tanko_kryptis)
    elif pasirinkimas == '2':
        tank.sauti(taikinys)
    elif pasirinkimas == '3':
        tank.informacija()
    elif pasirinkimas == '4':
        print('Programa užbaigs darbą')
        break
    else:
        print('Neteisingai pasirinkote, bandykite iš naujo')
