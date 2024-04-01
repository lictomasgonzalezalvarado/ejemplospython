#En Python, el código txt[::-1] se utiliza para revertir una cadena de texto
#Este tipo de notación se le denomina Notación de Rebanado (slicing notation)

# Nomenclatura Operador Terneario
# variable = valor_si_verdadero if condicion else valor_si_falso

#*************** Métodos **************************
def palindromoTXT(txt:str):
    txt=txt.replace(' ','').lower()
    return "La frase si es palíndromo" if txt==txt[::-1] else "La frase No es palíndromo"

def palindromoLISTA(lista):
    reversed_lista = lista[::-1]
    return reversed_lista

def palindromoLISTA2(lista):
    reversed_lista = lista[::-2]
    return reversed_lista

def palindromoMatriz(matriz):
    reversed_matrix = matriz[::-1]
    return  reversed_matrix
#*************** Métodos **************************

#Programa principal
print(palindromoTXT("Le avisara Sara si va el"))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista al revés: {palindromoLISTA(lista)}")
print(f"Otra lista al revés: {palindromoLISTA2(lista)}")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matriz al revés: {palindromoMatriz(matriz)}")
