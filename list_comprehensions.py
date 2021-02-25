nombres = ['ana', 'ariel', 'Arturo', 'juan', 'raul', 'beto', 'armando']

nombres_par = [nombre for i, nombre in enumerate(nombres) if i % 2 == 0]

# for i, nombre in enumerate(nombres):
#     if i % 2 == 0:
#         nombres_par.append(nombre)
# print(nombres_par)

nombres_a = [n for n in nombres if n[0].lower() == 'a']

# for nombre in nombres:
#     if nombre[0].lower() == 'a':
#         nombres_a.append(nombre)

print(nombres_a)
impares_hasta_30 = []

for i in range(31):
    if i % 2 != 0:
        impares_hasta_30.append(i)

# print(impares_hasta_30)