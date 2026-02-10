#Par o impar
numero_par_impar= 101
verificacion = numero_par_impar%2
if verificacion == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#positivo o negativo
numero_pos_neg = -23
if numero_par_impar >= 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

#mayor menor edad
edad = 23
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Aprobado reprobado
calificacion = 59
if calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#calificacion letras
calificacion_letra = 79
if calificacion_letra >=90:
    print("A")
elif calificacion_letra >=80:
    print("B")
elif calificacion_letra >=70:
    print("C")
elif calificacion_letra >=60:
    print("D")
else:
    print("F")

#Temperatura
temperatura = 80
if temperatura < 0:
    print("Solido")
elif temperatura >= 0 and temperatura <= 100:
    print("Liquido")
else:
    print("Gaseoso")
