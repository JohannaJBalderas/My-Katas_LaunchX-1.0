## Un Programa Python

from numpy import product
from pyparsing import java_style_comment

sum=1+2
print(sum)

#PRINT
#Impresión en pantalla print ("Hola desde la consola")
print('Hola desde la consola')

#VARIABLES
sum=1+2 # 3
product=sum*2
print(product) 

#TIPOS DE DATOS
# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)

#FECHA
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

#CONVERSIÓN DE TIPO DE DATOS
print("Today's date is: " + str(date.today()))

#RECOPILAR INFORMACIÓN
# Entrada del usuario
print("Bienvenido al programa de bienvenida")
print("Siga las intrucciones que a continuación se muestran:")
name = input("Introduzca su nombre: ")
edad = input ("Introduzca su edad: ")
print("Saludos: " + name)
print("Su edad es de:"+ edad)

#Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))
