dic_precios = {
    'papa': 2, 
    'arroz': 1,
    'carne': 10,
    'tomate': 3,
    'cebolla': 2
    }

lista_compras = ['papa', 'zanahoria','carne']       # lo que quiero comprar

costo_total = 0

# para cada elemento en la lista de compras
for elem in lista_compras:
    print(f'comprando {elem}...')
    # verificar si esta disponible
    if elem in dic_precios:
        print(f'item {elem} disponible!')
        # si esta disponible, agregar el costo al costo total
        costo_total += dic_precios[elem]

print(f'costo total: {costo_total}')