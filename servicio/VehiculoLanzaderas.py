from dominio.NavesEspaciales import NavesEspaciales

class VehiculoLanzaderas(NavesEspaciales):
    contadorVl = 0
    
    def __init__(self,nombre, velocidad, potencia, tEnergia, peso, altura, empuje,capacidadT) -> None:
        super().__init__(nombre, velocidad, potencia, tEnergia, peso, altura, empuje)
        self._capacidadT = capacidadT
        self._tipo = 'Vehiculo Lanzaderas'

        
    @property
    def capacidadT(self):
        return self._capacidadT
    
    @capacidadT.setter
    def capacidadT(self,capacidadT):
        self._capacidadT = capacidadT

    def __str__(self) -> str:
        return f'''
            Tipo de nave: {self._tipo}
            
            Capacidad de transporte: {self._capacidadT}{super().__str__()}'''
            
    def mostrarDetalleLan(self):
        print(f'''
            Tipo de nave: {self._tipo}     
            Capacidad de tripulantes:{self._capacidadT}{super().__str__()}''')
    
    def crear_vehiculo_lanzadera(self):
        
        self._nombre = input('* Ingresa el nombre de la nave : ')
        self._velocidad = int(input('* Ingresa la velocidad : '))
        self._potencia = int(input('* Ingresa la potencia de la nave : '))
        self._tEnergia = input('* Tipo de energia : ')
        self._peso = int(input('* Ingresa peso de la nave : '))
        self._altura = int(input('* Ingresa la altura : '))
        self._empuje = int(input('* Ingresa el empuje : '))
        
        
        print(f'Nave Creada con Exito')
        return