
#Utilizando solo python elegir alguno de los siguientes problemas y solucionarlo (no use numpy) El archivo ejemplo.py contiene la solucion #al primer ejercicio. Puede utilizarlo para verificar su solucion o como ejemplo para resolver los demas. Los problemas fueron extraidos de #https://projecteuler.net/archives

#a) Si hacemos una lista de todos los numeros naturales debajo de 10 que sean multiplos de 3 o 5 obtendriamos 3, 5, 6 y 9. La suma de los #multiplos es 23. Encuentre la suma de todos los multiplos de 3 y 5 debajo de 1000.

# Importamos la libreria con las funciones que se van a utilizar
import numpy as np

# Aqui se define el numero a probar
n=1000
# Se crea un vector que vaya de 0 a n-1
a= range(1,n) #defined as a list
# Se define un valor auxiliar que sera la suma parcial
suma=0
for i in a:
# Esta es la condicion se es multiplo de 3 o 5 hace lo que esta dentro del if
    if (i%3)==0 or (i%5)==0:
        # print(i)
        suma =suma+i
# Imprime el valor final de la suma
print ("El valor final de la suma es = ",suma)
# ('El valor final de la suma es = ', 233168)






