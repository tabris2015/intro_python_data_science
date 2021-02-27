frutas = ['manzana', 'durazno', 'higo', 'kiwi', 'mango', 'frutilla']

# frutas que contengan la letra 'a'
# nueva_lista = []
# for f in frutas:
#     if 'a' in f:
#         nueva_lista.append(f)

# todas las frutas que contengan la letra 'a', en mayuscula
nueva_lista = [fruta.upper() for fruta in frutas if 'a' in fruta]
# print(nueva_lista)

# todas las frutas que no sean manzana
lista2 = [fruta for fruta in frutas if fruta != 'manzana']
# print(lista2)

# todos los numeros pares menores a 10
pares = [numero for numero in range(10) if numero % 2 == 0]
# print(pares)

# intercambiar el higo por sandia
frutas2 = [fruta if fruta != 'higo' else 'sandia' for fruta in frutas]
print(frutas2)