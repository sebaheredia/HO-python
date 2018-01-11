
# Se importan las libreria con las funciones que se van a utilizar
import numpy as np
import matplotlib.pyplot as pp
from pylab import * 

# Carpeta local
local_fol='/home/janisaseba/Dropbox/documentos/cursos/TecnicasDeProgramacionCientifica/ejercicios/labdia1/mios'
# Se definen los valores de x e y
x=array([7,5,4,48,8,60,7,73,5,28,4,25,6,99,6,31,9,15,5,06])
y=array([28,66,20,37,22,33,26,35,22,29,21,74,23,11,23,13,24,68,21,89])

# Grafico de los puntos en el plano x,y
fig=pp.figure()
line1, =pp.plot(x,y,"*",color='b')
pp.title('Scatter plot y Vs. x')
pp.ylabel('Eje y')
pp.grid(True)
pp.xlabel('Eje x')
# direccion donde se va a guardar la figura
fig_fol=local_fol + '/xVsy_scatter.png'
# Se guarda la figura
fig.savefig(fig_fol)

# Calculo de los coeficientes del ajuste lineal
m,b = np.polyfit(x, y, 1) 
# Calcuo de valor de "y" segun el ajuste
yaux=x*m+b
# Grafico de los valores interpolados
line2, =pp.plot(x,yaux, '--r')
pp.legend([line1,line2], ['Valores Originales', 'Valores Interpolados'])
fig_fol2=local_fol + '/x-y_Vs_xyinterpolated_scatter.png'
# Se guarda la figura
fig.savefig(fig_fol2)
pp.show() 



