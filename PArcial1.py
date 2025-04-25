#1. Propuesta de ejercicio integrador (Enunciado y consigna)
#Título: Sistema de Gestión de Pedidos en una Cafetería
#Enunciado:
#Desarrollar un sistema en Python que permita gestionar los pedidos de una cafetería. El
#sistema debe:
#•1 Registrar pedidos (nombre del cliente, producto, cantidad).
#•2 Calcular el total a pagar (con precios fijos por producto).
#•3 Almacenar los pedidos en una lista.
#•4 Permitir ver los pedidos pendientes (uso de colas).
#•5 Permitir deshacer el último pedido registrado (uso de pila).
#•6 Validar entradas y manejar excepciones si se ingresa un dato incorrecto.
#•7 Incorporar al menos una función recursiva (por ejemplo, para sumar los totales de
#los pedidos de forma recursiva).
#Requisitos técnicos:
#• Uso de clases (Pedido, Cafeteria) para representar abstracciones.
#• Uso de listas, pilas y colas (pueden ser listas simuladas).
#• Uso de funciones propias y estructuras condicionales y repetitivas.
#• Ingreso de datos por consola.
#Temas utilizados vistos hasta ahora para la resolución del ejercicio:
#• Tipos de datos (int, float, str, listas)
#• Variables
#• Condicionales
#• Ciclos
#• Listas y vectores (listas como estructuras secuenciales)
#• Funciones y funciones recursivas
#• Excepciones
#• Abstracción
#• Tipos de datos abstractos (clase con métodos)
#• Pilas y colas
#1.Creamos una clase para almacenar los pedidos
class Cafeteria:
    #Creamos un constructor para la clase Cafeteria
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
    #2.creamos una funcion para determinar  el total a pagar
    def calcular(self):
        self.total = self.cantidad * 100 #Calculamos el total a pagar con el precio del producto y la cantidad 
        print(f"El total a pagar es de {self.total}") # Mostramos el total a pagar
        return self.total #Retornamos el total a pagar
    #3.Creamos una funcion para almacenar los pedidos en una lista
    def almacenar(self):
        pedidos = [] #Creamos una lista vacia para almacenar los pedidos
        pedidos.append(self)# Agregamos los pedidos a una lista 
        return pedidos #Retornamos la lista de pedidos
    #4. creamos una funcion para ver los pedidos pendientes (uso de colas)
    def ver_pedidos(self):
        print("Ver pedidos pendientes: ")
        for pedido in self.pedidos: #Recorremos la lista de pedidos
            print(f"Cliente: {pedido} Producto: {pedido.producto} Cantidad: {pedido.cantidad} Total a pagar: {pedido.total} ")
    #5. Creamos una función para deshacer el ultimo pedido registrado (uso de pila)
    def deshacer_pedido(self):
        if len(self.pedidos) > 0: #verificamos si la lista de pedidos tiene elementos
            ultimo_pedido = self.pedidos.pop()#Eliminamos el ultimo pedido de la lista
            print(f"Se ha deshecho el pedido de {ultimo_pedido}")#Imprimimos que se ha deshecho el ultimo pedido
        else: #Si la lista de pedidos está vacia imprimimos que no hay mas pedidos pendientes
            print(f"No hay pedidos pendientes")
    #6. creamos una funcion para manejar excepciones si es que se ingresa un dato incorrecto
    def manejar_excepciones(self):
        try:
            cliente = input("Ingrese el nombre del cliente: ")#Pedimos al usuario que ingrese el nombre del cliente
            producto = input("Ingrese el producto: ") #pedimos al usuario que ingrese el producto
            cantidad = int(input("Ingrese la cantidad: "))#pedimos al usario que ingrese la cantidad de productos
            return cliente, producto, cantidad #retornamos los datos ingresados
        except ValueError: #Manejamos la excepcion si el usuario ingresa un dato incorrecto
            print("ERROR al ingresar los datos")
    #7. funcion que imprime el menu de opciones
    def menu(self):
        print("____Menu de opciones____")
        print("1. Registrar pedido")
        print("2. Ver pedidos pendientes")
        print("3. Deshacer pedido")
        print("4. Salir") 
        op= int (input("Ingrese la opcion: "))
        return op #retornamos la opcion del menu

    #8. funcion que maneja las opciones del menu
    def manejar_opcion(self, op):#Creamos una funcion que maneje las opciones del menu
        if op == 1: #Si el usuario elige la opcion 1 registra un nuevo pedido
            cliente, producto, cantidad = self.manejar_excepciones()#Llamamos a la función manejar_excepciones para manejar las excepciones
            pedido = Cafeteria(cliente, producto, cantidad)#Creamos un objeto de la clase Cafeteria
            self.pedido = pedido # Asignamos el objeto a la variable pedido
            self.pedidos = self.pedido.almacenar()#almacenamos los pedidos en una lista
            self.pedido.calcular()#calcula el total a pagar
            self.pedido.ver_pedidos()#Imprimimos los pedidos pendientes
        elif op == 2:#Si el usuario elige la opcion 2 ver pedidos
            self.pedido.ver_pedidos #imprimimos los pedidos pendientes
        elif op == 3: #si el usuario elige la opcion 3 deshacer pedido
            self.pedido.deshacer_pedido() #deshacemos el pedido
            self.almacenar()#almacenamos los pedidos en una lista
            print("Se ha deshecho el pedido")#Imprimimos que se ha deshecho el pedido
        elif op == 4: #Si el usuario elige la opcion 4 sale del programa
            print("Gracias por usar el programa")
        else: #Si el usuario ingresa una opcion incorrecta 
            print("EROR: OPCION INCORRECTA")
        self.manejar_opcion(self.menu())#volvemos a llamar a la funcion menu para que el usuario pueda elegir otra opcion

#9. creamos el programa principal
if __name__ == 'main'