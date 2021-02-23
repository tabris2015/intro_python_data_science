def distancia(a, b):
    return abs(a - b)
# numero a adivinar
numero = 9
numero_usuario = None
print('Puedes adivinar el numero que estoy pensando?')
# rangos caliente: numero +- 5
# tibio numero +- 15
# frio dist(numero) > 15
while numero_usuario != numero:
    numero_usuario = int(input('tu corazonada: '))
    if numero_usuario != numero:
        print('te equivocaste!')
        if distancia(numero_usuario, numero) > 15:
            print('te congelas')
        elif distancia(numero_usuario, numero) > 5:
            print('tas tibio')
        else: 
            print('te quemas')

print('Felicidades! adivinaste!')