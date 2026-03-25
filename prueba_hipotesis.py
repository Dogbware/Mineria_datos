import numpy as np
from scipy import stats
import pandas as pd
#ejercicio_1
# Datos
mu_0_1 = 10
x_bar_1 = 9.7
s1 = 0.5
n1 = 49
alpha1 = 0.01

# Estadístico t
t1 = (x_bar_1 - mu_0_1) / (s1 / np.sqrt(n1))

# Grados de libertad
df_11 = n1 - 1

# p-value (cola izquierda)
p_value1 = stats.t.cdf(t1, df_11)

print("t =", t1)
print("p-value =", p_value1)

# Decisión
if p_value1 < alpha1:
    print("Rechazamos H0")
else:
    print("No se rechaza H0")
#df
df1 = pd.DataFrame({
    'Parametros' : ['Media Teorica', 'Media Muestral', 'Desviacion estandar', 'Tamano de la muestra', 'Z-calculado', 'Z-critico', 'Conclusion'],
    'valores' : [mu_0_1, x_bar_1,s1,n1,t1,p_value1, 'Rechazar la hipotesis nula' if t1 > p_value1 else 'No rechazar la hipotesis nula']
})

#Ejercicio 2
# Datos
mu_0_2 = 20
x_bar_2 = 18.5
s2 = 2.5
n2 = 30
alpha2 = 0.05

# Estadístico t
t2 = (x_bar_2 - mu_0_2) / (s2 / np.sqrt(n2))

# Grados de libertad
df22 = n2 - 1

# p-value (cola izquierda)
p_value2 = stats.t.cdf(t2, df22)

print("t =", t2)
print("p-value =", p_value2)

# Decisión
if p_value2 < alpha2:
    print("Rechazamos H0")
else:
    print("No se rechaza H0")

df1 = pd.DataFrame({
    'Parametros' : ['Media Teorica', 'Media Muestral', 'Desviacion estandar', 'Tamano de la muestra', 'Z-calculado', 'Z-critico', 'Conclusion'],
    'valores' : [mu_0_2, x_bar_2,s2,n2,t2,p_value2, 'Rechazar la hipotesis nula' if t1 > p_value1 else 'No rechazar la hipotesis nula']
})

#Ejercicio 3

mu_0_3 = 1000
x_bar_3 = 990
s3 = 12
n3 = 40
alpha3 = 0.02

t3 = (x_bar_3 - mu_0_3) / (s3 / np.sqrt(n3))
df33 = n3 - 1
p_value3 = stats.t.cdf(t3, df33)

print("t =", t3)
print("p-value =", p_value3)

if p_value3 < alpha3:
    print("Rechazamos H0")
else:
    print("No se rechaza H0")

df3 = pd.DataFrame({
    'Parametros' : ['Media Teorica', 'Media Muestral', 'Desviacion estandar', 'Tamano de la muestra', 'Z-calculado', 'Z-critico', 'Conclusion'],
    'valores' : [mu_0_3, x_bar_3,s3,n3,t3,p_value3, 'Rechazar la hipotesis nula' if t1 > p_value1 else 'No rechazar la hipotesis nula']
})