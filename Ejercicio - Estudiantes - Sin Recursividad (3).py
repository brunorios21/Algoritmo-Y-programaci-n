# Clase Estudiante (Abstracción y TDA)
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        return promedio_iterativo(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= 6

# Función iterativa para calcular el promedio
def promedio_iterativo(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for nota in lista:
        suma += nota
    return suma / len(lista)

# Función para solicitar notas con validación
def ingresar_notas():
    notas = []
    while True:
        try:
            nota = input("Ingrese una nota (o 'fin' para terminar): ")
            if nota.lower() == "fin":
                break
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    return notas

# Función principal
def main():
    estudiantes = []
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        print(f"Ingrese las notas del estudiante {nombre}:")
        notas = ingresar_notas()
        estudiante = Estudiante(nombre, notas)
        estudiantes.append(estudiante)

    print("\n--- Resultados ---")
    for est in estudiantes:
        try:
            promedio = est.calcular_promedio()
            if est.esta_aprobado():
                estado = "APROBADO"
            else:
                estado = "DESAPROBADO"
            # Versión mas corta
            #estado = "APROBADO" if est.esta_aprobado() else "DESAPROBADO"
            print(f"{est.nombre}: Promedio = {promedio:.2f} - {estado}")
        except Exception as e:
            print(f"Error al procesar al estudiante {est.nombre}: {e}")

# Ejecutar programa
main()
