## Instituto Tecnologico de Costa Rica
## Ingenieria en Computación
## Primer proyecto de taller de programación realizado por Joshua Venegaz Zúñiga y Ronald Arce Matamoros 
import requests
import os 
from posixpath import join

cursos=[(2, 'IC-1802', 'Introducción a la programación', 51, 'Abel Méndez Porras', 'I ', 2020), (5, 'IC-1803', 'Taller de programación', 51, 'Abel Méndez Porras', 'I ', 2020), (3, 'IC-1802', 'Introducción a la programación', 52, 'Leonardo Víquez Acuña', 'I ', 2020), (6, 'IC-1803', 'Taller de programación', 52, 'Leonardo Víquez Acuña', 'I ', 2020), (1, 'IC-1802', 'Introducción a la programación', 50, 'Vera Gamboa Guzman', 'I ', 2020), (4, 'IC-1803', 'Taller de programación', 50, 'Vera Gamboa Guzman', 'I ', 2020)]

def opciones():
    print(" 1.Ver cursos disponibles\n","2.Ver listado del resgistro de emociones por curso\n","3.Ver detalles de registro de emociones\n","4. Salir del Sistema")

def listadoEmociones():
    print(" 1.Listar registro de emociones\n","2.Regresar al menu principal")

def getCursos():
        URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
        r = requests.get(url = URL)
        results= eval(r.text)
        return results

def listaEmociones():
    URL="http://leoviquez.synology.me/VisionAPI/cursos.py?id=6"
    os.system("cls")
    r = requests.get(url = URL)
    resultados= eval(r.text)
    cont=0
    cantidad=len(resultados)
    print ("        {0:10}{1:10} {2:10}{3:10}  {4:10}{5:10}{6:10}".format('ID','Dia','Mes','Año','Hora','Minuto','Segundos'))
    for z in resultados:
         print ("{0:10}  {1:10}{2:10} {3:10}  {4:10} {5:10}   {6:10}".format(z[0],z[1],z[2],z[3],z[4],z[5],z[6]))
    input("Presione ENTER para continuar...")

def detallesRegistro():
    print(" 1.Detalle del registro\n","2.Estadísticas de reconocimiento\n","3. Regresar al menu principal")

def menu():
    opcion2=int(1)
    while True:
        os.system("cls")
        opciones()
        try:
            opcion=int(input("Digite su opcion: "))

            if opcion == 1:
                os.system("cls")
                cursos=getCursos()
                for p in cursos:
                    print(p)
                os.system("pause")
            elif opcion==2:
                os.system("cls")
                listadoEmociones()
                opcion2=int(input("Digite su opcion: "))
                if opcion2==2:
                    menu()
                elif opcion2==1:
                    listaEmociones()
            
            elif opcion==3:
                os.system("cls")
                detallesRegistro()
                opcion2=int(input("Digite su opcion: "))
                if opcion2==3:
                    menu()
            elif opcion==4:
                break
            elif opcion!=1 and opcion!=2 and opcion !=3 and opcion!=4:
                os.system("cls")
                print("opcion no valida ")
                os.system("pause")
        except ValueError:
            os.system("cls")
            print("Seleccione una opción válida")
            os.system("pause")
            menu()

        

menu()