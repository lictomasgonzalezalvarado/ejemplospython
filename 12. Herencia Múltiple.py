class Telefono:
    def __init__(self):
        pass # Todavía no he he implementado un algoritmo para el contructor
    def llamar(self):
        print("Llamando...")
    def ocupado(self):
        print("Ocupado...")
    def colgar(self):
        print("Colgando...")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('Tomando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print('reproduciendo musica...')
    def reproducirvideo(self):
        print('Reproducir un video...')

class Smartphone(Telefono, Camara, Reproduccion):
    def __init__(self):
        print('Objeto movil creado')
    #El método __del__ en Python es un método especial o mágico que se llama automáticamente
    #cuando un objeto está a punto de ser destruido, es decir, justo antes de que la memoria
    #que ocupa el objeto sea liberada por el recolector de basura (garbage collector) de Python.
    #
    # Este método se utiliza para realizar operaciones de limpieza o liberación de recursos
    # asociados con el objeto antes de su eliminación.
    def __del__(self):
        print('Objeto movil destruido')

movil = Smartphone()

#a función dir() en Python se utiliza para obtener una lista de nombres válidos en el espacio
#de nombres local o global de un objeto. En otras palabras, devuelve una lista de los atributos
#y métodos disponibles para un objeto dado
print(dir(movil))

movil.llamar()
movil.colgar()
movil.reproducciondemusica()