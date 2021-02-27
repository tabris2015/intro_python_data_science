def registrar_estudiantes(n):
    # registro de datos
    estudiantes = []
    for i in range(n):
        estudiante = {}
        print(f'estudiante {i+1}:')
        estudiante['nombre'] = input('nombre del estudiante: ')
        in_edad = input('edad del estudiante: ')
        while not in_edad.isdigit():
            print('ingrese una edad valida')
            in_edad = input('edad del estudiante: ')

        estudiante['edad'] = int(in_edad)
        estudiantes.append(estudiante)

    return estudiantes

def guardar_estudiantes(estudiantes, archivo='estudiantes.txt'):
    # abrir un archivo y almacenar todos los datos 
    # estudiante = {
    #   'nombre': 'dfalkjasdf',
    #   'edad': 123123
    # }
    # estudiante["nombre"]  => 'dfalkjasdf'
    with open(archivo, 'w') as f:
        for est in estudiantes:
            fila = est['nombre'] + ',' + str(est['edad']) + '\n'
            print(fila)
            f.write(fila)
