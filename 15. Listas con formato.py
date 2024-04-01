#https://youtu.be/ewKUjEgg6mM?si=qmWcP_S2L46LlijE
#f-string
#format %

class Estudiante:
    def __init__(self, nombre, apellido,edad):
        self.nombre = nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self): #representación informal de una cadena
        return f"hola me llamo {self.nombre} {self.apellido} y tengo {self.edad} años"

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, apellido={self.apellido}, edad={self.edad})"


#Aquí inicia el código de un programa principal
curso = 'python'
edad = 25
nombre = 'Tomás'

print("Tutoriales de %s"%curso) #concatenar variables

print("Hola soy %s y tengo %s años."%(curso,edad))

print('que tal soy {} y mi edad es {} años.'.format(nombre,edad))

print(f"hola soy {nombre}, tengo {edad} años y me gusta programar en {curso}")

print("*****************************************************************************")
obj= Estudiante("Tomas","Gonzalez",43)
print(obj)           # Utiliza __str__()
print(str(obj))      # Utiliza __str__()
print(f"{obj}")      # Utiliza __str__()
print(f"{obj !r}")   # Utiliza __repr__()
print(repr(obj))     # Utiliza __repr__()
