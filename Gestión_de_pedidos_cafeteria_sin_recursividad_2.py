# Sistema de Gestión de Pedidos en una Cafetería

# Clase que representa un pedido
class Pedido:
    def __init__(self, cliente, producto, cantidad, precio_unitario):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cliente} pidió {self.cantidad} {self.producto}(s) - Total: ${self.total()}"


# Función recursiva que calcula el total de todos los pedidos
def total_no_recursivo(pedidos):
    total = 0
    for pedido in pedidos:
        total += pedido.total()
    return total



# Precios fijos de los productos
precios_productos = {
    "Café": 200,
    "Té": 150,
    "Tostada": 180,
    "Medialuna": 120
}

# Estructuras de datos: cola para los pedidos y pila para deshacer
cola_pedidos = []  # FIFO
pila_ultimos = []  # LIFO


# Menú principal del sistema
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar pedido")
        print("2. Ver pedidos pendientes")
        print("3. Deshacer último pedido")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                cliente = input("Nombre del cliente: ")
                producto = input("Ingrese el nombre del producto: ")
                if producto not in precios_productos:
                    raise ValueError("Producto no válido.")

                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a 0.")

                precio = precios_productos[producto]
                nuevo_pedido = Pedido(cliente, producto, cantidad, precio)
                cola_pedidos.append(nuevo_pedido)
                pila_ultimos.append(nuevo_pedido)
                print("Pedido registrado correctamente.")

            except ValueError as ve:
                print("Error:", ve)

        elif opcion == "2":
            if not cola_pedidos:
                print("No hay pedidos pendientes.")
            else:
                print("\nPEDIDOS PENDIENTES:")
                for p in cola_pedidos:
                    print("-", p)

        elif opcion == "3":
            if pila_ultimos:
                eliminado = pila_ultimos.pop()
                cola_pedidos.remove(eliminado)
                print("Último pedido cancelado:", eliminado)
            else:
                print("No hay pedidos para deshacer.")

        elif opcion == "4":
            total = total_no_recursivo(cola_pedidos)
            print(f"Total acumulado de todos los pedidos: ${total}")

        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Iniciar el sistema
menu()
