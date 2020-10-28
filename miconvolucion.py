import numpy as np
#------------------------------------------------------------------------------------------------
def convolucion(A,B):
    filas = len(A) - len(B) + 1
    columnas = len(A[0]) - len(B[0]) + 1
    C = np.zeros((filas,columnas))
    for i in range(len(C)):
        for j in range(len(C[0])):
            suma = 0
            for k in range(len(B)):
                for l in range(len(B[0])):
                    suma += A[k + i][l + j]*B[k][l]
            C[i][j] = suma
    return C
#------------------------------------------------------------------------------------------------
matriz1 = np.array([[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]])
kernell1 = np.array([[1,0,2],[5,0,9],[6,2,1]])
matriz2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]])
kernell2 = np.array([[1,1,1],[0,0,0],[2,10,3]])
#------------------------------------------------------------------------------------------------
print("Primer ejemplo: ","\n",convolucion(matriz1,kernell1))
print("Segundo ejemplo: ","\n",convolucion(matriz2,kernell2))



