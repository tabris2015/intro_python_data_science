import random

class Dado:
    def __init__(self, caras=6, nombre='default'):
        self.caras = caras
        self.nombre = nombre
        self.resultados = []
        print('dado creado!')

    def lanzar(self):
        print(f'{self.nombre} ha sido lanzado')
        resultado = random.randrange(1, self.caras + 1)
        self.resultados.append(resultado)
        return resultado
    
    def saludar(self):
        print(f'hola soy un dado llamado {self.nombre}')
    
    def obtener_resultados(self):
        return self.resultados

    def __repr__(self):
        """Para la funcion print"""
        return f'Dado:\nnombre: {self.nombre}\ncaras: {self.caras}\nresultados: \n{self.resultados}'

    def __add__(self, otro):
        """Sobrecarga del operador '+' para obtener el resultado de self + otro """
        if not self.resultados or not otro.resultados:
            return 0
        
        return self.resultados[-1] + otro.resultados[-1]
