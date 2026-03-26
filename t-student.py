import numpy as np
from scipy import stats
#ejercicio1
tiempos_resolucion1 = [
    48, 50, 42, 44, 55, 39, 41, 47, 49, 52, 
    43, 40, 46, 45, 51, 48, 38, 44, 47, 50, 
    42, 46, 49, 43, 45
]

media_afirmada1 = 45

t_stat1, p_value1 = stats.ttest_1samp(tiempos_resolucion1, media_afirmada1)

print(f"Media de la muestra: {np.mean(tiempos_resolucion1):.2f} minutos")
print(f"Estadístico T: {t_stat1:.4f}")
print(f"Valor p (p-value): {p_value1:.4f}")

alpha1 = 0.05
if p_value1 < alpha1:
    print("\nResultado: Rechazamos la hipótesis nula.")
    print("Hay evidencia suficiente para decir que el tiempo es SIGNIFICATIVAMENTE DIFERENTE de 45 min.")
else:
    print("\nResultado: No podemos rechazar la hipótesis nula.")
    print("No hay diferencia significativa; la afirmación de la empresa parece válida.")

#Ejercicio4
jovenes2 = [210, 225, 190, 240, 215, 205, 200, 230, 220, 210, 
           195, 225, 235, 200, 210, 205, 190, 215, 220, 230]

adultos_mayores2 = [310, 350, 290, 320, 340, 305, 315, 330, 360, 325, 
                   310, 345, 300, 315, 335, 320, 355, 310, 305, 340]

t_stat, p_value2 = stats.ttest_ind(jovenes2, adultos_mayores2)

print(f"Promedio Jóvenes: {np.mean(jovenes2):.2f} ms")
print(f"Promedio Adultos Mayores: {np.mean(adultos_mayores2):.2f} ms")
print(f"Valor p (p-value): {p_value2:.10f}") # Usamos muchos decimales porque suele ser muy pequeño

alpha2 = 0.05
if p_value2 < alpha2:
    print("\nResultado: Diferencia SIGNIFICATIVA.")
    print("La edad sí influye en la velocidad de reacción.")
else:
    print("\nResultado: No hay diferencia significativa.")
    print("La velocidad de reacción es similar en ambos grupos.")

#ejercicio7
antes3 = [15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7]
despues3 = [15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8]

t_stat3, p_value3 = stats.ttest_rel(antes3, despues3)

crecimiento_promedio3 = np.mean(despues3) - np.mean(antes3)

print(f"Crecimiento promedio: {crecimiento_promedio3:.2f} cm")
print(f"Estadístico T: {t_stat3:.4f}")
print(f"Valor p (p-value): {p_value3:.4f}")

alpha3 = 0.05
if p_value3 < alpha3:
    print("\nResultado: ¡Crecimiento SIGNIFICATIVO!")
    print("El fertilizante sí tuvo un efecto real en las plantas.")
else:
    print("\nResultado: No hay crecimiento significativo.")
    print("La diferencia es tan pequeña que pudo ser por error de medición o azar.")