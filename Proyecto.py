## Instituto Tecnologico de Costa Rica
## Ingenieria en Computación
## Primer proyecto de taller de programación realizado por Joshua Venegaz Zúñiga y Ronald Arce Matamoros 

#se importan las librerias que se utilizaran a lo largo del proyecto
import requests
import os 
from posixpath import join
import datetime
import operator
import sys

#se crea una funcion que mostrará las opciones del menu principal
def opciones():
    print(" 1.Ver cursos disponibles\n","2.Ver listado del resgistro de emociones por curso\n","3.Ver detalles de registro de emociones\n","4.Salir del Sistema")

#se crea una función que se utilizará para encontrar el menor de los valores que hay en la lista recibida por parametros
def elMenor(listado):
    l=listado[0]
    menorP=datetime.datetime(int(l["Año"]),int(l["Mes"]),int(l["Dia"]),int(l["Hora"]),int(l["Minuto"]),int(l["Segundos"]))
    
    for z in listado:
        if datetime.datetime(int(z["Año"]),int(z["Mes"]),int(z["Dia"]),int(z["Hora"]),int(z["Minuto"]),int(z["Segundos"])) < menorP:
            l=z
    return(l)
#funcion que imprime las opciones que se mostraran en la opcion de "Ver listado del registro de emociones"
def listadoEmociones():
    print(" 1.Listar registro de emociones\n","2.Regresar al menu principal")

#Función creada para obtener los cursos desde el link brindado por el profesor
def getCursos():
        URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
        r = requests.get(url = URL)
        results= eval(r.text)
        return results

#Funcion que se crea con el fin de monstrar la lista de cursos disponibles de manera ordenada segun su id 
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

#Funcion creada con el fin de mostrar los registros de emociones ordenados segun su fecha de creación
def listaEmociones():
    URL="http://leoviquez.synology.me/VisionAPI/cursos.py?id=6"
    os.system("cls")
    r = requests.get(url = URL)
    resultados= eval(r.text)
    lista=[]

    for z in resultados:
        lista.append({"ID":z[0],"Dia":z[1],"Mes":z[2],"Año":z[3],"Hora":z[4],"Minuto":z[5],"Segundos":z[6]})
    ListaOrdenada=[]

    while len(lista)>0:
        menor=elMenor(lista)
        ListaOrdenada.append(menor)
        lista.remove(menor)
    print ("        {0:10}{1:10} {2:10}{3:10}  {4:10}{5:10}{6:10}".format('ID','Dia','Mes','Año','Hora','Minuto','Segundos'))

    for z in ListaOrdenada:
        print ("------------------------------------------------------------------------------------")
        print ("{0:10}{1:10} {2:10} {3:10}  {4:10} {5:10} {6:10}".format(int(z["ID"]),int(z["Dia"]),int(z["Mes"]),int(z["Año"]),int(z["Hora"]),int(z["Minuto"]),int(z["Segundos"])))
    os.system("pause")

#Funcion creada para mostrar las opciones disponibles dentro de "Ver detalles de registro de emociones"
def detallesRegistro():
    print(" 1.Detalle del registro\n","2.Estadísticas de reconocimiento\n","3.Regresar al menu principal")

#Funcion creada para que obtenga un registro de datos segun el id digitado por el usuario, este registro se obtiene del link brindado por el profesor
#Tambien cumple con la función de mostrar la información de el registro de manera tabular 
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
        print("Asegurese de haber digitado un registro válido")
    os.system("pause")
    opcion3()

#Funcion que devuelve los porcentajes de emociones segun la lista recibida, los valores que devuelve esta función son: 0,25,50,75,100
def devolverPorcentaje(lista):
    if lista=="VERY_UNLIKELY":
        return 0
    elif lista=="UNLIKELY":
        return 25
    elif lista=="POSSIBLE":
        return 50
    elif lista=="LIKELY":
        return 75
    elif lista=="VERY_LIKELY":
        return 100

#Funcion que se encarga de mostrar la "estadistica de reconocimiento", mostrará el curso que se digitó y el porcentaje de estudiantes que tuvieron cada expresión facial    
def imprimirEmociones(emo,curso):
    os.system("cls")
    lista=emo[0]
    cont=len(lista)
    ordenado=dict(sorted(lista.items(),key=operator.itemgetter(1),reverse=True))
    print("Curso|","Emociones                                          \n"
    ,"------------------------------------------------------------\n"
    ,"{}  | {}".format(curso,ordenado))
                  
#Funcion que se encarga de obtener el registro de expresiones(emociones) de un registro segun su id las emociones que se buscaran en el registro son: joy, sorrow, anger, surprise
#luego segun los datos recolectados se enviarán a imprimir a otra función
def obtenerEmociones(id):
    try:
        URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={}".format(int(id))
        r = requests.get(url = URL)
        estadistica = eval(r.text)
        estadistica=estadistica[0]
        rostros=estadistica["rostros"]
        joy=0
        sorrow=0
        anger=0
        surprise=0

        for p in rostros:
            expresiones=p["face_expressions"]
            #se van sumando los porcentajes de cada expresion por cada cara reconocida
            joy+=devolverPorcentaje(expresiones["joy_likelihood"])
            sorrow+=devolverPorcentaje(expresiones["sorrow_likelihood"])
            anger+=devolverPorcentaje(expresiones["anger_likelihood"])
            surprise+=devolverPorcentaje(expresiones["surprise_likelihood"])      
        
        #se saca el promedio por emoción del registro 
        surprise=surprise//len(rostros)
        anger=anger//len(rostros)
        sorrow=sorrow//len(rostros)
        joy=joy//len(rostros)
        emociones=[{"surprise":surprise,"anger":anger,"sorrow":sorrow,"joy":joy}]
        imprimirEmociones(emociones,id)
    except:
        os.system("cls")
        print("porfavor digite un registro válido")  
    

#se crea la función en caso de que la opcion del usuario sea la 1 Ver cursos disponibles
def opcion1():
    os.system("cls")
    tempoCursos=getCursos()
    mostraCursos(tempoCursos)
    os.system("pause")    
#se crea la función en caso de que la opcion del usuario sea la 2 Ver listado del resgistro de emociones por curso
def opcion2():
    os.system("cls")
    listadoEmociones()
    opcion=int(input("Digite su opcion: "))
    if opcion==2:
        menu()
    elif opcion==1:
        listaEmociones()
        opcion2()
#se crea la función en caso de que la opcion del usuario sea la 3 Ver detalles de registro de emociones
def opcion3():
        os.system("cls")
        detallesRegistro()
        opcion=int(input("Digite su opcion: "))
        if opcion==1:
            os.system("cls")
            registro=input("Digite el id del registro que desea ver: ")
            obtenerEstadisticas(registro)
            os.system("pause")
        elif opcion==2:
            os.system("cls")
            registro=input("Digite el id del registro que desea ver: ")
            obtenerEmociones(registro)
            os.system("pause")
        elif opcion==3:
            menu()    
#se crea el menu principal de opciones el cual tendrá 4 opciones 
# 1.Ver cursos disponibles 
# 2.Ver listado del resgistro de emociones por curso,
# 3.Ver detalles de registro de emociones 
# 4.Salir del Sistema
def menu():
    while True:
        os.system("cls")
        opciones()
        try:

            opcion=int(input("Digite su opcion: "))

            if opcion == 1:#en caso de que la opcion sea la 1
                opcion1()

            elif opcion==2:#en caso de que la opcion sea la 2
                opcion2()
            
            elif opcion==3:#en caso de que la opcion sea la 3
                opcion3()

            elif opcion==4:#en caso de que la opcion sea la 4
                os.system("cls")
                print("Gracias por utilizar el programa")#se imprime un mensaje de despedida
                os._exit(1)#se llama a la siguiente función para cerrar el programa en su totalidad sin que devuelva error alguno

            elif opcion!=1 and opcion!=2 and opcion !=3 and opcion!=4:#en caso de que la opción no sea válida
                os.system("cls")
                print("opcion no valida ")#se imprime un mensaje 
                os.system("pause")

        except ValueError:#en caso de que el usuario no digite un valor valido con respecto al programa. Para que este no se caiga se le imprime un mensaje  
            os.system("cls")
            print("Seleccione una opción válida")#se le pide al usuario por favor digitar un valor valido 
            os.system("pause")
            menu()#se llama de nuevo al menu 

        

menu()#se llama al menu principal 