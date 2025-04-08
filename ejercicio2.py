#2. Realizar un programa que tenga una clase Persona con las siguientes características. La clase
#tendrá como atributos el nombre y la edad de una persona. Implementar los métodos
#necesarios para inicializar los atributos utilizando el constructor (__init__), mostrar los datos e
#indicar si la persona es mayor de edad o no.

#Creamos la clase
class persona():
    #Creamos el constructor
    def __init__(self, nombre, edad):
        #sus atributos
        self.nombre = nombre
        self.edad = edad
    #metodo para mostrar los datos
    def imprimirDATOS(self):
        print("el nombre de la persona es: ",self.nombre)
        print("la edad de la persona es: ",self.edad)
    #COMPROBAMOS LA EDAD
    def mayor_edad (self):
        if self.edad >= 18:
            print("es mayor de edad")
        else:
            print("Es menor de edad")
#bloque principal
persona1 = persona("Bruno", 15)
persona2 = persona("Julian",45)
#Imprimimos datos y comprobamos si es mayor de edad
persona1.imprimirDATOS()
persona1.mayor_edad()
persona2.imprimirDATOS()
persona2.mayor_edad()