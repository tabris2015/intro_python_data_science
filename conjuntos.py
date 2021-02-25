#%%
primero_A = set([
    'juan', 'alex', 'edgar', 'arturo'
    ])
primero_B = set([
    'julia',
    'diana',
    'paola',
    'oscar'
])
team_volley = set([
    'alex', 
    'arturo', 
    'paola', 
    'raul'
])
# %%

# condicion: elementos del conjunto
# deben ser inmutables
# primitivos: int, str, float, bool
# tupla

primero_A.intersection(team_volley)
primero_A.union(primero_B)
primero_B & team_volley
primero_A.difference(team_volley)
primero_A - team_volley