nombre_completo = 'juan perez fernandez'
palabras = nombre_completo.split()
nombre = palabras[0]
ap_paterno = palabras[1]
ap_materno = palabras[2] if len(palabras) > 2 else ''


print('nombre:', nombre)
print('ap_paterno:', ap_paterno)
print('ap_materno:', ap_materno)