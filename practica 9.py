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


basicas = OperacionesBasicas()
raizcuadrada= Raiz()

print('Operacions básicas')
basicas.ingresardato()
print("La suma es ",basicas.suma())
print("La resta es ",basicas.resta())

print('\nRaiz Cuadrada')
raizcuadrada.ingresardato()
print("La raiz cuadrada es ",raizcuadrada.cuadrada())