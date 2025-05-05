#Título: Sistema de Gestión de Pedidos en un Restaurante
#Enunciado:
#Desarrollar un sistema en Python que permita gestionar los pedidos de un restaurante. El sistema debe:
#Registrar nuevos pedidos (nombre del cliente, plato solicitado, cantidad).
#Validar que la cantidad sea un número entero positivo.
#Guardar los pedidos en una lista general de registros.
#Mostrar los pedidos pendientes por orden de llegada (uso de cola).
#Permitir cancelar el último pedido ingresado (uso de pila).
#Validar entradas y manejar excepciones si se ingresa un dato incorrecto.
#No usar funciones recursivas.
#Requisitos técnicos:
#Uso de clases (Pedido, Restaurante) para representar abstracciones.
#Uso de listas, pilas y colas simuladas con listas.
#Uso de estructuras de control (if, while, for) y funciones propias.
#Ingreso de datos por consola y presentación clara de los pedidos.
#Manejo de errores con try / except.

#Creamos una clase Pedido para reservar un pedido
class Pedido:
    #Creamos el constructor de la clase Pedido
    def __init__(self, cliente, plato, cantidad):
        self.cliente = cliente
        self.plato = plato
        self.cantidad = cantidad
    #Creamos el metodo para mostrar los datos del pedido
    def mostrar(self):
        return f"{self.cliente} - {self.plato} - {self.cantidad}"
#Creamos una clase Restaurante para gestionar los pedidos
class Restaurante:
    def __init__(self):
        self.pedidos = [] #Lista general de pedidos
        self.cola_pedidos = [] #Cola de pedidos (Pendientes)
        self.pila_cancelados = [] #Pila para deshacer ultimo pedido cancelado
    #Creamos el metodo registrar_pedido para registrar un nuevo pedido
    def registrar_pedido(self):
        try: #Try es para manejar excepciones
            #Solicitamos al usuario que ingrese los datos del pedido
            cliente = input("Ingrese nombre del cliente: ")
            plato = input("Ingrese plato solicitado: ")
            cantidad = int(input("Ingrese cantidad:"))
            #Validamos que la canrtidad sea un numero entero positivo
            if cantidad <= 0: #Si la cantidad es menor o igual a 0
                print("Cantidad debe ser un número entero positivo.")
                return #Retornamos para salir del metodo
            #Creamos un nuevo objeto Pedido con los datos ingresados
            nuevo_pedido = Pedido(cliente, plato, cantidad)#Creamos un nuevo pedido (Pedido) con los datos ingresados
            self.pedidos.append(nuevo_pedido)#Agregamos el nuevo pedido a la lista de pedidos
            self.cola_pedidos.append(nuevo_pedido)#Agregamos el nuevo pedido a la cola de pedidos pendientes
            self.pila_cancelados.append(nuevo_pedido)#Agregamos el nuevo pedido a la pila de pedidos cancelados
            #Imprimimos un mensaje de pedido registrado correctamente
            print("Pedido registrado correctamente.")
        #Exepciones para manejar errores
        except ValueError:
            #Si se produce un error de valor (ValueError) al convertir la cantidad a entero 
            print("Error: la cantidad debe ser un número entero.")
    #Creamos el metodo ver_pedidos_pendientes para mostrar los pedidos pendientes
    def ver_pedidos_pendientes(self):
        if len(self.cola_pedidos) == 0:
            print("No hay pedidos pendientes.")
        else:
            print("Pedidos pendientes:")
            for pedido in self.cola_pedidos:
                print(pedido.mostrar())
    #Creamos el metodo cancelar_ultimo_pedido para cancelar el ultimo pedido ingresado
    def cancelar_ultimo_pedido(self):
        if len(self.pila_cancelados) == 0:
            print("No hay pedidos para cancelar.")
        else:
            #Cancelamos el ultimo pedido ingresado
            pedido_cancelado = self.pila_cancelados.pop()
            #Sacamos el ultimo pedido de la cola de pedidos pendientes
            self.cola_pedidos.remove(pedido_cancelado)
            print(f"Pedido cancelado: {pedido_cancelado.mostrar()}")
    #Creamos el metodo menu para mostrar el menu de opciones
    def menu(self):
        try: #Try es para manejar excepciones
            while True: #Iniciamos un bucle infinito para mostrar el menu de opciones
                print("1. Registrar nuevo pedido")
                print("2. Ver pedidos pendientes")
                print("3. Cancelar último pedido")
                print("4. Salir")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.registrar_pedido() #Llamamos al metodo registrar_pedido para registrar un nuevo pedido
                elif opcion == 2:
                    self.ver_pedidos_pendientes() #Llamamos al metodo ver_pedidos_pendientes para mostrar los pedidos pendientes
                elif opcion == 3:
                    self.cancelar_ultimo_pedido() #Llamamos al metodo cancelar_ultimo_pedido para cancelar el ultimo pedido ingresado
                elif opcion == 4:
                    print("Saliendo del sistema...") #Imprimimos un mensaje de salida del sistema
                    break #rompemos el bucle
                else:
                    print("Opción inválida. Intente nuevamente.") #Imprimimos un mensaje de error si la opcion es invalida
        except ValueError:
            print("Entrada inválida. Ingrese un número.") #Imprimimos un mensaje de error si la entrada es invalida
#Creamos el  objeto restaurante de la clase Restaurante
restaurante = Restaurante() #Creamos un nuevo objeto Restaurante
#Llamamos al metodo menu para mostrar el menu de opciones
restaurante.menu() #Llamamos al metodo menu para mostrar el menu de opciones
#Fin del programa
