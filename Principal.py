import os
from NavesEspaciales import *


opc =0
os.system("cls")
while not(opc==5):
    print('Menú Principal'.center(40,'_'))
    opc=int(input('''
            1- Crear Nave
            2- Listar Naves
            3- Buscar Naves
            4- Borrar Nave

            5- Salir
            Elige una opcion '''))
    
    if opc == 1:
        opc =0
        os.system("cls")
        while not(opc==4):
            print((('Menú creacion de  naves').center(50,'_')))
            opc=int(input('''
        1- Crear Naves Tripuladas
        2- Crear Naves lazaderas
        3- Crear Naves NO Tripuladas
            
        4- Atras
        Elige una opcion '''))
            os.system("cls")
            if opc ==1:
                nt= NavesTripuladas
                print((('Menú DE creacion de naves Tripuladas').upper()).center(40,'_'))
                print('\n')
                listaNtK=['velocidad', 'potencia', 'tEnergia', 'peso', 'altura', 'empuje', 'capacidadPer']
                listaNtV=[]
                dicNT=dict(zip(listaNtK,listaNtV))
                nt.crearNaveTri(nt)
                nt.mostrarDetalleTri(nt)


    elif opc ==2 :
        os.system("cls")
        print('Menú listar naves')
        nt.mostrarDetalleTri(nt)
        
    elif opc == 3 :
        os.system("cls")
        print('Menú buscar naves')
        
    elif opc ==4 :
        os.system("cls")
        print ('Menú borrar naves')
        
    elif opc == 5:
        opc =0
        os.system("cls")
        print((('SEGURO QUE DESEA SALIR')).center(50,'-'))
        opc=int(input('''
                    [1]Si  [0]No 
                    
                    Confirma '''))
        os.system("cls")
        if opc == 1:
            load()
            print('Fin de la ejecucion')    
            break
        os.system("cls")

        
            
        
        
# for i in range(2) :





# n = NavesEspaciales(300,122,'Combistible',123,2451,3862)
# print('Creancion de Naves'.center(50,'_'))
# print(n)

# vl= VehiculoLanzaderas(525,7662,'Panel',636,2388,777,9999)
# print(vl)

# nt= NavesTripuladas(525,7662,'Panel',636,2388,777,222)
# print(nt)