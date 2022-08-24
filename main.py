
from fractions import Fraction
from funciones import printMatriz, Matriz, interCambioDeFilas, escalarXfila, operacionEntreFila
from colores import YELLOW,CYAN, MAGENTA, BLUE, GREEN ,WHITE

def main():
    print(GREEN+'='*20+'Cargar Matriz'+'='*20+WHITE);matriz = Matriz(int(input('ingrese la cantidad de filas: ')), int(input('ingrese la cantidad de columnas: ')))
    printMatriz(matriz)
    print(CYAN+'='*60);opciones = int(input('Opcion 1: intercambio de fila\nOpcion 2: fila por un escalar\nOpcion 3: operacion elemental entre filas\nMostrar Matriz\nPresionar 0 para finalizar el programa\n opcion: '));print('='*60+WHITE)
    while opciones != 0:
        printMatriz(matriz)
        if opciones == 1:
            print(YELLOW+'='*20+'Intercambio de Fila'+'='*20+WHITE)
            matriz = interCambioDeFilas(matriz,int(input('Seleccionar una Fila: ')),int(input('seleccionar segunda Fila: ')))
        if opciones == 2:
            print(MAGENTA+'='*20+'Escalar por fila'+'='*20+WHITE)
            matriz = escalarXfila(matriz,int(input('que fila desea modificar: ')),Fraction(input('Escalar con el que desea operar: ')))
        if opciones == 3:
            print(BLUE+'='*20+'Operacion entre fila'+'='*20+WHITE)
            fila2 = int(input('fila a modificar: '))
            fila1 = int(input(f'La fila {fila2} se va sumar con la: '))
            matriz = operacionEntreFila(matriz,fila2,fila1,input(f'escalar que va a multiplicar la fila {fila1}: '))
        if opciones == 4:
            printMatriz(matriz)
        if opciones == 5:
            print(GREEN+'='*20+'Cargar Nueva Matriz'+'='*20+WHITE)
            matriz = Matriz(int(input('ingrese el numero de fila de la nueva matriz')), int(input('ingrese el numero de columna de la nueva matriz: '))) 
        #TODO: ciclo nuevo
        print(CYAN+'='*60);opciones = int(input('realizar otra operacion\nOpcion 1: intercambio de fila\nOpcion 2: fila por un escalar\nOpcion 3: Operacion elemental entre filas\nOpcion 4: Mostar Matriz\n5: Cargar nueva Matriz\nPresionar 0 para finalizar el programa\nOpcion: '));print('='*60+WHITE)
main()