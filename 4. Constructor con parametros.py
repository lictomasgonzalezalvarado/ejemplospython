#https://youtu.be/rC7D39VuNyo?si=Qe8etQ5Xs_BCiuZ1
#yacklyion
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

obj = Calculadora(5,8)

print(obj.suma)
print(obj.resta)
print(obj.producto)
print(obj.division)