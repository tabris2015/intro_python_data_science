#%%
with open('estudiantes.txt', 'r') as f:
    contenido = f.read()

#%%
with open('estudiantes.txt', 'r') as f:
    e1 = f.readline()
    e2 = f.readline()
    e3 = f.readline()

#%%
estudiantes = []
with open('estudiantes.txt', 'r') as f:
    for line in f:
        estudiantes.append(line)

# %%
estudiantes = []
with open('estudiantes.txt', 'r') as f:
    for line in f:
        palabras = line.strip().split(',')
        estudiante = {
            'nombre': palabras[0],
            'edad': palabras[1]
        }
        estudiantes.append(estudiante)
# %%
