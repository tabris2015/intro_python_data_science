from dado import Dado
from cosas.saludos import hola

print(hola)

# lanzar el dado 3 veces y mostrar el resultado
dado_magico = Dado(nombre='magico')
dado_normal = Dado(nombre='normal')

print(dado_magico)

print(dado_magico.lanzar())
print(dado_magico.lanzar())
print(dado_magico.lanzar())

print(dado_magico.obtener_resultados())
print(dado_magico)

print(dado_normal.lanzar())
# dado_magico == dado_normal

if dado_magico + dado_normal == 7:
    print('ganaste')
else:
    print(f'el resultado es {dado_magico + dado_normal}')
# dado_magico.caras = 20
# print(f'magico: {dado_magico.caras}, normal: {dado_normal.caras}')