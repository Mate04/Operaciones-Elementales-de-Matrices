from colorama import Cursor, init, Fore
from fractions import Fraction
from funciones import Matriz, interCambioDeFilas, escalarXfila, operacionEntreFila
from colores import YELLOW,CYAN, MAGENTA, BLUE, GREEN,RED ,WHITE
from prettytable import PrettyTable

def PrintTable(matriz):
    #!: Implementar Tablas
    Table = PrettyTable()
    Table.header = False
    Table.add_rows(matriz)
    print(Table)

def main():
    print(GREEN+'='*20+'Cargar Matriz'+'='*20+WHITE);matriz = Matriz(int(input('ingrese la cantidad de filas: ')), int(input('ingrese la cantidad de columnas: ')))
    PrintTable(matriz)
    print(CYAN+'='*60);opciones = int(input('Opcion 1: intercambio de fila\nOpcion 2: fila por un escalar\nOpcion 3: operacion elemental entre filas\nOpcion 4: Mostrar Matriz\nPresionar 0 para finalizar el programa\n opcion: '));print('='*60+WHITE)
    while opciones != 0:
        PrintTable(matriz)
        if opciones == 1:
            print(YELLOW+'='*20+'Intercambio de Fila'+'='*20+WHITE)
            fila1 = int(input('Seleccione una Fila para intercambiar: '))-1
            fila2 = int(input('seleccionar segunda Fila para intercambiar: '))-1
            matriz = interCambioDeFilas(matriz,fila1,fila2)
            print()
            PrintTable(matriz)
            print(Cursor.UP(1)+Cursor.FORWARD(len(matriz[0])*10)+MAGENTA+f'E↓ {fila1+1} {fila2+1}'+WHITE)
            print()
        if opciones == 2:
            print(MAGENTA+'='*20+'Escalar por fila'+'='*20+WHITE)
            fila = int(input('que fila desea modificar: '))-1
            escalar = Fraction(input('Escalar con el que desea operar: '))
            matriz = escalarXfila(matriz,fila,escalar)
            print()
            PrintTable(matriz)
            print(Cursor.UP(1)+Cursor.FORWARD(len(matriz[0])*10)+MAGENTA+f'E↓ {fila+1} ({escalar})'+WHITE)
            print()
        if opciones == 3:
            print(BLUE+'='*20+'Operacion entre fila'+'='*20+WHITE)
            fila2 = int(input('fila a modificar: '))-1
            fila1 = int(input(f'La fila {fila2+1} se va sumar con la: '))-1
            escalar = Fraction(input(f'escalar que va a multiplicar la fila {fila1+1}: '))
            matriz = operacionEntreFila(matriz,fila2,fila1,escalar)
            print()
            PrintTable(matriz)
            print(Cursor.UP(1)+Cursor.FORWARD(len(matriz[0])*10)+MAGENTA+f'E↓ {fila2+1} {fila1+1} ({escalar})'+WHITE)
            print()
        if opciones == 4:
            print(CYAN+'='*20+f'Matriz {len(matriz)}x{len(matriz[0])}'+'='*20+WHITE)
            input(f'\n{RED}presione enter para continuar{WHITE}')
        if opciones == 5:
            print(GREEN+'='*20+'Cargar Nueva Matriz'+'='*20+WHITE)
            matriz = Matriz(int(input('ingrese el numero de fila de la nueva matriz: ')), int(input('ingrese el numero de columna de la nueva matriz: '))) 
        #TODO: ciclo nuevo
        print(CYAN+'='*60);opciones = int(input('realizar otra operacion\nOpcion 1: intercambio de fila\nOpcion 2: fila por un escalar\nOpcion 3: Operacion elemental entre filas\nOpcion 4: Mostar Matriz\nOpcion 5: Cargar nueva Matriz\nPresionar 0 para finalizar el programa\nOpcion: '));print('='*60+WHITE)
main()