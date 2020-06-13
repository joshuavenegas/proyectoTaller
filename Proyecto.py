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

def mostraCursos(lista1):#funcion creada para ordenar los registros de la lista recibida por el id
    os.system("cls")
    listaTemporal=[]
    tempo=lista1
    for p in tempo:
        for t in lista1:
            if len(listaTemporal)<len(lista1):
                if (t[0]<p[0]) & (t not in listaTemporal):
                    listaTemporal.append(t)

    for s in listaTemporal:
        print(s)


    

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
    print(" 1.Detalle del registro\n","2.Estadísticas de reconocimiento\n","3.Regresar al menu principal")

def obtenerEstadisticas(id):
    try:
        URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={}".format(int(id))
        r = requests.get(url = URL)
        estadistica = eval(r.text)
        estadistica=estadistica[0]
        fechaResgistro=estadistica["fecha"]
        informacionCurso=estadistica["curso"]
        informacionRostro=estadistica["rostros"]
        os.system("cls")
        print("Hora de Registro  | Información del Curso                                                               | Cantidad de Rostros Reconocidos|\n"
        ,"-----------------------------------------------------------------------------------------------------------------------------------------\n",
        "{}:{}            |".format(fechaResgistro["hora"],fechaResgistro["minuto"],)
        ,"codigo:{} grupo:{} curso:{} profesor:{} |".format(informacionCurso["codigo"],informacionCurso["grupo"],informacionCurso["Curso"],informacionCurso["profesor"])
        ,"{}                              |".format(len(informacionRostro)))
    except:
        os.system("cls")
        print("asegurese de haber digitado un registro válido")
    os.system("pause")
    opcion3()

def opcion3():
        os.system("cls")
        detallesRegistro()
        opcion2=int(input("Digite su opcion: "))
        if opcion2==1:
            os.system("cls")
            registro=input("Digite el id del registro que desea ver: ")
            obtenerEstadisticas(registro)
            os.system("pause")
        if opcion2==3:
            menu()    

def menu():
    opcion2=int(1)
    while True:
        os.system("cls")
        opciones()
        try:
            opcion=int(input("Digite su opcion: "))

            if opcion == 1:
                os.system("cls")
                tempoCursos=getCursos()
                mostraCursos(tempoCursos)
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
                opcion3()
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