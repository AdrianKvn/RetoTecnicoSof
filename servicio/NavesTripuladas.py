from dominio.NavesEspaciales import NavesEspaciales

class NavesTripuladas(NavesEspaciales):
    contadorNavTri = 0
    def __init__(self,nombre, velocidad, potencia, tEnergia, peso, altura, empuje,capacidadPer) -> None:
        super().__init__(nombre,velocidad, potencia, tEnergia, peso, altura, empuje)
        self._capacidadPer = capacidadPer
        NavesTripuladas.contadorNavTri +=1
        self._id = NavesTripuladas.contadorNavTri
        
    
    @property
    def capacidadPer(self):
        return self._capacidadPer

    @capacidadPer.setter
    def capacidadPer(self,capacidadPer):
        self._capacidadPer = capacidadPer

        
    def __str__(self) -> str:
        return f'''
            ID : NT{self._id}
            Tipo de nave: Nave Tripulada
            {super().__str__()}     
            Capacidad de tripulantes:{self._capacidadPer}'''
                        
            

    def mostrarDetalleTri(self):
        
        print(f''''
            Tipo de nave: Nave Tripulada
            Altura : {self._altura:,} m
            Peso : {self._peso:,} kg
            Velocidad : {self._velocidad:,} km/h
            Empuje : {self._empuje:,} N
            Tipo de Energia : {self._tEnergia}
            Potencia : {self._potencia:,} Hp
            Capacidad de Tripulates : {self._capacidadPer}
            
            ''')
            
    
    def crearNaveTri(self):            

        self._nombre = input('* Ingresa el nombre de la nave : ')
        self._velocidad = int(input('* Ingresa la velocidad : '))
        self._potencia = int(input('* Ingresa la potencia de la nave : '))
        self._tEnergia = input('* Tipo de energia : ')
        self._peso = int(input('* Ingresa peso de la nave : '))
        self._altura = int(input('* Ingresa la altura : '))
        self._empuje = int(input('* Ingresa el empuje : '))
        self._capacidadPer = int(input('* Capacidad de tripulante : '))
        
        
        print(f'Nave Creada con Exito')
        return 
    
    def buscarNave(id):
        for i in range (0,len(NavesTripuladas.navelt)):
            if i == id:
                # print(NavesTripuladas.navelt[i])
                return i
            return -1
        
        
