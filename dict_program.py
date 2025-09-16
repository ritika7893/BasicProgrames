name_and_percentage={}
n=int(input("Enter the no of student: "))
i=0
while i<n:
    name=input("enter the name: ")
    percentage=int(input("Enter the percentage: "))
    section=input("Enter the section")
    rollno=int(input("Enter rollno"))
    li=[name,percentage,section]
    name_and_percentage[rollno]=li
    i+=1
for i in name_and_percentage:
    z=name_and_percentage[i]
    print(i,":")
    for j in z:
        print(j, end=" ")
