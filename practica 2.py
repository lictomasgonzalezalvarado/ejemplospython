#https://youtu.be/rC7D39VuNyo?si=Qe8etQ5Xs_BCiuZ1
#yacklyion
class Matematicas:
    def suma(self): #Esto es un método
        self.n1 = 2 #esta es una variable que pertenece al paso de parametros del método.
        self.n2 = 3 #esta es una variable que pertenece al paso de parametros del método.

obj = Matematicas() #se instancía un objeto de la clase Matematicas.

obj.suma() #se invoca el método suma.

print(obj.n1 + obj.n2)

