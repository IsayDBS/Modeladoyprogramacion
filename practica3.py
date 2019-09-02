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
    return max(diccionario.iteritems(), key=operator.itemgetter(1))[0] #python2.7
    #este funciona para python 3.7
    #return max(stat.items(), key=operator.itemgetter(1))[0]

def condensa(cadena):
    lista = []
    for i in range(len(cadena)):
        if len(lista) == 0 or lista[-1][0] != cadena[i]:
            lista += [[cadena[i], 1]]
        else:
            lista[-1][1] += 1
    return lista

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
        return subcadenas_aux(cadena, len(cadena)-1) + [[cadena]]

def subcadenas_aux(cadena, longitud):
    if longitud == 0:
        return [[""]]
    lista = []
    for i in range(len(cadena) - (longitud -1)):
        n = i + longitud
        lista.append(cadena[i:n])
    return subcadenas_aux(cadena,longitud-1) + [lista]
