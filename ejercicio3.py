#realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el
#método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método
#para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora. 
class calculadora():
    def __init__(self):
        print("Bienvenidos a la calculadora")
        try:
            self.valor1=int(input("Ingrese el primer numero que desea calcular: "))
            self.valor2=int(input("Ingrese el segundo numero que desea calcular: "))
            #llamamos a los metodos para realizar las operaciones
            self.mostrar_resultados()
        except ValueError:
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
     #validamos que no haya dividir entre cero 
        if self.valor2 == 0:
            return "No se puede dividir por cero"
        return self.valor1 / self.valor2
    def mostrar_resultados(self):
                    print("el resultado de la suma es: ",self.suma)
                    print("el resultado de la resta es: ",self.resta)
                    print("el resultado de la multiplicación es: ",self.multiplicacion)
                    print("el resultado de la división es: ",self.division)
calculadora()
