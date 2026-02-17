class Coche:
    def __init__(self):
        self.marca = "Chevy"
        self.modelo = "2004"
        self.color = "Gris"
        self.velocidad = 0
    
    def acelerar(self, velocidad):
        if velocidad > 0:
            self.velocidad += velocidad
            print(f"El coche aceleró {velocidad} km/h.")
        else:
            print("La velocidad a aumentar debe ser positiva.")

    def frenar(self, velocidad):
        if velocidad > 0:
            self.velocidad -= velocidad
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El coche frenó {velocidad} km/h.")
        else:
            print("La velocidad a disminuir debe ser positiva.")

    def mostrar_info(self):
        print("Información del coche:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad actual: {self.velocidad} km/h")

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0  # Inicialmente en 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso de ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro exitoso de ${cantidad:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo:.2f}")

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        print("Información del rectángulo:")
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")