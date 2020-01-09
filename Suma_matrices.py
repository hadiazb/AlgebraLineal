# A basic code for matrix input from user 
print("Este programa realiza la suma de dos matrices\n ") 


R = int(input("Ingrese el numero de filas de la matrix A: ")) 
C = int(input("Ingrese el numero de columnas de la matrix A: ")) 
M = int(input("Ingrese el numero de filas de la matrix B: ")) 
N = int(input("Ingrese el numero de columnas de la matrix B: ")) 
  
if R != M or C != N:
	print() 
	print("Las matrices no se pueden sumar")

else:
	matrixA = [] 
	matrixB = []
	matrixC = []
	print("Ingrese matris A  por pantalla  ") 
	print() 
	for i in range(R):          
    	 a = [] 
    	 for j in range(C):
    		 a.append(int(input("Elemento de A [%d,%d] ---> "%(i,j))))
    	 matrixA.append(a)
	print() 
	print("Ingrese matris A  por pantalla  ") 
	print() 
	for i in range(R):          
    	 b = []
    	 for j in range(C):
    		 b.append(int(input("Elemento de B [%d,%d] ---> "%(i,j))))
    	 matrixB.append(b)	 
	print() 
	print("-------Matris A-------") 
	for i in range(R): 
    	 for j in range(C): 
        	print("   ",matrixA[i][j], end = "  ") 
    	 print() 
	print() 
	print("-------Matris B-------") 
	for i in range(R): 
    	 for j in range(C): 
        	print("   ",matrixB[i][j], end = "  ") 
    	 print() 
	print("------Matris Suma-------") 
	print() 
	for i in range(R):   
    	 c = []       
    	 for j in range(C):
    	 	 c.append(matrixA[i][j] + matrixB[i][j])
    	 matrixC.append(c)             
	for i in range(R): 
    	 for j in range(C): 
        	print("   ",matrixC[i][j], end = "  ") 
    	 print() 
    
    




