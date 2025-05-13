'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def read_matrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter the value of element at position ({i}, {j}): "))
            row.append(value)
        matrix.append(row)
    return matrix, rows, cols
def addition_matrix(matrix1, matrix2, rows, cols):
    matrix = []
    for i in range(rows):
        row = []  # Initialize a new row for the result
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])  # Add corresponding elements
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print() 
matrix1, rows, cols = read_matrix()
# Read the second matrix
matrix2, _, _ = read_matrix()  # We can ignore the dimensions for the second matrix
# Print the first matrix
print("Matrix 1:")
print_matrix(matrix1)
# Print the second matrix
print("Matrix 2:")
print_matrix(matrix2)
# Add the two matrices
add = addition_matrix(matrix1, matrix2, rows, cols)
# Print the result of the addition
print("Addition of Matrix 1 and Matrix 2:")
print_matrix(add)
