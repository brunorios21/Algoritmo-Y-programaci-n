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
#•	Lectura de archivos y manejo de listas
#•	Búsqueda secuencial
#•	Ordenamiento por año de estreno (método de selección)
#•	Escritura en archivos
#________________________________________
#Código base para entregar a estudiantes:
# FUNCIONES DE BÚSQUEDA (ya implementadas)
#Función de búsqueda secuencial que toma una lista y un elemento a buscar.

def busquedaSecuencial(lista, item):
    # Recorremos la lista y comparamos cada elemento con el item buscado
    #Longitud de la lista
    for i in range(len(lista)):
        #SI el elemento en la posició i de la lista es igual al item buscado
        if lista[i] == item:
            return True
    return False

# FUNCIONES COMPLETAS
def cargar_peliculas(nombre_archivo):
    #cargar peliculas desde un archivo de texto
    peliculas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        #Recorrer cada linea del archivo
        #y dividirla en partes usando el separador "|"
        for linea in archivo:
            # Eliminar espacios en blanco al inicio y al final de la línea
            partes = linea.strip().split("|")
            #Si la longitud de partes es 3, significa que tenemos un título, año y precio
            if len(partes) == 3:
                titulo = partes[0]#El titulo es el primer elemento [0]
                anio = int(partes[1])#El año es el segundo elemento [1] y lo convertimos a entero
                precio = int(partes[2])#El precio es el tercer elemento [2] y lo convertimos a entero
                peliculas.append([titulo, anio, precio])
    #Si el archivo no se encuentra, se maneja la excepción
    return peliculas
# Función para mostrar las películas cargadas
def mostrar_peliculas(peliculas):
    # Imprimir el encabezado de la lista de películas
    print("\n--- Catálogo de Películas ---")
    # Recorrer la lista de películas y mostrar el título, año y precio de cada película
    for p in peliculas:
        # Cada película es una sublista con el título, año y precio
        # p[0] es el título, p[1] es el año y p[2] es el precio
        print(f"Título: {p[0]} | Año: {p[1]} | Precio: ${p[2]}")
    # Imprimir una línea en blanco para separar la salida
    print()

# FUNCIÓN INCOMPLETA A IMPLEMENTAR
def buscar_pelicula(peliculas):
    # Pedir el título de la película a buscar
    # TODO: Pedir título, buscarlo y mostrar año y precio si existe
    # Se solicita al usuario que ingrese el título de la película a buscar
    print("\n--- Búsqueda de Película ---")
    # Solicitar el título de la película
    titulo_buscado = input("Ingrese el título de la película a buscar: ")
    # Crear una lista de títulos de las películas
    # Esta lista se usará para realizar la búsqueda secuencial   
    titulos = [p[0] for p in peliculas]  # Crear lista de títulos
    # Llamar a la función de búsqueda secuencial para verificar si el título existe
    if busquedaSecuencial(titulos, titulo_buscado):
        # Si se encuentra el título, mostrar el año y el precio
        for p in peliculas:
            # Comparar el título buscado con el título de cada película
            if p[0].lower() == titulo_buscado.lower():
                # Si se encuentra, mostrar los detalles de la película
                print(f"Película encontrada: Título: {p[0]}, Año: {p[1]}, Precio: ${p[2]}")
                # Salir de la función después de encontrar la película
                return
        # Si no se encuentra la película, mostrar un mensaje adecuado
    else:
        # Si no se encuentra el título, mostrar un mensaje adecuado
        print("Película no encontrada.")  
        

# FUNCIÓN INCOMPLETA A IMPLEMENTAR
def ordenar_por_anio(peliculas):
    # Ordenar las películas por año usando el método de selección
    # TODO: Ordenar las películas por año usando el método de selección
    print("\n--- Ordenando películas por año de estreno ---")
    # Implementación del método de selección para ordenar por año
    # Recorremos la lista de películas
    n = len(peliculas)
    # Usamos el algoritmo de ordenamiento por selección
    for i in range(n):
        # Suponemos que el primer elemento es el mínimo
        # Inicializamos el índice del elemento mínimo como el índice actual
        min_index = i
        # Recorremos el resto de la lista para encontrar el elemento mínimo
        # Comenzamos desde el siguiente elemento al actual (i + 1)
        for j in range(i + 1, n):
            # Si el año de la película en la posición j es menor que el año del elemento mínimo actual
            # (peliculas[min_index]), actualizamos el índice del mínimo
            # Comparar por año (índice 1)
            # Aquí asumimos que cada película es una sublista con [título, año, precio]
            if peliculas[j][1] < peliculas[min_index][1]:  # Comparar por año (índice 1)
                min_index = j
        # Después de encontrar el índice del elemento mínimo, lo intercambiamos con el elemento en la posición i
        # Esto asegura que el elemento mínimo se coloca en la posición correcta
        # Intercambiar el elemento mínimo encontrado con el primer elemento
        peliculas[i], peliculas[min_index] = peliculas[min_index], peliculas[i]

# FUNCIÓN PARA GUARDAR PELÍCULAS EN UN ARCHIVO
def guardar_peliculas(peliculas, nombre_archivo):
    # Guardar las películas en un archivo de texto
    # Abrir el archivo en modo escritura
    print("\n--- Guardando películas en el archivo ---")
    # Abrimos el archivo en modo escritura y especificamos la codificación UTF-8
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Recorremos la lista de películas y escribimos cada película en una líneaq
        # Cada película es una sublista con [título, año, precio]
        # Usamos el separador "|" para separar los campos
        for p in peliculas:
            linea = f"{p[0]}|{p[1]}|{p[2]}\n"
            archivo.write(linea)
    # Imprimir un mensaje de confirmación
    print("Películas guardadas correctamente.")

# PROGRAMA PRINCIPAL
def menu():
    # Esta función muestra un menú interactivo para el usuario
    print("\n--- Sistema de Gestión de Películas ---")
    # Definimos el nombre del archivo que contiene las películas
    # En este caso, el archivo se llama "peliculas.txt"
    nombre_archivo = "peliculas.txt"
    # Cargar las películas desde el archivo
    # Llamamos a la función cargar_peliculas para cargar las películas desde el archivo
    # Si el archivo no existe o no se puede leer, se manejará la excepción
    peliculas = cargar_peliculas(nombre_archivo)
#    # Si no se cargan películas, mostramos un mensaje de error y salimos
    if not peliculas:
        print("No se pudo cargar el catálogo de películas.")
        return
    print(f"Archivo cargado con éxito. Películas en catálogo: {len(peliculas)}")
    # Iniciar el bucle del menú
    while True:
        # Mostrar el menú de opciones al usuario
        print("\n--- MENÚ ---")
        print("1. Mostrar todas las películas")
        print("2. Buscar película por título")
        print("3. Ordenar películas por año de estreno")
        print("4. Guardar cambios")
        print("5. Salir")
        # Solicitar al usuario que seleccione una opción
        # Usamos input para capturar la opción seleccionada por el usuario
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
#Instrucciones para los estudiantes:
#1.	Completar buscar_pelicula(peliculas):
#	Pedir el título.
#	Crear una lista de títulos.
#	Usar búsqueda secuencial.
#	Si se encuentra, mostrar título, año y precio.
#	Si no, mostrar un mensaje adecuado.
#2.	Completar ordenar_por_anio(peliculas):
#	Implementar el método de selección para ordenar por el año de estreno (índice 1 de cada sublista).

