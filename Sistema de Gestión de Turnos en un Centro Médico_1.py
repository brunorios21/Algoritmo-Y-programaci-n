#2. Propuesta de Ejercicio Integrador (Enunciado y consigna) 
#Título: Sistema de Gestión de Turnos en un Centro Médico 
#Enunciado: 
#Desarrollar un sistema en Python que permita gestionar los turnos de atención en un centro 
#médico. El sistema debe: 
#• Registrar nuevos turnos (nombre del paciente, especialidad, horario). 
#• Validar que el horario sea un número entre 8 y 18 (horas del día). 
#• Guardar los turnos en una lista general de registros. 
#• Mostrar los turnos pendientes por orden de llegada (uso de cola). 
#• Permitir cancelar el último turno ingresado (uso de pila). 
#• Validar entradas y manejar excepciones si se ingresa un dato incorrecto. 
#• No usar funciones recursivas. 
#_____________Requisitos técnicos:______________ 
#• Uso de clases (Turno, CentroMedico) para representar abstracciones. 
#• Uso de listas, pilas y colas simuladas con listas. 
#• Uso de estructuras de control (if, while, for) y funciones propias. 
#• Ingreso de datos por consola y presentación clara de los turnos. 
#• Manejo de errores con try / except.
#Creamos una clase Turno para representar un turno médico
class Turno:
    #Creamos el constructor de la clase Turno
    def __init__(self, paciente, especialidad, horario): #inciamos los atributos de la clase Turno
        self.paciente = paciente #Nommbre del paciente
        self.especialidad = especialidad #Especialidad del turno
        self.horario = horario #Horario del turno /8 a 18 hs 
#Creamos el metodo mostrar para mostrar los datos del turno
    def mostrar(self): #Self es la referencia al objeto actual
        #Retornamos una cadena formateada con los datos del turno
        return f"{self.paciente} - {self.especialidad} - {self.horario}:00 hs"
#Creamos una clase CentroMedico para gestionar los turnos
class CentroMedico: 
    def __init__(self): #Creamos el constructor de la clase CentroMedico
        #Inicializamos los atributos de la clase CentroMedico
        self.turnos = []         # Lista general de turnos
        self.cola_turnos = []    # Cola de turnos (pendientes) 
        self.pila_cancelados = [] # Pila para deshacer último turno cancelado
    #creamos el metodo registrar_turno para registrar un nuevo turno
    def registrar_turno(self): 
        try: #try es para manejar excepciones
            #Solicitamos al usuario que ingrese los datos del turno
            nombre = input("Ingrese nombre del paciente: ")
            especialidad = input("Ingrese especialidad: ")
            horario = int(input("Ingrese horario (8 a 18): "))
            #Validamos que el horario esté dentro del rango permitido
            if horario < 8 or horario > 18: #Si el horario es menor a 8 o mayor a 18
                #Imprimimos un mensaje de error
                print("Horario fuera del rango permitido.")
                return #Retornamos para salir del metodo
            #Creamos un nuevo objeto Turno  con los datos ingresados
            nuevo_turno = Turno(nombre, especialidad, horario) #Creamos un nuevo turno (Turno) con los datos ingresados
            self.turnos.append(nuevo_turno)#Agregamos el nuevo turno a la lista de turnos
            self.cola_turnos.append(nuevo_turno)#Agregamos el nuevo turno a la cola de turnos pendientes
            self.pila_cancelados.append(nuevo_turno)#Agregamos el nuevo turno a la pila de turnos cancelados
            #Imprimimos un mensaje de turno registrado correctamente
            print("Turno registrado correctamente.")
        #Exepciones para manejar errores
        except ValueError:
            #Si se produce un error de valor (ValueError) al convertir el horario a entero
            print("Error: el horario debe ser un número entero.")
    #Creamos el metodo ver_turnos_pendientes para mostrar los turnos pendientes
    def ver_turnos_pendientes(self):#Self es la referencia al objeto actual llamado CEntroMedico
        #Verificamos si la cola de turnos está vacía
        if len(self.cola_turnos) == 0:#SI la longitud de la cola de turnos es igual a 0
            #imprimimos un mensaje indicando que no hay turnos pendientes
            print("No hay turnos pendientes.")
        #Si la cola de turnos no está vacía, mostramos los turnos pendientes
        else:
        #Imprimimos un mensaje indicando que no hay turnos pendintes
            print("Turnos pendientes:")
            #Recorremos la cola de turnos y mostramos cada turno
            for turno in self.cola_turnos: #Recorremos la cola de turnos
                #Imprimimos el turno llamado al metodo mostrar de la clase Turno
                print("-", turno.mostrar())
    #Creamos el metodo cancelar_ultimo_turno para cancelar el ultimo turno ingresado
    def cancelar_ultimo_turno(self): 
        if len(self.pila_cancelados) == 0: #si la longitud de la pila de turnos cancelados es igual a 0
            print("No hay turnos para cancelar.") 
        else:
            ultimo = self.pila_cancelados.pop() #Sacamos el ultimo turno de la pila de turnos cancelados
            self.turnos.remove(ultimo) #eliminamos el turno de la lista de turnos
            self.cola_turnos.remove(ultimo) #eliminamos el turno de la cola de turnos pendientes
            print("Último turno cancelado:", ultimo.mostrar()) 
    #Creamos el metodo menu para mostrar el menu de opciones
    def menu(self): 
        while True: #Creamos un bucle infinito para mostrar el menu de opciones
            print("\n--- CENTRO MÉDICO ---")
            print("1. Registrar turno")
            print("2. Ver turnos pendientes")
            print("3. Cancelar último turno")
            print("4. Salir")
            #Solicitamos al usuario que seleccione una opción
            opcion = input("Seleccione una opción: ") 
            if opcion == "1": #Si la opcion es 1 
                #Llamamos al metodo registrar_turno para registrar un nuevo turno
                self.registrar_turno() #Llamamos al metodo registrar_turno para registrar un nuevo turno
            elif opcion == "2": #Si la opcion es 2
                #Llamamos al metodo ver_turnos_pendientes para ver los turnos pendientes
                self.ver_turnos_pendientes() #Llamamos al metodo ver_turnos_pendientes para ver los turnos pendientes
            elif opcion == "3": #Si la opcion es 3
                #Llamamos al metodo cancelar_ultimo_turno para cancelar el ultimo turno ingresado
                self.cancelar_ultimo_turno()#Llamamos al metodo cancelar_ultimo_turno para cancelar el ultimo turno ingresado
            #Si la opcion es 4        
            elif opcion == "4":# #Si la opcion es 4
                print("Saliendo del sistema...")
                break# #Salimos del bucle y del programa
            else:
                print("Opción inválida. Intente nuevamente.")

# Ejecución del programa
centro = CentroMedico()
#Creamos un objeto de la clase CentroMedico
centro.menu()
