from funciones import registrar_estudiantes, guardar_estudiantes

n_estudiantes = 0
in_n_estudiantes = input('numero de estudiantes a registrar: ')
if not in_n_estudiantes.isdigit():
    print('ERROR: ingrese un numero valido')
    exit()

n_estudiantes = int(in_n_estudiantes)

estudiantes = registrar_estudiantes(n_estudiantes)

guardar_estudiantes(estudiantes)