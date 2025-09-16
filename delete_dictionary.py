name_and_percentage={}
n=int(input("Enter the no of student: "))
i=0
while i<n:
    name=input("enter the name: ")
    percentage=int(input("Enter the percentage: "))
    name_and_percentage[name]=percentage
    i+=1
for i in name_and_percentage:
    print(i,name_and_percentage[i])
c=input("Enter name to be delted")
del name_and_percentage[c]
print(name_and_percentage)
