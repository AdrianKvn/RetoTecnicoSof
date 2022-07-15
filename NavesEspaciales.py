class NavesEspaciales:
    
    def __init__(self,velocidad,potencia,tEnergia,peso,altura,empuje) -> None:
        self._velocidad = velocidad
        self._potencia = potencia
        self._tEnergia = tEnergia
        self._peso = peso
        self._altura = altura
        self._empuje = empuje
    
    
    #METODOS GET's        
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
            Altura : {self._altura:,} m
            Peso : {self._peso:,} kg
            Velocidad {self._velocidad:,} km/h
            Empuje : {self._empuje:,} N
            Tipo de Energia : {self._tEnergia}
            Potencia {self._potencia:,} Hp
            '''
            
            
class VehiculoLanzaderas(NavesEspaciales):
    
    def __init__(self, velocidad, potencia, tEnergia, peso, altura, empuje,capacidadT) -> None:
        super().__init__(velocidad, potencia, tEnergia, peso, altura, empuje)
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
    

    
class NavesTripuladas(NavesEspaciales):
    
    
    def __init__(self, velocidad, potencia, tEnergia, peso, altura, empuje,capacidadPer) -> None:
        super().__init__(velocidad, potencia, tEnergia, peso, altura, empuje)
        self._capacidadPer = capacidadPer
       # self._tipo = 'Naves Tripuladas'
    
    @property
    def capacidadPer(self):
        return self._capacidadPer

    @capacidadPer.setter
    def capacidadPer(self,capacidadPer):
        self._capacidadPer = capacidadPer

        
    def __str__(self) -> str:
        return f'''
            Tipo de nave: Nave Tripulada
            
            Capacidad de tripulantes:{self._capacidadPer}{super().__str__()}'''
            
    def mostrarDetalleTri2(self):
        self.mostrarDetalleTri2()
        print(f'''
            
            Capacidad de tripulantes:{self._capacidadPer}{super().__str__()}''')
            
            

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
        listaNtK=['velocidad', 'potencia', 'tEnergia', 'peso', 'altura', 'empuje', 'capacidadPer']
        listaNtV=[]
        i=1
        while i <= 5:
            i+1
            nt='nt'
            conC=f'{nt}{i}'
        
            conC= NavesTripuladas
            conC._velocidad = int(input('* Ingresa la velocidad '))
            listaNtV.append(self._velocidad)
            conC._potencia = int(input('* Ingresa la potencia de la nave '))
            listaNtV.append(self._potencia)
            conC._tEnergia = input('* Tipo de energia ')
            listaNtV.append(self._tEnergia)
            conC._peso = int(input('* Ingresa peso de la nave '))
            listaNtV.append(self._peso)
            conC._altura = int(input('* Ingresa la altura '))
            listaNtV.append(self._altura)
            conC._empuje = int(input('* Ingresa el empuje '))
            listaNtV.append(self._empuje)
            conC._capacidadPer = int(input('* Capacidad de tripulante '))
            listaNtV.append(self._capacidadPer)
            dicNT=dict(zip(listaNtK,listaNtV))
            
        
            print(f'Nave Creada con Exito')
            return dicNT
        # print(dnt)
        



def load():
    from tqdm import tqdm
    from time import sleep
    a = 10
    for i in tqdm(range(a),desc='Cerrando'):
        sleep(0.1)

    
    
    ##TEST
if __name__ == "__main__":
    n = NavesEspaciales(12,166,'Combistible',276,2763,2662)
    print(n)
    
    # vl= VehiculoLanzaderas(525,7662,'Panel',636,2388,777)
    # print(vl)
    
    vl =VehiculoLanzaderas(22,11,'r',333,111,444,555)
    vl.mostrarDetalleLan()
    vl2 =VehiculoLanzaderas(333,3,'rrr',333,3,34,55335)
    vl2.mostrarDetalleLan()
    
    # nt =NavesTripuladas
    # nt.crearNaveTri(nt)
    
    # nt.mostrarDetalleTri(nt)
    

