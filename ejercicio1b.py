class alumno:
    #inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    #Función para obtener resultado 
    def resultado (self):
        if self.nota < 5:
            print("El alumno ha sido suspendido")
        else:
            print("El alumno ha aprobado")
    #Funcion para imprimir los datos
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
