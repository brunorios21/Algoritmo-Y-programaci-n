class Calculadora:
    def __init__(self):
        print("Bienvenidos a la calculadora")
        try:
            self.valor1 = int(input("Ingrese el primer número que desea calcular: "))
            self.valor2 = int(input("Ingrese el segundo número que desea calcular: "))
            
            # Llamamos a los métodos y mostramos los resultados
        except ValueError:
            self.mostrar_resultados()
            print("No se ha definido un valor correcto, intente nuevamente")
        finally:
            print("Gracias por utilizar calculadora")
       
    def suma(self):
        return self.valor1 + self.valor2
    
    def resta(self):
        return self.valor1 - self.valor2
    
    def multiplicacion(self):
        return self.valor1 * self.valor2
    
    def division(self):
        # Validamos que no haya división por cero
        if self.valor2 == 0:
            return "No se puede dividir entre cero"
        return self.valor1 / self.valor2
    
    def mostrar_resultados(self):
        print("El resultado de la suma es: ", self.suma())
        print("El resultado de la resta es: ", self.resta())
        print("El resultado de la multiplicación es: ", self.multiplicacion())
        print("El resultado de la división es: ", self.division())

# Bloque principal
Calculadora()
# 