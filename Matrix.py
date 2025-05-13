matrix=[]
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of col:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        value = int(input(f"Enter the value of element at position ({i}, {j}): "))
        row.append(value)
    matrix.append(row)
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=' ')
    print()
