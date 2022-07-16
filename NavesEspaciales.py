class NavesEspaciales:
    
    def __init__(self,nombre,velocidad,potencia,tEnergia,peso,altura,empuje) -> None:
        self._nombre =nombre
        self._velocidad = velocidad
        self._potencia = potencia
        self._tEnergia = tEnergia
        self._peso = peso
        self._altura = altura
        self._empuje = empuje
    
    
    #METODOS GET's  
    @property
    def nombre(self):
        return self._nombre
    @property
    def velocidad (self):
        return self._velocidad
    @property
    def potencia(self):
        return self._potencia
    @property
    def tEnergia(self):
        return self._tEnergia
    @property
    def peso(self):
        return self._peso
    @property
    def altura(self):
        return self._altura
    @property
    def empuje(self):
        return self._empuje
    
    #METODO SET's
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad= velocidad
    @potencia.setter
    def potencia(self,potencia):
        self._potencia= potencia
    @tEnergia.setter
    def tEnergia(self,tEnergia):
        self._tEnergia= tEnergia
    @peso.setter
    def peso(self,peso):
        self._peso= peso
    @altura.setter
    def altura(self,altura):
        self._altura= altura
    @empuje.setter
    def empuje(self,empuje):
        self._empuje= empuje
        
    
    def __str__(self) -> str:
        return f'''
            Nombre de la nave: {(self._nombre).upper()}
            Altura : {self._altura:,} m
            Peso : {self._peso:,} kg
            Velocidad {self._velocidad:,} km/h
            Empuje : {self._empuje:,} N
            Tipo de Energia : {self._tEnergia}
            Potencia {self._potencia:,} Hp
            '''
            
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
    
class VehiculoLanzaderas(NavesEspaciales):
    contadorVehLan = 0
    
    def __init__(self,nombre, velocidad, potencia, tEnergia, peso, altura, empuje,capacidadT) -> None:
        super().__init__(nombre, velocidad, potencia, tEnergia, peso, altura, empuje)
        self._capacidadT = capacidadT
        self._tipo = 'Vehiculo Lanzaderas'
        VehiculoLanzaderas.contadorVehLan+=1
        self._id = VehiculoLanzaderas.contadorVehLan

        
    @property
    def capacidadT(self):
        return self._capacidadT
    
    @capacidadT.setter
    def capacidadT(self,capacidadT):
        self._capacidadT = capacidadT

    def __str__(self) -> str:
        return f'''
            ID : VL{self._id}
            Tipo de nave: Vehiculo Lanzadera
            {super().__str__()}
            Capacidad de transporte: {self._capacidadT}'''
            
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
        
        




    
    
    ##TEST
if __name__ == "__main__":
    n = NavesEspaciales('a',12,166,'Combistible',276,2763,2662)
    # print(n)
    # navest=[]
    encaDic=['nombre', 'velocidad', 'potencia', 'tEnergia', 'peso', 'altura', 'empuje','capacidadT']
    dataDics=[]
    
    vl =VehiculoLanzaderas('NAVE NOMBRE',22,11,'r',333,111,444,555)
    dataDics.append(vl)
    #dicNav=dict(zip(encaDic,dataDics))
    print(vl)
    
    vl2 =VehiculoLanzaderas('c',444,444,'qqq',99,99,99,59955)
    
 
    #for k,ll in dicNav.items():
    #    print (k,ll)
    # navest.append(vl2)
    # buscar = 12
    # n=len(navest)
    
#     def search_element(navest, n, buscar):
#         for i in range(n):
#             if navest[i] == buscar:
#                 return True
#         return False 
    
# if search_element(navest, n, buscar):
#     print(buscar, "is found")
# else:
#     print(buscar, "is not found")
    
    
        


