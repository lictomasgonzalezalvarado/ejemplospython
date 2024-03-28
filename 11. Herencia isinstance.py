class Calculadora:
    def __init__(self, numero, i): #constructor con 2 pasos de parámetros
        self.n = numero #atributo n
        self.datos =[0 for i in range(numero)] #declaración de un arreglo en python

    def ingresardato(self):
        self.datos = [int(input('ingresar datos ' + str(i+1) + ' = ')) for i in range(self.n)] #Ingresar n valores al arreglo desde teclado

class OperacionesBasicas (Calculadora): #clase derivada OperacionesBAsicas obtiene herencia de la clase base Calculadora
    def __init__(self):
        Calculadora.__init__(self,2,0) #se indica que se usará el constructor padre y se limitará el arreglo a 2 valores.

    def suma(self): #función suma
        a,b = self.datos #se la asignan los valores del arreglo, a las variables a y b
        s = a + b
        # print('La suma es: ', s)
        return s

    def resta(self):
        a,b = self.datos #se la asignan los valores del arreglo, a las variables a y b
        r = a - b
        # print('La resta es: ', r)
        return r

class Raiz (Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1,0) #Se invoca el constructor de la clase base para ingresar solo un valor al arreglo

    def cuadrada(self):
        import math
        a, = self.datos
        raiz = math.sqrt(a)
        # print('La raiz cuadrada es: ', raiz
        return raiz

objeto= OperacionesBasicas()

# isinstance se utiliza para verificar si un objeto es una instancia de una clase dada o si pertenece a una clase específica
print(isinstance(objeto, OperacionesBasicas)) #devuelve true porque objeto es una instancia de OperacionesBasicas
print(isinstance(objeto, Raiz)) #devuelve false porque objeto NO es una instancia de Raiz

# se utiliza para verificar si una clase es una subclase de otra clase dada
print(issubclass(Raiz, OperacionesBasicas)) #devuelve false porque la clase Raiz NO obtiene herencia de la clase OperacionesBasicas
print(issubclass(OperacionesBasicas, Calculadora)) #devuelve true porque OperacionesBasicas SI obtiene herencia de la clase Calculadora