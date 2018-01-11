# Se importan las libreria con las funciones que se van a utilizar
import numpy as np
import matplotlib.pyplot as pp

# Carpeta local
local_fol='/home/janisaseba/Dropbox/documentos/cursos/TecnicasDeProgramacionCientifica/ejercicios/labdia1/mios'
# Variable independiente - vector x
x=np.arange(-10,10,0.1)
# Coeficientes del polinomio en orden decreciente
pol=np.array([1,1,-4,4])
# Se evalua el poliinomio en los valores de x
pol_val=np.polyval(pol,x)
# Calculo de la derivada. El primer argumento de polyder es el polinomio, el segundo es el orden de la derivada
pol_der=np.polyder(pol,1)
# se evalua la derivada en x
pol_der_val=np.polyval(pol_der,x)

# Grafico del polinomio y su derivada en funcion de x
fig=pp.figure()
line1, =pp.plot(x,pol_val,".-",color='b')
line2, =pp.plot(x,pol_der_val,".-",color='r')
pp.title('Grafico del Polinomio y su derivada')
pp.ylabel('Eje y')
pp.grid(True)
pp.xlabel('Eje x')
pp.legend([line1,line2], ['Valores del Polinomio', 'Valores de la Derivada'])
fig_fol=local_fol + '/PolinomioYDerivada.png'
fig.savefig(fig_fol)
pp.show()

# Se ordenan las variables en columnas
c=zip(x,pol_val,pol_der_val)
# Escritura de las variables en un archivo de texto
np.savetxt("PolAndDer.txt", c, delimiter='   ', header="        Valores de x            Valores del Polinomio   Valores de la Derivada", comments="")










