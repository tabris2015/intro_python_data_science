from flask import Flask
import numpy as np

app = Flask(__name__)

#rutas
@app.route('/')
def hola_mundo():
    return 'hola mundo'


@app.route('/populares')
def get_populares():
    ######
    a = np.random.random((1,4))
    print(a)
    ######
    return str(a[0, 0])


@app.route('/anual/<year>')
def get_anual(year):
    ######
    ######
    return f'reporte anual del {year}'


app.run()