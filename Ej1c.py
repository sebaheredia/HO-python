
# Importamos la libreria con las funciones que se van a utilizar
import numpy as np

# Aqui se define el numero a descomponer en numeros primos
n=2*3*5*7
print("n = ",n)
# El primer divisor de prueba se define 2, ya que todo numero es divisible por 1
i=2
# aux es un valor auxiliar que seria el ultimo cociente  de la descomposicion con el ultimo numero primo
aux=n
# La condicion i <= n/2 se debe a que no va a haber ningun numero primo mayor a n/2
while i <= n/2:
#        print("i = ",i)
        if aux%i==0:
                aux=aux/i
                max_div=i
                print("max_div = ",max_div)
                print("aux = ",aux)
# Se sube e 1 el divisor propuesto
        i=i+1
# Se imprime el ultimo valor del maximo divisor
print("max_div = ",max_div)

