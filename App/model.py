"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sha
from DISClib.Algorithms.Sorting import insertionsort as ia
from DISClib.Algorithms.Sorting import selectionsort as sa
from DISClib.Algorithms.Sorting import quicksort as qk
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(estructura):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'id_category':None}

    catalog['videos'] = lt.newList(estructura)
    catalog['id_category'] = lt.newList(estructura)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)



def addCategory(catalog, category):

    lt.addLast(catalog['id_category'], category)

  
# Funciones para creacion de datos

# Funciones de consulta
def crearSubList(lista, tamanhoMuestra):

   return lt.subList(lista, 1, tamanhoMuestra)


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):

    valor= None
    if int(video1["views"]) < int(video2["views"]):
        valor= True
    
    else:
        valor= False

    return valor

# Funciones de ordenamiento

def insertionSort(sublista):

    startTime= time.process_time()
    
    ia.sort(sublista, cmpVideosByViews)

    stopTime= time.process_time()

    totalTime_msc= (stopTime - startTime) * 1000

    return totalTime_msc

def selectionSort(sublista):

    startTime= time.process_time()

    sa.sort(sublista, cmpVideosByViews)
    
    stopTime= time.process_time()

    totalTime_msc= (stopTime - startTime) * 1000

    return totalTime_msc

def shellSort(sublista):

    startTime= time.process_time()

    sha.sort(sublista, cmpVideosByViews)

    stopTime= time.process_time()

    totalTime_msc= (stopTime - startTime) * 1000

    return totalTime_msc

def quickSort(sublista):

    startTime= time.process_time()

    qk.sort(sublista, cmpVideosByViews)

    stopTime= time.process_time()

    totalTime_msc= (stopTime - startTime) * 1000

    return totalTime_msc


def mergeSort(sublista):

    startTime= time.process_time()

    mg.sort(sublista, cmpVideosByViews)

    stopTime= time.process_time()

    totalTime_msc= (stopTime - startTime) * 1000

    return totalTime_msc


