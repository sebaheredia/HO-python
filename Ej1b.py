
# Importamos la libreria con las funciones que se van a utilizar
import numpy as np

# Se definen los valores iniciales de las variables: suma, amin1, amin2
suma = 0
amin1=0
amin2=1
# Se define el corte en la serie de Fibonacci
corte=1000000
# Valor inicial de la variable fibonacci
fibonacci=0
while fibonacci < corte:
# Si fibonacci es impar hace la suma parcial del termino
        if (fibonacci%2==1):
                suma=suma+fibonacci
#                print('La suma es: ',suma)
# Se actualizan los valores del termino de la serie fibonacci, amin1 y amin2
        fibonacci=amin1+amin2
#        print('El termino fibonacci es: ',fibonacci)
        amin1=amin2
        amin2=fibonacci
# Se imprime el valor final de la suma
print("La suma total de los numeros impares de la serie de Fibonacci menores a ",corte," es ",suma)
#'La suma total de los numeros impares de la serie de Fibonacci menores a ', 1000000, ' es ', 1089153

