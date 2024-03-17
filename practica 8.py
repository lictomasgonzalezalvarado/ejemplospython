
#https://youtu.be/znsaoO_HqzM?si=E8jX8Og-d_kmt6w9
#jacklyon
#Herencia

class pokemon: #clase base
    pass
    def __init__(self, nombre,tipo): #consructor con dos parametros
        self.nombre = nombre #atributo 1
        self.tipo = tipo #atributo 2

    def descripcion(self): #función con retorno
        return '{} es un pokemon de tipo {}'.format(self.nombre,self.tipo)

class pikachu (pokemon): #Clase derivada que objetiene herencia de la clase pokemon
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoataque)

class charmander (pokemon):
    def habilidad(self,tipohabilidad):
        return '{} tipo de habilidad: {}'.format(self.nombre,tipohabilidad)

mipokemon=pikachu('pikachu','energia');
otropokemon=charmander('charmander', 'agua');

print(mipokemon.descripcion())
print(mipokemon.ataque(" energía eléctrica"))

print(otropokemon.descripcion())
print(otropokemon.habilidad(' es persuasivo'))

