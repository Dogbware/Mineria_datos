#Ejercicio1 suma de N numeros
numero = int(input("Hasta que numero deseas sumar: "))
suma = 0
for i in range(1, numero+1):
    suma += i

print(suma)

#Ejercicio 2 Factorial de un numero
numeroPFactorial = int(input("Dime que numero quieres para sacar su factorial: "))
factorial = 1
for f in range(numeroPFactorial, 1, -1):
    factorial *= f

print(factorial)

#Ejercicio 3 tablas de multiplicar
numeromultiplo = int(input("Dime un numero para darte la tabla de multiplicar: "))
for f in range(1, 11):
    tabla = numeromultiplo * f
    print(f"{numeromultiplo} x {f} = {tabla}")

#Ejercicio 4 Calculo de promedio de notas
suma = 0
contador = 1

for _ in range(1000): 
    nota = float(input(f"Ingresa calificacion {contador}(negativa para terminar): "))

    if nota < 0:
        break

    suma += nota
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron notas válidas")


#Ejercicio 5 
numeropotencia = int(input("Selecciona la base: "))
potenciatotal = numeropotencia
potencia = int(input("Seleccione la potencia:"))
for p in range(1, potencia):
    potenciatotal = potenciatotal * numeropotencia
print(f"{numeropotencia} ⌃ {potencia} = {potenciatotal}")

#Ejercicio 6
numeroA = int(input("Seleccione el numero A: "))
numeroB = int(input("Selecciona el numero B"))
sumanumeros = 0
for n in range(numeroA, numeroB+1):
    if n%2==0:
        sumanumeros+=n
print(f"La suma de los pares en un rango del {numeroA} y {numeroB} es: {sumanumeros}")