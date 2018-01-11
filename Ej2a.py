
# Se importan las libreria con las funciones que se van a utilizar
import numpy as np
import matplotlib.pyplot as pp
from pylab import * 

fold='/home/janisaseba/Dropbox/documentos/cursos/TecnicasDeProgramacionCientifica/ejercicios/labdia1/mios'
# Se definen los valores de x e y
x=array([7,5,4,48,8,60,7,73,5,28,4,25,6,99,6,31,9,15,5,06])
y=array([28,66,20,37,22,33,26,35,22,29,21,74,23,11,23,13,24,68,21,89])

# Grafico de los puntos en el plano x,y
fig=pp.figure()
pp.plot(x,y,"*",color='r',label='x vs y')
pp.title('Scatter plot y Vs. x')
pp.ylabel('y')
pp.grid(True)
pp.xlabel('x')
fig_fol=fold + '/xVsy_scatter.png'
print(fig_fol)
fig.savefig(fig_fol)
pp.show()
#m,b = np.polyfit(x, y, 1) 
#yaux=x*m+b
##print(yaux)
##x_si=np.size(x)
##yaux_si=np.size(yaux)
##print("x.shape = ",x_si)
##print("yaux.shape = ",yaux_si)
##print(m)
##print(b)
#pp.plot(x, y, 'yo', x, yaux, '--r')
##plot(x, y, 'yo', x, m*x+b, '--k') 
#pp.show() 
