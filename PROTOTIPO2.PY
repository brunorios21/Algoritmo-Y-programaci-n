# FUNCIONES DE BÚSQUEDA (las que el profesor enseñó)
#Creamos una función de busqueda secuencial que toma una lista y un elemento a buscar.
def busquedaSecuencial(lista, item):
    #Posición inicial de búsqueda
    pos = 0
    while pos < len(lista): #Recorremos la lista mientras la posición sea menor que la longitud de la lista
        #Si el elemento en la posición actual es igual al item buscado, retornamos True
        if lista[pos] == item:
            return True 
        #Si no es igual, incrementamos la posición para continuar la búsqueda
        pos = pos + 1
    #Si no se encuentra el elemento, retornamos False   
    return False

# FUNCIONES DEL PROGRAMA
#cargamos los libros desde un archivo de texto
def cargar_libros(nombre_archivo): 
    #Creamos una lista vacía para almacenar los libros
    libros = []
    #Abrimos el archivo en modo lectura y especificamos la codificación UTF-8
    #para manejar caracteres especiales
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo: # Recorremos cada línea del archivo
            # Dividimos la línea en partes usando el separador "|"
            partes = linea.strip().split("|")
            #si la longitud de partes es 2, significa que tenemos un libro con nombre y precio
            #y los agregamos a la lista de libros
            if len(partes) == 2:
                #Obtenemos el nombre y el precio del libro
                nombre = partes[0]
                #Convertimos el precio a entero [1] significa que es el segundo elemento y lo agregamos a la lista libros
                precio = int(partes[1]) 
                #Agregamos el libro como una sublista con nombre y precio
                libros.append([nombre, precio]) 
    #Si el archivo no se encuentra, se maneja la excepción
    return libros
#función para mostrar los libros cargados
def mostrar_libros(libros):
    #Imprimimos el encabezado de la lista de libros
    print("\n--- Lista de Libros ---")
    #Recorremos la lista de libros y mostramos el titulo y el precio de cada libro
    for libro in libros:
        #Cada libro es una sublista con el combre del libro  y su precio
        #libro[0] es el nombre del libro y libro[1] es el precio
        print(f"Título: {libro[0]}, Precio: ${libro[1]}")
    print()
#Función para buscar un libro por su nombre
def buscar_libro(libros):
    #Solicitamos al usuario que ingrese el nombre del libro a buscar
    print("\n--- Búsqueda de Libro ---")
    #nombre_buscado es una variable que almacena el nombre del libro ingresado por el usuario
    nombre_buscado = input("Ingrese el nombre del libro a buscar: ")
    # Creamos una lista vacía para almacenar los nombres de los libros
    # Esta lista se usará para realizar la búsqueda secuencial
    nombres = []                   # Se crea una lista vacía llamada nombres.
    for libro in libros:           # Se recorre la lista libros
         nombres.append(libro[0])  # De cada sublista libro, se toma el primer elemento (libro[0]) y se agrega a nombres.
                
    # esas tres líneas la podemos expresar de esta manera:  nombres = [libro[0] for libro in libros]
    # Llamamos a la función de búsqueda secuencial para verificar si el libro existe
    # en la lista de nombres
    encontrado = busquedaSecuencial(nombres, nombre_buscado)
    #Si el libro fue encontrado, mostramos su información
    if encontrado:
        #Recorremos la lista de libros para encontrar el libro buscado
        print("Libro encontrado:")
        # Recorremos la lista de libros para encontrar el libro buscado
        for libro in libros:
            #Si el nombre del libro coincide con el nombre buscado, lo mostramos
            # libro[0] es el nombre del libro y libro[1] es el precio
            if libro[0] == nombre_buscado:
                # Imprimimos el nombre y el precio del libro encontrado
                print(f"Libro encontrado: {libro[0]} - ${libro[1]}")
    #Si el libro no fue encontrado, mostramos un mensaje
    else:
        print("Libro no encontrado.")
#Función para ordenar los libros por nombre, llamando el parametro libros
def ordenar_libros_por_nombre(libros):
    # Ordenamiento por selección (selection sort)
    print("\n--- Ordenando libros por nombre ---")
    #Recorremos la lista de libros para ordenar por nobre
    # Utilizamos el algoritmo de ordenamiento por selección
    for i in range(len(libros)):
        menor = i# Inicializamos el indice del menor elemento como el indice actual
        #Recorremos el resto de la lista (i+1 hasta la longitud de libros)
        for j in range(i+1, len(libros)):
            #Si el nombre del libro en la posición j es menor que el nombre del libro en la posición menor
            if libros[j][0] < libros[menor][0]:
                #Actualizamos el indice del menor elemento
                menor = j
        #Si encontramos un libro con un nombre menor, lo intercambiamos con el libro en la posición i
        libros[i], libros[menor] = libros[menor], libros[i]
    #Imprimimos los libros ordenados por nombre
    print("Libros ordenados por nombre.")
#Creamos una función para guardar los cambios en el archivo de libros
#Recibe como arumentos la lista de libros y el nombre del archivo
def guardar_libros(libros, nombre_archivo):
    #Abrimos el archivo en modo escritura (w) y especificamos la codificación UTF-8
    #Para manejar caracteres especiales
    # Si el archivo no existe, se creará automáticamente
    # Si el archivo ya existe, se sobrescribirá
    # Esto es útil para guardar los cambios realizados en la lista de libros
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Recorremos la lista de libros y escribimos cada libro en una línea del archivo
        for libro in libros:
            # Formateamos cada libro como una cadena con el nombre y el precio separados por "|"
            # Cada línea tendrá el formato "nombre|precio\n"
            linea = f"{libro[0]}|{libro[1]}\n"
            # Escribimos la línea en el archivo
            archivo.write(linea)#write escribe la linea del arhivo
    # Imprimimos un mensaje indicando que los cambios se han guardado
    print("Cambios guardados en el archivo.")

# PROGRAMA PRINCIPAL
# Esta función muestra un menú interactivo para el usuario
def menu():
    # Cargamos los libros desde el archivo al iniciar el programa
    # Definimos el nombre del archivo que contiene los libros
    ## En este caso, el archivo se llama "libros.txt"
    nombre_archivo = "libros.txt"
    #Cargamos los libros desde el archivo
    libros = cargar_libros(nombre_archivo)
# Si no se cargan libros, mostramos un mensaje
# y terminamos el programa
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar todos los libros")
        print("2. Buscar un libro por nombre")
        print("3. Ordenar libros por nombre (Selección)")
        print("4. Guardar cambios")
        print("5. Salir")
        # Solicitamos al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")
        # Dependiendo de la opción seleccionada, llamamos a la función correspondiente
        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            buscar_libro(libros)
        elif opcion == "3":
            ordenar_libros_por_nombre(libros)
        elif opcion == "4":
            guardar_libros(libros, nombre_archivo)
        elif opcion == "5":
            print("Programa finalizado.")
            # Salimos del bucle y terminamos el programa
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# EJECUCIÓN
menu()