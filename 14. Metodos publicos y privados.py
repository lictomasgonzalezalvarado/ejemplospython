#n Python, no existen modificadores de acceso explícitos como en algunos otros lenguajes
# de programación como Java. En lugar de eso, Python utiliza convenciones para indicar la
# accesibilidad de los miembros de una clase.

#Público: Por convención, los miembros que no comienzan con un guion bajo (_) se consideran
# públicos y pueden ser accesibles desde cualquier parte del programa.

class MiClase1:
    def metodo_publico(self):
        print("Este es un método público")

# Protegido: Aunque no hay una forma directa de hacer un miembro protegido en Python como en
# otros lenguajes (por ejemplo, Java), por convención, los miembros que comienzan con un solo
# guion bajo (_) se consideran protegidos. Esto significa que no se espera que se acceda desde
# fuera de la clase, pero aún se puede acceder.
class MiClase2:
    def _metodo_protegido(self):
        print("Este es un método protegido")

#Privado: De manera similar, los miembros que comienzan con doble guion bajo (__) se consideran
# privados por convención. Estos miembros no deberían ser accesibles ni siquiera desde clases heredadas.
class MiClase3:
    def __metodo_privado(self):
        print("Este es un método privado")

objeto1 = MiClase1()
objeto1.metodo_publico()  # Acceso público

objeto2 = MiClase2()
objeto2._metodo_protegido()  # Aunque es accesible, se considera protegido por convención

objeto3 = MiClase3()
# objeto3.__metodo_privado()