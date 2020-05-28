## Instituto Tecnologico de Costa Rica
## Ingenieria en Computación
## Primer proyecto de taller de programación realizado por Joshua Venegaz Zúñiga y Ronald Arce Matamoros 

import os 
cursos=[(2, 'IC-1802', 'Introducción a la programación', 51, 'Abel Méndez Porras', 'I ', 2020), (5, 'IC-1803', 'Taller de programación', 51, 'Abel Méndez Porras', 'I ', 2020), (3, 'IC-1802', 'Introducción a la programación', 52, 'Leonardo Víquez Acuña', 'I ', 2020), (6, 'IC-1803', 'Taller de programación', 52, 'Leonardo Víquez Acuña', 'I ', 2020), (1, 'IC-1802', 'Introducción a la programación', 50, 'Vera Gamboa Guzman', 'I ', 2020), (4, 'IC-1803', 'Taller de programación', 50, 'Vera Gamboa Guzman', 'I ', 2020)]

def opciones():
    print(" 1.Ver cursos disponibles\n","2.Ver listado del resgistro de emociones por curso\n","3.Ver detalles de registro de emociones\n","4. Salir del Sistema")

def listadoEmociones():
    print(" 1.Listar registro de emociones\n","2.Regresar al menu principal")

def detallesRegistro():
    print(" 1.Detalle del registro\n","2.Estadísticas de reconocimiento\n","3. Regresar al menu principal")

def menu():
    opcion=int(1)
    opcion2=int(1)
    while opcion !=4:
        os.system("cls")
        opciones()
        opcion=int(input("Digite su opcion: "))

        if opcion == 1:
            os.system("cls")
            print(cursos[4])
            print(cursos[0])
            print(cursos[2])
            print(cursos[5])
            print(cursos[1])
            os.system("pause")

        elif opcion==2:
            os.system("cls")
            listadoEmociones()
            opcion2=int(input("Digite su opcion: "))
            if opcion2==2:
                menu()

        elif opcion==3:
            os.system("cls")
            detallesRegistro()
            opcion2=int(input("Digite su opcion: "))
            if opcion2==3:
                menu()
        elif opcion!=1 and opcion!=2 and opcion !=3 and opcion!=4:
            os.system("cls")
            print("opcion no valida ")
            os.system("pause")

menu()