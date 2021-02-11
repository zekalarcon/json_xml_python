#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.axes


def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    

    datos_ezequiel = {
                     "nombre" : "Ezequiel",
                     "apellido" : "Alarcon",
                     "dni" : "32222222",
                     "prendas": [
                                { 
                                 "prenda" : "zapatillas",
                                 "cantidad" : 15
                                },
                                {
                                 "prenda" : "remeras",
                                 "cantidad" : 30   
                                },
                                {
                                 "prenda" : "medias",
                                 "cantidad" : 20
                                },
                                {
                                 "prenda" : "shorts",
                                 "cantidad" : 10
                                }
                                ]
                     }

    with open('Info_personal.json', 'w') as jsonfile:
        data = [datos_ezequiel]
        json.dump(data, jsonfile, indent = 4)


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    

    with open('info_personal.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Info personal')
    print(json.dumps(json_data, indent=4))\


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    
    tree = ET.parse('Info_personal.xml')
    root = tree.getroot()

    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)

def ej5():
    # Ejercicio de consumo de datos por API

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

   

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    dataset = response.json()
    print(dataset)
    filter_data = [x['userId'] for x in dataset if x.get('completed') is True]

    userId_1 = len([x for x in filter_data if x == 1 ])
    userId_2 = len([x for x in filter_data if x == 2 ])
    userId_3 = len([x for x in filter_data if x == 3 ])
    userId_4 = len([x for x in filter_data if x == 4 ])
    userId_5 = len([x for x in filter_data if x == 5 ])
    userId_6 = len([x for x in filter_data if x == 6 ])
    userId_7 = len([x for x in filter_data if x == 7 ])
    userId_8 = len([x for x in filter_data if x == 8 ])
    userId_9 = len([x for x in filter_data if x == 9 ])
    userId_10 = len([x for x in filter_data if x == 10 ])

    aprobadas = [userId_1, userId_2, userId_3, userId_4, userId_5, userId_6, userId_7, userId_8,
                 userId_9, userId_10]

    labels = ['userId 1', 'userId 2', 'userId 3', 'userId 4', 'userId 5', 'userId 6', 'userId 7',
              'userId 8', 'userId 9', 'userId 10']

    fig, ax = plt.subplots()
    fig.suptitle('Porcentaje aprobado por Alumno')

    ax.pie(aprobadas, labels = labels, autopct='%1.1f%%', startangle=180)
    ax.axis('equal') 

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    # ej3()
    #ej4()
    ej5()
