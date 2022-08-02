#Realizar un programa que simule tirar dos dados y luego muestre los valores que aparecieron.
# Si la suma de dichos números es igual a 9 mostrar un mensaje de “has ganado” sino mostrar “has perdido”.
# importar el modulo random, función randint()

# importamos el modulo random
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

print("*** Bienvenido a CASINO LA PALOMA ***")
print("El primer dado vale: ", dado1)
print("El segundo dado vale: ", dado2)
print("La suma de los dados es: ", suma)

if suma == 9:
    print("Has ganado")
else:
    print("Has perdido")