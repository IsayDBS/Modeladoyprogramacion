from practica3 import *
def seleccionador (argument):
    if argument == 1:
        while True:
            try:
                entrada = input('Introduce una matriz de la forma [[1,2],[2,3]]\n')
                print(mas_repetido(entrada))
                break
            except:
                print('Error, se debe ingresar una matriz bidimensional\n')
    elif argument == 2:
        while True:
            try:
                entrada = input('Introduce una cadena\n')
                print(condensa(str(entrada)))
                break
            except:
                print('Error, Las cadenas deben estar entre comillas\n')
    elif argument == 3:
        entrada = -1
        correcto= False
        while not correcto:
            try:
                entrada = int(input('Introduce un numero entero mayor o igual a cero\n'))
                if entrada >= 0:
                    print(triangulo_pascal(entrada))
                    correcto = True
            except:
                print('Error, se debe ingresar un numero mayor o igual a cero')
        #print(triangulo_pascal(entrada))
    elif argument == 4:
        while True:
            try:
                entrada = input('Introduce una cadena\n')
                print(subcadenas(str(entrada)))
                break
            except:
                print('Error, Las cadenas deben estar entre comillas\n')
    elif argument == 0:
        pass
    else:
        print('No es una opcion')

def pedirNumeroEntero():
    correcto= False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce un numero entero del menu: "))
            correcto = True
        except:
            print('Error, introduce un numero entero\n')
    return num


def main():
    print('Por favor, introduce el valor numerico que desees:\n1.mas_repetido(matriz)\n2.condensa(cadena)\n3.triangulo_pascal(niveles)\n4.subcadenas(cadena)\nIntroduce 0 para salir del programa')
    seleccionado = -1
    while seleccionado != 0:
        seleccionado = pedirNumeroEntero()
        seleccionador(seleccionado)
    print("Adios")

if __name__ == '__main__':
    main()
