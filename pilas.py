class Pila():
    #Definimos el constructor
    def __init__(self):
        #inicializamos una "pila vacia", el elemento contenedor es del
        #TIpo de dato de lista, donde se irán apilando los elementos.
        self.lista = []
    #metodo apilar, agrega un nuevo elemento a la pila (lista)
    def apilar(self, item):
        self.lista.append(item)
        print(f"elemento {item}apilado, lista actualizada: {self.lista}")
    #metodo de desapilar, quita el ultimo elemento ingresado de la pila (lista)
    def desapilar(self):
        if self.vacia():
            print("No se puede desapilar la vacia")
        else:
            print("elemento {self.lista.pop()}desapilado, lista actualizada: {self.lista}")
    #Metodo que indica el tamaño (largo) de la pila
    def tamanio(self):
        print("la pila tiene {len(self.lista)}elementos")
    #Metodo que controla si la lista esta vacia
    def vacia (self):
        print("La pila tiene {len(self.lista)}elementos")
    #metodo que controla si la lista está  vacia
    def vacia(self):
        if len(self.lista)==0:
            return True
        else:
            return False
    def limpiar(self):
        print("limpiar")
        return self.lista.clear()    
    #creamos (instanciamos) el objeto pila_numeros de la clase Pila
pila_numeros = Pila()
#apilamos (Agregamos)los elementos utilizando el metodo apilar
pila_numeros.apilar(1)
pila_numeros.apilar(2)
pila_numeros.apilar(3)
#Consultamos el tamaño utilizando el metodo tamaño
pila_numeros.tamanio()
#Desapilamos (quitamos) el ultimo elemento agregado de la lista (pila)
pila_numeros.desapilar()
#apilamos (agregamos) los elementos utilizando el metodo apilar
pila_numeros.apilar(4)
#vaciamos (eliminamos) todos los elementos
pila_numeros.limpiar()
#Al querer desapilar el otro elemento de la lista 
#el metodo nos indica que la lista esta vacia
pila_numeros.desapilar()