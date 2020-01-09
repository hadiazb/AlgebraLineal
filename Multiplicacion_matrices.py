matrizA = []
matrizB = []
matrizC = []

filasA = int(input("Ingresa las filas de A: "))
columnasA = int(input("Ingresa las columnas de A: "))

filasB = int(input("Ingresa las filas de B: "))
columnasB = int(input("Ingresa las columnas de B: "))

if columnasA != filasB:
	print("No existe solucion")

else:
	print("Ingrese matris A  por pantalla  ") 
	print() 
	for i in range(filasA):          
    	 a = [] 
    	 for j in range(columnasA):
    		 a.append(int(input("Elemento de A [%d,%d] ---> "%(i,j))))
    	 matrizA.append(a)
	print() 
	print("Ingrese matris B  por pantalla  ") 
	print() 
	for i in range(filasB):          
    	 b = [] 
    	 for j in range(columnasB):
    		 b.append(int(input("Elemento de B [%d,%d] ---> "%(i,j))))
    	 matrizB.append(b)
	print() 

	for i in range(filasA):          
    	 c = [] 
    	 for j in range(columnasB):
    		 c.append(int(0))
    	 matrizC.append(c)
	print() 
	for i in range(filasA):
    	 for j in range(columnasB):
    		 for k in range(columnasA):
    			 matrizC[i][j] = int((matrizA[i][k]*matrizB[k][j])+matrizC[i][j])
	print("------Matris Mult-------") 
	print() 
	for i in range(filasA): 
    	 for j in range(columnasB): 
        	print("   ",matrizC[i][j], end = "  ") 
    	 print() 
