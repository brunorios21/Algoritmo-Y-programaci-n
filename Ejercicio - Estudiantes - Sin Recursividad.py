# Clase Estudiante (Abstracción y TDA - Tipo de Dato Abstracto)
class Estudiante:
    def __init__(self, nombre, notas):
        # Inicializamos los atributos: nombre del estudiante y sus notas
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        # Calculamos el promedio utilizando la función iterativa promedio_iterativo
        return promedio_iterativo(self.notas)

    def esta_aprobado(self):
        # Verificamos si el promedio es mayor o igual a 6 para determinar si está aprobado
        return self.calcular_promedio() >= 6


# Función iterativa para calcular el promedio
def promedio_iterativo(lista):
    # Si la lista está vacía, retornamos 0 para evitar división por cero
    if len(lista) == 0:
        return 0
    suma = 0  # Inicializamos la suma en 0
    for nota in lista:  # Iteramos sobre cada nota en la lista
        suma += nota  # Acumulamos las notas
    # Retornamos el promedio dividiendo la suma total por la cantidad de elementos
    return suma / len(lista)


# Función para solicitar las notas con validación
def ingresar_notas():
    notas = []  # Inicializamos la lista para almacenar las notas
    while True:  # Ciclo infinito para ingresar notas
        try:
            nota = input("Ingrese una nota (o 'fin' para terminar): ")  # Solicitamos una nota
            if nota.lower() == "fin":  # Si el usuario escribe 'fin', salimos del ciclo
                break
            nota = float(nota)  # Convertimos la entrada a tipo float
            if 0 <= nota <= 10:  # Validamos que la nota esté entre 0 y 10
                notas.append(nota)  # Agregamos la nota a la lista
            else:
                print("La nota debe estar entre 0 y 10.")  # Mensaje de error para valores fuera de rango
        except ValueError:
            # Mensaje de error para entradas que no sean numéricas
            print("Entrada inválida. Ingrese un número.")
    return notas  # Retornamos la lista de notas


# Función principal para coordinar el programa
def main():
    estudiantes = []  # Lista para almacenar objetos de tipo Estudiante
    while True:  # Ciclo infinito para registrar estudiantes
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")  # Solicitamos el nombre
        if nombre.lower() == "salir":  # Si el usuario escribe 'salir', salimos del ciclo
            break
        print(f"Ingrese las notas del estudiante {nombre}:")  # Indicamos que vamos a ingresar las notas
        notas = ingresar_notas()  # Llamamos a la función para registrar las notas
        estudiante = Estudiante(nombre, notas)  # Creamos un objeto Estudiante con el nombre y las notas
        estudiantes.append(estudiante)  # Agregamos el objeto Estudiante a la lista de estudiantes

    print("\n--- Resultados ---")  # Imprimimos un encabezado para los resultados
    for est in estudiantes:  # Iteramos sobre la lista de estudiantes
        try:
            promedio = est.calcular_promedio()  # Calculamos el promedio del estudiante
            if est.esta_aprobado():  # Determinamos si el estudiante está aprobado
                estado = "APROBADO"  # Mensaje si el estudiante está aprobado
            else:
                estado = "DESAPROBADO"  # Mensaje si el estudiante está desaprobado
            # Imprimimos los resultados con el nombre, promedio y estado del estudiante
            print(f"{est.nombre}: Promedio = {promedio:.2f} - {estado}")
        except Exception as e:
            # Mensaje de error si ocurre alguna excepción al procesar un estudiante
            print(f"Error al procesar al estudiante {est.nombre}: {e}")


# Ejecutar el programa llamando a la función principal
main()
