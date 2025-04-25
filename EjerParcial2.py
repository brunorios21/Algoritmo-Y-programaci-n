'''Propuesta de Ejercicio Integrador (Enunciado y consigna)
#Título: Sistema de Gestión de Turnos en un Centro Médico
#Enunciado:
#Desarrollar un sistema en Python que permita gestionar los turnos de atención en un centro
#médico. El sistema debe:
#•1 Registrar nuevos turnos (nombre del paciente, especialidad, horario).
#•2 Validar que el horario sea un número entre 8 y 18 (horas del día).
#•3 Guardar los turnos en una lista general de registros.
#•4 Mostrar los turnos pendientes por orden de llegada (uso de cola).
#•5 Permitir cancelar el último turno ingresado (uso de pila).
#•6 Validar entradas y manejar excepciones si se ingresa un dato incorrecto.
#•7 No usar funciones recursivas.
#R01. Requisitos técnicos:
#•1 Uso de clases (Turno, CentroMedico) para representar abstracciones.
#•2 Uso de listas, pilas y colas simuladas con listas.
#•3 Uso de estructuras de control (if, while, for) y funciones propias.
#•4 Ingreso de datos por consola y presentación clara de los turnos.
#•5 Manejo de errores con try / except.
'''
#Creamos la clase turno
class Turno:
    #1.Constructor de la clase turno
    def __init__(self, nombre, especialidad, horario):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario
class CentroMedico:
    #creamos el constructor de la clase centromMedico
    def __init__(self, nombre, especialidad, horario):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario
    #2.Creamos una funcion que valide los horarios entre 8 y 18 (horas del dia)
def validar_horario(self):
    try:
        if 8 <= self.horario <= 18:
            return True
        else:
            return False
    except:
        return

    
    #3. Creamos una lista vacia para guardar los turnos    
guardar_turnos = []
    #4. Creamos una lista vacia para guardar los turnos pendientes por orden de llegada (uso de colas)
guardar_turnos_pendientes = []
    #5. Creamos una lista vacia para guardar los turnos cancelados
guardar_turnos_cancelados = []
    #6. Creamos una funcion que nos permita registrar nuevos turnos (nombre del paciente, especialidad, horario)

def registrar_turno(self):
    nombre = input("Ingrese el nombre del paciente: ") #PEDIMOS AL USUARIO QUE INGRESE EL NOMBRE DEL PACIENTE
    especialidad = input("Ingrese la especialidad del paciente: ")#PEDIMOS AL USUARIO QUE ingrese la especialidad del paciente
    horario = int(input("Ingrese el horario del paciente: "))#PEDIMOS AL USUARIO QUE INGRESE EL HORARIO DEL PACIENTE
    self.guardar_turnos.append(self)
    self.guardar_turnos_pendientes.append(self)
    self.guardar_turnos_cancelados.append(self)
    print("Turno registrado exitosamente.")
#7. Creamos un objeto de la clase turno y lo agregamos a la lista de turnos
    nuevo_turno = Turno(nombre, especialidad, horario)
    self.guardar_turnos.append(nuevo_turno)#Agregamos a la lista nuevo_turno
    print("Turno registrado exitosamente.")
#8. Creamos una funcion que nos permita mostrar los turnos pendientes por orden de llegada (uso de colas)
def mostrar_turnos_pendientes(self):
    print("Turnos pendientes por orden de llegada:")
    for turno in self.guardar_turnos_pendientes:
        print(f"Nombre: {turno.nombre}, Especialidad: {turno.especialidad}, Horario: {turno.horario}")
#9. Creamos una funcion que nos permita cancelar el último turno ingresado (uso de pila)
def cancelar_turno(self):
    if len(self.guardar_turnos) == 0:
        print("No hay turnos pendientes para cancelar.")
    else:
        print("Turno cancelado exitosamente.")
#10. creamos una funcion para el menu principal
def main():
    while True:
        try:
            print("----Centro Médico----")
            print("----Menu de opciones----") 
            print("1. Registrar turno")
            print("2. Mostrar turnos pendientes")
            print("3. Cancelar turno")
            print("4. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.registrar_turno()
            elif opcion == 2:
                self.mostrar_turnos_pendientes()
            elif opcion == 3:
                self.cancelar_turno()
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida. Por favor, ingrese una opcion valida.")
        except ValueError:
            print("Opcion invalida. Por favor, ingrese una opcion valida.")
#creamos un objeto de la clase centro_medico y lo llamamos centro_medico

main()


