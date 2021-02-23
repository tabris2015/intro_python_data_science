# recibir el numero de estudiantes
n_estudiantes = int(input('ingrese el numero de estudiantes: '))
print(f'estudiantes a registrar: {n_estudiantes}')
# abrir archivo para registrar datos
with open('notas.csv', 'w') as archivo:
    archivo.write('Nombre,Promedio,Observacion\n')
    for i in range(n_estudiantes):
        print(f'estudiante {i + 1}')
        # registrar nombre del estudiante
        nombre = input('nombre del estudiante: ')
        ha_asistido = bool(int(input('asistencia[0-1]: ')))
        if not ha_asistido:
            print('reprobado por inasistencia')
            archivo.write(f'{nombre}, ,REPROBADO\n')
            continue
        print(f'notas para el/la estudiante {nombre}')
        # registrar notas y calcular promedio
        mat = int(input('matematica: '))
        fis = int(input('fisica: '))
        qmc = int(input('quimica: '))
        # calcular y mostrar el promedio
        promedio = (mat + fis + qmc) / 3
        print(f'promedio para estudiante {nombre}: {promedio}')
        observacion = 'APROBADO' if promedio > 50 else 'REPROBADO'
        archivo.write(f'{nombre},{promedio},{observacion}\n')
