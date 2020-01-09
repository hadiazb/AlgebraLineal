# A basic code for matrix input from user 
  
R = int(input("Ingrese el numero de filas: ")) 
C = int(input("Ingrese el numero de columnas: ")) 
  
# Initialize matrix 
matrix = [] 
print("Ingrese matris por pantalla  ") 
print() 
# For user input 
for i in range(R):          # A for loop for row entries 
    a = [] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input("Elemento [%d,%d] ---> "%(i,j))))
    matrix.append(a) 
print() 
print("-------Matris-------") 
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print("   ",matrix[i][j], end = "  ") 
    print() 