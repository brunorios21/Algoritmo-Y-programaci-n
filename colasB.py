class Cola:
    def __init__(self):
        # La cola vacía se representa por una lista vacía
        self.clientes = []

    def encolar(self, x):
        # Método para agregar un cliente a la cola
        self.clientes.append(x)
        print(f"Cliente {x} agregado (encolado). Cola actualizada: {self.clientes}")

    def desencolar(self):
        # Método para atender (eliminar) al primer cliente de la cola
        if self.es_vacia():
            print("La cola está vacía. No hay más clientes.")
        else:
            cliente_atendido = self.clientes.pop(0)
            print(f"Cliente {cliente_atendido} atendido (desencolado). Cola actualizada: {self.clientes}")

    def es_vacia(self):
        # Método para verificar si la cola está vacía
        return self.clientes == []

    def mostrar(self):
        # Método para mostrar los clientes restantes en la cola
        print(f"Turnos: {self.clientes}")


# Bloque principal: creación de una instancia de la clase Cola y ejecución de métodos
cola_banco = Cola()

# Agregar (encolar) clientes
cola_banco.encolar(10)
cola_banco.encolar(11)
cola_banco.encolar(12)

# Desencolar (atender) al primer cliente en la cola
cola_banco.desencolar()

# Agregar un nuevo cliente a la cola
cola_banco.encolar(13)

# Mostrar los clientes restantes y su posición en la cola
cola_banco.mostrar()
