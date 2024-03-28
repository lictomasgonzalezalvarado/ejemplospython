#https://youtu.be/rC7D39VuNyo?si=Qe8etQ5Xs_BCiuZ1
#yacklyion
#https://youtu.be/L10koAOz5SA?si=VXwaxAG6-_NWTtCE
#Jhon Ortiz Ordoñez

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

    def saly_hi(name: str|None=None):
        if name is not None:
            print(f"¡Hola {name}!")
        else:
            print("Hola mundo")

obj = Calculadora(5,8)

print(obj.suma)
print(obj.resta)
print(obj.producto)
print(obj.division)

obj.saly_hi()