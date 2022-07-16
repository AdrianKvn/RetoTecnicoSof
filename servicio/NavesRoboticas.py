from dominio.NavesEspaciales import NavesEspaciales

class NavesRoboticas(NavesEspaciales):
    
    def __init__(self, nombre, velocidad, potencia, tEnergia, peso, altura, empuje) -> None:
        super().__init__(nombre, velocidad, potencia, tEnergia, peso, altura, empuje)
    

    def crear_nave_robotica(self):
        self._nombre = input('* Ingresa el nombre de la nave : ')
        self._velocidad = int(input('* Ingresa la velocidad : '))
        self._potencia = int(input('* Ingresa la potencia de la nave : '))
        self._tEnergia = input('* Tipo de energia : ')
        self._peso = int(input('* Ingresa peso de la nave : '))
        self._altura = int(input('* Ingresa la altura : '))
        self._empuje = int(input('* Ingresa el empuje : '))
        
        print('Nave creada con exito')
        return