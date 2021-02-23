"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con mas views en un país correspondientes a una categoría")
    print("3- Requerimiento 2")
    print("4- Requerimiento 4")
    print("5- Requerimiento 5")
    print("0- Salir")


def initCatalog(estructura):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(estructura)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def crearSubList(lista, tamanhoMuestra):

    return controller.crearSubList(lista, tamanhoMuestra)

def insertionSort(sublista):

    return controller.insertionSort(sublista)

def selectionSort(sublista):

    return controller.selectionSort(sublista)

def shellSort(sublista):

    return controller.shellSort(sublista)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Escoja la estructura de datos que desa utilizar para almacenamiento del repositorio: ")
        print("1. Lista por arreglos")
        print("2. Lista Enlazada")
        estructuraDatos= int(input())

        if estructuraDatos == 1:
            estructura= "ARRAY_LIST"

            print("Cargando información de los archivos ....")
            catalog = initCatalog(estructura)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            
            videos = catalog['videos']
            video = lt.getElement(videos, 1)
            primero = (video['title'], video['channel_title'], video['trending_date'], 
            video['country'], video['views'], video['likes'], video['dislikes'])
            print("Caracteristicas del primer video cargado: ")
            print("Titulo: " + primero[0])
            print("Canal: " + primero[1])
            print("Fecha en que estuvo Trending: " + primero[2])
            print("País: " + primero[3])
            print("Visitas: " + primero[4])
            print("Likes: " + primero[5])
            print("Dislikes: " + primero[6])
            print("Categorias de videos: ")
            for x in range(1, lt.size(catalog['id_category'])+1):
                elemento= lt.getElement(catalog['id_category'], x)
                print(elemento["id\tname"])
        
        elif estructuraDatos == 2:
            estructura= "LINKED_LIST"

            print("Cargando información de los archivos ....")
            catalog = initCatalog(estructura)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
                
            videos = catalog['videos']
            video = lt.getElement(videos, 1)
            primero = (video['title'], video['channel_title'], video['trending_date'], 
            video['country'], video['views'], video['likes'], video['dislikes'])
            print("Caracteristicas del primer video cargado: ")
            print("Titulo: " + primero[0])
            print("Canal: " + primero[1])
            print("Fecha en que estuvo Trending: " + primero[2])
            print("País: " + primero[3])
            print("Visitas: " + primero[4])
            print("Likes: " + primero[5])
            print("Dislikes: " + primero[6])
            print("Categorias de videos: ")
            for x in range(1, lt.size(catalog['id_category'])+1):
                elemento= lt.getElement(catalog['id_category'], x)
                print(elemento["id\tname"])

        else:
            print("Por favor escoja una opciòn válida")        

       

    elif int(inputs[0]) == 2:

        tamanhoMuestra= int(input("Ingrese el tamaño de la muestra que quiere analizar: "))
        lista= catalog["videos"]

        if tamanhoMuestra > lt.size(lista):
             print("Por favor escoja un tamaño de muestra menor o igual al número total de videos")
        
        else:

            sublista= crearSubList(lista, tamanhoMuestra)

            print("Seleccione el tipo de algoritmo de ordenamiento iterativo que desea utilizar: ")
            print("1. Selection Sort")
            print("2. Insertion Sort")
            print("3. Shell Sort")
            opcion= int(input())

            if opcion == 1:

                print(selectionSort(sublista))

            elif opcion == 2:

                print(insertionSort(sublista))

            elif opcion == 3:

                print(shellSort(sublista))

            else:
                print("Por favor seleccione una opción válida")




    else: 
        sys.exit(0)
sys.exit(0)
#Paths de los archivos y formatos de los prints