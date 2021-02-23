# obtener variables desde el teclado
nombre = input('nombre del estudiante: ')

matematica = int(input('nota de matematica: '))
filosofia = int(input('nota de filosofia: '))
fisica = int(input('nota de fisica: '))
ed_fisica = int(input('nota de educacion fisica: '))

# calcular el promedio
promedio = (matematica + filosofia + fisica + ed_fisica) / 4

# imprimir el resultado
print(f'{nombre} tiene de promedio: {promedio}')

# imprimir observaciones
# operadores de comparacion
# igualdad: ==
# desigualdad: !=
# mayor que: >
# menor que: <
# mayor o igual que: >=
# menor o igual que: <=

if promedio >= 51:
    print('APROBADO')
    print('felicidades!')
else:
    print('REPROBADO')
    print('que verguenza')

# mencion: REGULAR, BUENO, MUY BUENO, SOBRESALIENTE
#           <=60     <=70     <=80         <=100
# if(promedio > 80)
# if(!(promedio > 80))
if not promedio > 80:
    print('SOBRESALIENTE')
elif promedio > 70 and promedio <= 80:
    print('MUY BUENO')
elif promedio > 60 and promedio <= 70:
    print('BUENO')
elif promedio > 50 and promedio <= 60:
    print('REGULAR')
else:
    print('que verguenza x2')
