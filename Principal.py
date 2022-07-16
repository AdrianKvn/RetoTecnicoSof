import os

from NavesEspaciales import *
#sys.path.insert(0,'./servicios/')

naves_tripuladas=[]
naves_roboticas=[]
vehiculo_Lanzadera=[]
opc =0
os.system("cls")
while not(opc=='5'):
    print('Menú Principal'.center(40,'_'))
    opc=(input('''
            1- Crear Nave
            2- Listar Naves
            3- Buscar Naves
            4- Borrar Nave

            5- Salir
            Elige una opcion '''))
    
    if opc == '1':
        opc =0
        os.system("cls")
        while not(opc=='4'):
            print((('Menú creacion de  naves').center(50,'_')))
            opc=(input('''
        1- Crear Naves Tripuladas
        2- Crear Naves lazaderas
        3- Crear Naves NO Tripuladas(Robotica)
            
        4- Atras
        Elige una opcion '''))
            os.system("cls")
            if opc =='1':
                nt = NavesTripuladas (0,0,0,0,0,0,0,0)
                print((('Menú DE creacion de naves Tripuladas').upper()).center(40,'_'))
                print('\n')
                nt.crearNaveTri()
                
                naves_tripuladas.append(nt)
            elif opc =='2':
                nr = NavesRoboticas (0,0,0,0,0,0,0)
                print((('Menú DE creacion de naves roboticas').upper()).center(40,'_'))
                print('\n')
                nr.crear_nave_robotica()
                naves_roboticas.append(nr)
                
            elif opc =='3':
                vl = VehiculoLanzaderas (0,0,0,0,0,0,0,0)
                print((('Menú DE creacion de vehiculo lanzadera').upper()).center(40,'_'))
                print('\n')
                vl.crear_vehiculo_lanzadera()
                vehiculo_Lanzadera.append(vl)
        
        
    elif opc =='2' :
        os.system("cls")
        print((('Menú listar naves').upper()).center(40,'_'))
        for nave in naves_tripuladas:
            print(nave)
        for nave in naves_roboticas:
            print(nave)
        for nave in vehiculo_Lanzadera:
            print(nave)
        
    elif opc == '3' :
        os.system("cls")
        print('Menú buscar naves')
        NavesTripuladas.buscarNave('NT1')
        
    elif opc =='4' :
        os.system("cls")
        print ('Menú borrar naves')
        
    elif opc == '5':
        opc =0
        os.system("cls")
        print((('SEGURO QUE DESEA SALIR')).center(50,'-'))
        opc=(input('''
                    [1]Si  [0]No 
                    
                    Confirma '''))
        os.system("cls")
        if opc == '1':
            print('Fin de la ejecucion')    
            break
        os.system("cls")

    else:
        os.system("cls")
        print('Opcion incorrecta, intenta de nuevo \n')
            
