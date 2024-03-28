class Heore:

    def __init__(self,nombre, nivel, clase):
        self.nombre= nombre
        self.nivel = nivel
        self.clase = clase


#es un método especial que se utiliza para definir
# cómo se debe representar una instancia de una clase
# como una cadena de texto. Este método es llamado
# automáticamente cuando se intenta convertir un objeto
# en una cadena de texto utilizando la función str()
# o cuando el objeto es utilizado en contextos donde
# se espera una representación de cadena, como al
# imprimirlo con la función print().

    def __str__(self):
        return (f"{self.nombre}" +
                f" es un {self.clase} de nivel {self.nivel}")

gandalf = Heore("Gandalf",99,"Mago blanco")
print(gandalf)

descripcion = str(gandalf)
print(f"Descripcion: {descripcion}")