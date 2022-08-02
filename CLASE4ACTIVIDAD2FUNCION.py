# importamos modulo

import random

# para cargar valores con ramdom (aleatorios)

def carga():
    lista=[]
    for x in range(10):
        numero = random.randint(1,1000)
        lista.append(numero)
    return lista

#funcion para imprimir lista

def imprimir(lista):
    print (lista)


