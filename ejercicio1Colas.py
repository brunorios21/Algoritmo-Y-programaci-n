class Cola:
    def __init__(self):
        # La cola vacía se representa por una lista vacía
        self.clientes = []

    def encolar(self, x):
        # Método para agregar un cliente a la cola
        self.clientes.append(x)
        print(f"Cliente '{x}' agregado (encolado). Cola actualizada: {self.clientes}")

    def desencolar(self):
        # Método para atender (eliminar) al primer cliente de la cola
        if self.es_vacia():
            print("La cola está vacía. No hay más clientes.")
        else:
            cliente_atendido = self.clientes.pop(0)
            print(f"Cliente '{cliente_atendido}' atendido (desencolado). Cola actualizada: {self.clientes}")

    def es_vacia(self):
        # Método para verificar si la cola está vacía
        return self.clientes == []

    def mostrar(self):
        # Método para mostrar los clientes restantes en la cola
        if self.es_vacia():
            print("La cola está vacía.")
        else:
            print("Clientes en la cola (de primero a último):")
            for cliente in self.clientes:
                print(cliente)


# Función principal con un menú interactivo
def main():
    cola = Cola()
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Encolar cliente")
        print("2. Desencolar cliente")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4): ")

        if opcion == "1":
            while True:
                cliente = input("Ingrese el nombre del cliente (deje vacío y presione Enter para volver al menú): ")
                if cliente == "":
                    break
                cola.encolar(cliente)
        elif opcion == "2":
            cola.desencolar()
        elif opcion == "3":
            cola.mostrar()
        elif opcion == "4":
            print("\n--- Clientes en la cola antes de salir ---")
            cola.mostrar()
            print("¡Programa finalizado!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecutar el programa
main()
