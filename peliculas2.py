#Archivo de datos: peliculas.txt
#Titanic|1997|850
#El Padrino|1972|1200
#Matrix|1999|950
#Forrest Gump|1994|1100
#Avengers: Endgame|2019|1800
#________________________________________
#Objetivo:
#Gestionar un catálogo de películas cargado desde un archivo de texto. Algunas funciones están implementadas y otras deben ser completadas por usted.
#________________________________________
#Temas evaluados:
#	Lectura de archivos y manejo de listas
#•	Búsqueda secuencial
#•	Ordenamiento por año de estreno (método de selección)
#3•	Escritura en archivos
#________________________________________
#Código base para entregar a estudiantes:
# FUNCIONES DE BÚSQUEDA (ya implementada)
def busquedaSecuencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

# FUNCIONES COMPLETAS
def cargar_peliculas(nombre_archivo):
    peliculas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 3:
                titulo = partes[0]
                anio = int(partes[1])
                precio = int(partes[2])
                peliculas.append([titulo, anio, precio])
    return peliculas

def mostrar_peliculas(peliculas):
    print("\n--- Catálogo de Películas ---")
    for p in peliculas:
        print(f"Título: {p[0]} | Año: {p[1]} | Precio: ${p[2]}")
    print()

# FUNCIÓN INCOMPLETA A IMPLEMENTAR
def buscar_pelicula(peliculas):
    # TODO: Pedir título, buscarlo y mostrar año y precio si existe
    print("\n--- Búsqueda de Película ---")
    titulo_buscado = input("Ingrese el título de la película a buscar: ")
    # Crear una lista de títulos
    titulos = [p[0] for p in peliculas]  # Extraer títulos de las películas
    # Usar búsqueda secuencial
    if busquedaSecuencial(titulos, titulo_buscado):
        # Si se encuentra, mostrar título, año y precio
        for p in peliculas:
            if p[0] == titulo_buscado:
                print(f"Título: {p[0]} | Año: {p[1]} | Precio: ${p[2]}")
                return
    else:
        # Si no se encuentra, mostrar mensaje adecuado
        print("Película no encontrada.")
# Archivo de datos: peliculas.txt

# FUNCIÓN INCOMPLETA A IMPLEMENTAR
def ordenar_por_anio(peliculas):
    # TODO: Ordenar las películas por año usando el método de selección
    n = len(peliculas)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if peliculas[j][1] < peliculas[min_index][1]:  # Comparar años
                min_index = j
        # Intercambiar el elemento mínimo encontrado con el primer elemento
        peliculas[i], peliculas[min_index] = peliculas[min_index], peliculas[i]

def guardar_peliculas(peliculas, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for p in peliculas:
            linea = f"{p[0]}|{p[1]}|{p[2]}\n"
            archivo.write(linea)
    print("Películas guardadas correctamente.")

# PROGRAMA PRINCIPAL
def menu():
    nombre_archivo = "peliculas.txt"
    peliculas = cargar_peliculas(nombre_archivo)

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar todas las películas")
        print("2. Buscar película por título")
        print("3. Ordenar películas por año de estreno")
        print("4. Guardar cambios")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_peliculas(peliculas)
        elif opcion == "2":
            buscar_pelicula(peliculas)
        elif opcion == "3":
            ordenar_por_anio(peliculas)
        elif opcion == "4":
            guardar_peliculas(peliculas, nombre_archivo)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# EJECUCIÓN
menu()
#________________________________________
##Instrucciones para los estudiantes:
#1.	Completar buscar_pelicula(peliculas):
#	Pedir el título.
#	Crear una lista de títulos.
#	Usar búsqueda secuencial.
##	Si se encuentra, mostrar título, año y precio.
#	Si no, mostrar un mensaje adecuado.
#2.	Completar ordenar_por_anio(peliculas):
#	Implementar el método de selección para ordenar por el año de estreno (índice 1 de cada sublista).

