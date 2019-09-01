import math
import operator
from collections import OrderedDict #mantiene el orden en que se fueron agregando al diccionario
def mas_repetido(matriz):
    diccionario = OrderedDict()
    for valor1 in matriz:
        for valor2 in valor1:
            if valor2 in diccionario:
                diccionario[valor2] +=  1
            else:
                diccionario[valor2] = 0
    return max(diccionario.iteritems(), key=operator.itemgetter(1))[0]

def condensa(cadena):
    pass

def triangulo_pascal(niveles):
    if niveles < 0:
        raise Exception('No hay triangulos con numeros negativos')
    if niveles == 0:
        return [[1]]
    else:
        lista=[]
        numero = 0
        for numero in range(0,niveles+1):
            lista.append(int(math.factorial(niveles)/(math.factorial(numero)*(math.factorial(niveles-numero)))))
        return triangulo_pascal(niveles-1)+[lista]

def subcadenas(cadena):
    pass
