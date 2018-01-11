
#Utilizando solo python elegir alguno de los siguientes problemas y solucionarlo (no use numpy) El archivo ejemplo.py contiene la solucion #al primer ejercicio. Puede utilizarlo para verificar su solucion o como ejemplo para resolver los demas. Los problemas fueron extraidos de #https://projecteuler.net/archives

#a) Si hacemos una lista de todos los numeros naturales debajo de 10 que sean multiplos de 3 o 5 obtendriamos 3, 5, 6 y 9. La suma de los #multiplos es 23. Encuentre la suma de todos los multiplos de 3 y 5 debajo de 1000.
import numpy as np

n=1000
a= range(1,n) #defined as a list
suma=0
for i in a:
    if (i%3)==0 or (i%5)==0:
        # print(i)
        suma =suma+i

print (suma)
# me dio 233168





