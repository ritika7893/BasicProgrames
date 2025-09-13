marks=[]
n=int(input("Enter the number of marks of student: "))
for i in range(n):
    mark=int(input("Enter the marks: "))
    marks.append(mark)
total=sum(marks)
percentage=(total/(len(marks)*100))*100
print(f"total:{total} percentage:{percentage}")
    
