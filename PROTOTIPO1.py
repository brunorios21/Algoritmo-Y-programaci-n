# ---------------------------
# FUNCIONES PRINCIPALES
# ---------------------------
#Se crea un sistema de inventario para una librería, que permite leer un archivo de texto con datos de libros, ordenado por precio, buscar libros por titulo, filtrar por autor y guardar los resultados ordenados en un nuevo archivo.
#toma como parametro el nombre del archivo que contiene los datos de los libros, lee el contenido del archivo y devuelve una lista de diccionarios, cada uno representando un libro con su código, titulo, autor y precio.
def leer_inventario(nombre_archivo):
    #Creamos una lista vacía para almacenar los libros
    libros = []
    try:
        #Abrimos el archivo en modo lectura
        #y especificamos la codificación UTF-8 para manejar caracteres especiales
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo: #Recorremos cada linea del archivo
                datos = linea.strip().split(",") # Eliminamos espacios en blanco y separamos los datos por comas
                if len(datos) == 4: #Si  la longitud de datos es 4, significa que tenemos todos los campos necesarios 
                    #Creamos un diccionario para representar el libro
                    #con sus respectivos campos: código, título, autor y precio
                    libro = {
                        "codigo": datos[0], #El codigo del libro es el primer  elemento [0]
                        "titulo": datos[1], #El titulo del libro es el segundo elemento [1]
                        "autor": datos[2], #El autor del libro es el tercer elemento [2]
                        "precio": float(datos[3]) #Convertimos el precio a tipo float para manejarlo como número [3]
                    }
                    libros.append(libro) #Añadimos el libro a la lista de libros
    #Manejamos la excepción si el archivo no se encuentra
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    return libros

#Creamos una función que ordena los libros por precio de forma descendente.
def ordenar_por_precio_desc(libros): #Toma el parámetro libros, que es una lista de diccionarios representando los libros.
    # Ordenamiento por selección (descendente)
    for i in range(len(libros)-1): # Se recorre hasta el penúltimo  elemento de la lista -1 quiere decir que no se incluye el último elemento en el bucle
        # Se asume que el primer elemento es el máximo
        max_index = i # Se guarda el índice del máximo encontrado 
        for j in range(i+1, len(libros)): #Se recorrre desde el siguiente elemento actual (i+1) hasta rl final de la lista
            #si se encuentra un elemento mayor al máximo actual, se actualiza el índice del máximo
            if libros[j]['precio'] > libros[max_index]['precio']: #si el precio del libro en la posicion j es mayor que el precio del libro en la posicion max_index
                max_index = j #Actualizamos max_index al índice j
        libros[i], libros[max_index] = libros[max_index], libros[i] # Intercambiamos los libros en las posiciones i y max_index
        # Al finalizar el bucle, la lista estará ordenada de mayor a menor precio
    return libros

#Creamos una función que busca un libro por su título.
#Toma como parámetros la lista de libros y el título a buscar.
def buscar_por_titulo(libros, titulo_buscado):
    for libro in libros:#recorremos la lista de libros
        #Comparamos el título del libro actual con el título buscado, ignorando mayúsculas y minúsculas 
        if libro['titulo'].lower() == titulo_buscado.lower():
            return libro #Si encontramos el libro, lo devolvemos
    #Si no se encuentra el libro, devolvemos None
    return None

#Creamos una función que filtra los libros por autor.
#Toma como parámetros la lista de libros y el autor a buscar.
def filtrar_por_autor(libros, autor_buscado):
    resultado = [] #Creamos una lista vacía para almacenar los libros filtrados
    #Recorremos la lista de libros
    for libro in libros:
        if autor_buscado.lower() in libro['autor'].lower(): #Si el autor esta buscando en el autor del libro 
            resultado.append(libro) #Añadimos el libro a la lista de resultados
    #Devolvemos la lista de libros filtrados
    return resultado

#Creamos una función que guarda los libros ordenados en un nuevo archivo.
#Toma como parámetros la lista de libros ordenados y el nombre del archivo donde se guardarán.
def guardar_ordenados(libros_ordenados, nombre_archivo):
    #Abrimos el archivo en modo escritura
    #y especificamos la codificación UTF-8 para manejar caracteres especiales
    with open(nombre_archivo, "w", encoding="utf-8") as archivo: 
        for libro in libros_ordenados: # Recorremos la lista de libros ordenados
            # Creamos una línea de texto con los datos del libro, separados por comas
            linea = f"{libro['codigo']},{libro['titulo']},{libro['autor']},{libro['precio']}\n"
            archivo.write(linea) # Escribimos la línea en el archivo

# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
## Creamos una función que muestra el menú principal del sistema de inventario.
def menu():
    print("\n--- Sistema de Inventario Letras y Libros ---")
## Definimos el nombre del archivo que contiene los datos de los libros

    nombre_archivo = "inventario.txt"
    # Llamamos a la función leer_inventario para cargar los libros desde el archivo
    libros = leer_inventario(nombre_archivo)
#    # Si no se pudieron cargar libros, mostramos un mensaje de error y salimos
    if not libros: 
        print("No se pudo cargar el inventario.")
        # Si la lista de libros está vacía, significa que no se pudieron cargar los datos
        return

    print(f"\nArchivo cargado con éxito. Libros en inventario: {len(libros)}")
#    # Llamamos a la función ordenar_por_precio_desc para ordenar los libros por precio de forma descendente
    libros_ordenados = ordenar_por_precio_desc(libros.copy()) # Esto crea una copia de la lista original libros
    
    '''
       Es importante porque si pasáramos directamente libros a la función ordenar_por_precio_desc, la función
       modificaría el orden del inventario original.
       Con .copy(), evitamos eso: se trabaja con una copia, dejando intacta la lista libros.
    '''
#    # Mostramos la lista de libros ordenados por precio
    print("\nLista ordenada por precio (mayor a menor):")
    for libro in libros_ordenados: # Recorremos la lista de libros ordenados
        # Imprimimos el título y el precio de cada libro, formateando el precio con dos decimales
        print(f"{libro['titulo']} - ${libro['precio']:,.2f}")
#    # Pedimos al usuario que ingrese un título para buscar
    titulo = input("\nIngrese un título para buscar: ")
    # Llamamos a la función buscar_por_titulo para buscar el libro por su título
    resultado = buscar_por_titulo(libros, titulo)
    # Si se encuentra el libro, mostramos sus detalles; de lo contrario, mostramos un mensaje de no encontrado
    if resultado:
        print(f"\nLibro encontrado: {resultado['titulo']} - {resultado['autor']} - ${resultado['precio']}")
    else:
        print("Libro no encontrado.")
    # Pedimos al usuario que ingrese un autor para filtrar los libros
    autor = input("\nIngrese un autor para filtrar: ")
    # Llamamos a la función filtrar_por_autor para obtener los libros del autor especificado
    libros_filtrados = filtrar_por_autor(libros, autor)
    if libros_filtrados: # Si se encontraron libros del autor, los mostramos
        # Mostramos los títulos y precios de los libros filtrados
        print("\nLibros encontrados:")
        for libro in libros_filtrados:
            print(f"- {libro['titulo']} - ${libro['precio']}")
    else:
        print("No se encontraron libros de ese autor.")
    # Llamamos a la función guardar_ordenados para guardar los libros ordenados en un nuevo archivo
    guardar_ordenados(libros_ordenados, "ordenados.txt")
    print("\nLibros ordenados guardados en 'ordenados.txt'.")

# Ejecutar el programa
menu()