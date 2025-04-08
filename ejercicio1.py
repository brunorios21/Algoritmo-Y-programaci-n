#1. Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el
#nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y
#mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
#¡No utilice el constructor!.
#iniciamos la clase
class alumno:
    #inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    #funcion para imprimir los datos
    def imprimir(self):
        print("nombre: ",self.nombre)
        print("nota: ",self.nota)
    #Función para obtener resultado 
    def resultado (self):
        if self.nota < 5:
            print("El alumno ha sido suspendido")
        else:
            print("El alumno ha aprobado")
#Bloque principal
#creamos los nuevos objetos
alumno1=alumno()
alumno2=alumno()

#Inicializamos los atributos
alumno1.inicializar("juan",8)
alumno2.inicializar("pepe",3)

#Imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()