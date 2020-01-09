#Variables
matriz = []
identica = []

#Funcion llena de ceros una matris
def mat(n):
    for i in range (n):
        matriz.append([])
        identica.append([])
        for j in range (n):
            matriz[i].append(0)
            identica[i].append(0)
    return matriz, identica

def llenar(n):
    matriz = mat(n)
    for x in range (n):
        for y in range (n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))

    
def unidad(n):
    identica = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    return identica

def im(n):
    print("\nMatriz identica:")
    for i in range (n):
            print (identica[i][:])

#Programa
n = int(input ('Tamano de la matriz : '))
llenar(n)
unidad(n)
im(n)