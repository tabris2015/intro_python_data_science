from carro import CarroElectrico, CarroGrande

tesla = CarroElectrico(
    modelo='model Y',
    año=2018,
    fabricante='Tesla Motors'
)

tesla.encender()
tesla.arrancar()
tesla.apagar()

mi_socio = CarroGrande(
    modelo='condor',
    año=1988,
    fabricante='Volvo'
)

mi_socio.arrancar()