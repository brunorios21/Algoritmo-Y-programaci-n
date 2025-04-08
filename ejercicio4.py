#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los
#métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo
#de triángulo que es (equilátero, isósceles o escaleno).
class triangulo:
    #Declaramos los atributos
    lado1=0
    lado2=0
    lado3=0
    #Inicializamos los atributos
    def inicializar(self):
        self.lado1=int(input("Ingrese el valor del lado 1: "))
        self.lado2=int(input("Ingrese el lado 2: "))
        self.lado3=int(input("Ingrese el lado 3: "))
    #Imprimimos
    def imprimir(self):
        print("Los lados del triangulo tienen el valor de: ")
        print("Lado 1: ",self.lado1)
        print("Lado 2: ",self.lado2)
        print("lado 3:", self.lado3)
    #Comprobamos el lado mayor
    def mayor(self):
        print("el lado mayor es:")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("Lado 1:",self.lado1)
        elif self.lado2>self.lado3:
            print("lado 2:", self.lado2)
        else:
            print("lado 3:", self.lado3)
#Comprobamos el tipo de triangulo
#equilatero -> todos los lados iguales
#Isoceles -> dos lados iguales
#escaleno -> todos los lados diferentes
    def tipo (self):
        if self.lado1==self.lado2 and self.lado1== self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1!=self.lado2 and self.lado3:
            print("es un triangulo escaleno")
        else:
            print("Es un triangulo isoceles")
#Bloque principal
figura= triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()