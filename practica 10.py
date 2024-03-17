class Heore:

    def __init__(self,nombre, nivel, clase):
        self.nombre= nombre
        self.nivel = nivel
        self.clase = clase

    def __str__(self):
        return (f"{self.nombre}" +
                f" es un {self.clase} de nivel {self.nivel}")

gandalf = Heore("Gandalf",99,"Mago blanco")
print(gandalf)

descripcion = str(gandalf)
print(f"Descripcion: {descripcion}")