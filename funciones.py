from fractions import Fraction
from colores import RED, WHITE

def PrintMatriz(matriz:list):
    nuevaMatriz = []
    for i in range(len(matriz)):
        nuevaMatriz.append([])
        for j in matriz[i]:
            nuevaMatriz[i].append(str(j))
    for i in nuevaMatriz:
        print(i)
def Matriz(n:int,m:int):
    vector = []
    for i in range(n):
        vector.append([])
        for j in range(m):
            vector[i].append(Fraction(input(f'Ingrese un numero para la fila {i+1} columna {j+1}: ')))
    return vector
def verificarFila(matriz:list,fila:int):
    if len(matriz) > fila and fila >= 0:
        return True
    else:
        return False
def interCambioDeFilas(matriz:list,filaA:int,filaB:int):
    if verificarFila(matriz,filaA) and verificarFila(matriz,filaB):
        matriz[filaA], matriz[filaB] = matriz[filaB],matriz[filaA]
    else:
        print(RED+'No se puede, ya que no encontro una de las filas'+WHITE)
    return matriz
def escalarXfila(matriz:list,fila:int,escalar:str):
    if verificarFila(matriz, fila):
        for i in range(len(matriz[fila])):
            matriz[fila][i] *= escalar
    else:
        print(RED+f'No se encontro la fila {fila}'+WHITE)
    return matriz
def operacionEntreFila(matriz, filaB,filaA,escalar):
    if verificarFila(matriz, filaA) and verificarFila(matriz, filaB):
        for i in range(len(matriz[filaA])):
            matriz[filaB][i] += matriz[filaA][i] * escalar
    else:
        print(RED+'No se puede, ya que no encontro una de las filas'+WHITE)
    return matriz