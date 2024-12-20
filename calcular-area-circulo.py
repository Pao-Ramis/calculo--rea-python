
import math

#1. Solicite al usuario que ingrese el radio del círculo que desea calcular

radio = float(input("Por favor, ingrese el radio del círculo: "))

#2. Calcular el área de círculo utilizando la fórmula área = p * radio al cuadrado 

area = math.pi * (radio **2)

#3. Mostrar al usuario el área calculada

print("El área del círculo con radio", radio, "es:", area)
