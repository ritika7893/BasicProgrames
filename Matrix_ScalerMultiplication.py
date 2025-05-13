matrix=[]
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of col:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        value = int(input(f"Enter the value of element at position ({i}, {j}): "))
        row.append(value)
    matrix.append(row)


val=int(input("Enter the value for scaler multiplcation"))   
for i in range(rows):
    for j in range(cols):
       matrix[i][j]=val*matrix[i][j]
  
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=' ')
    print()
