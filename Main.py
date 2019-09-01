from practica3 import *
def seleccionador (argument):
    if argument == 1:
        entrada = input("Introduce una matriz de la forma [[1,2],[2,3]]\n")
        print(mas_repetido(entrada))
    elif argument == 2:
        entrada = input("Introduce una cadena\n")
        print(condensa(entrada))
    elif argument == 3:
        entrada = input("Introduce el numero del nivel que quieres ver del triangulo de pascal\n")
        print(triangulo_pascal(entrada))
    elif argument == 4:
        entrada = input("Introduce una cadena\n")
        print(subcadenas(entrada))
    elif argument == 0:
        pass
    else:
        print("No es un opcion")

def pedirNumeroEntero():
    correcto= False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce un numero entero: "))
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
