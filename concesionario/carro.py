class Carro:
    modelo: str
    año: int
    fabricante: str
    tipo_motor: str = 'gasolina'
    esta_encendido: bool

    def encender(self):
        print(f'encendiendo {self.modelo}')
        self.esta_encendido = True

    def arrancar(self):
        print(f'brum brum')
    
    def apagar(self):
        print(f'apagando')
        self.esta_encendido = False

class CarroElectrico(Carro):
    def __init__(self, modelo, año, fabricante):
        self.modelo = modelo
        self.año = año
        self.fabricante = fabricante
        self.tipo_motor = 'electrico'
        self.apagar()
    
    def arrancar(self):
        print(f'zum zum')


class CarroGrande(Carro):
    def __init__(self, modelo, año, fabricante):
        self.modelo = modelo
        self.año = año
        self.fabricante = fabricante
        self.tipo_motor = 'diesel'
        self.apagar()
    
    def arrancar(self):
        print(f'BRUM BRUM')