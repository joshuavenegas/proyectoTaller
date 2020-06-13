# Instituto Tecnologico de Costa Rica 
# Joshua Venegas Zúñiga 
# Programa Realizado para ordenar registros de personas basados en su apellido 
import os#se importa la libreria os
lista=[{"nombre":"Leonardo","apellido1":"Víquez","apellido2":"Acuña"},{"nombre":"Martha","apellido1":"Días","apellido2":"Salazar"},{"nombre":"Joshua","apellido1":"Venegas","apellido2":"Zúñiga"}]

def ordenarApellido(lista1):#funcion creada para ordenar los registros de la lista recibida por apellido
    os.system("cls")#se limpia la terminal
    listaTemporal=[]#se crea una lista temporal donde se van a almacenar los registros ordenados por apellido
    tempo=lista1#se declara una variable temporal que almacenará la lista recibida
    for p in lista1:#se recorre la lista recibida
        for t in tempo:#se recorre tempo
            if len(listaTemporal)<len(lista1):#entra a la condicion en caso de que la lista temporal tenga menos registros que la lista recibida

                if p['apellido1']!=t['apellido1']:# en caso de que el apellido1 sea diferente en ambos registros se compara el apellido1

                    if p['apellido1']>t['apellido1']:
                        listaTemporal.append(t)
                    elif p['apellido1']<t['apellido1']:
                        listaTemporal.append(t)

                else:#en caso de que el apellido1 sea igual en ambos registros se compara el apellido2
                    if p['apellido2']>t['apellido2']:
                        listaTemporal.append(t)
                    elif p['apellido2']<t['apellido2']:
                        listaTemporal.append(t)
    return listaTemporal#devuelve la lista temporal como respuesta
    
respuesta=ordenarApellido(lista)#se llama la funcion de ordenamiento
print(respuesta)#se imprime la respuesta con la lista ordenada
