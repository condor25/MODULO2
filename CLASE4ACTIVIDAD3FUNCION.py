# importamos modulo

import random

# para cargar valores con ramdom (aleatorios)

numeroaleatorio = random.randint(1,100)
#print(numeroaleatorio)

def carga():
    numeroelegido = 0
    print("*** JUGAMOS A ADIVINE EL NUMERITO ***")
    numeroelegido = int(input("Ingrese nro elegido: "))
    print("El nro elegido es: ",numeroelegido)
    print("El nro aleatorio es: ",numeroaleatorio)
    if numeroelegido==numeroaleatorio:
        print("GANASTE!!! Usted adivino el nro")
    else:
        print("PERDISTE!!! NO ADIVINASTE")

