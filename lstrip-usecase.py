li=[]
n=int(input("Enter the number of element: "))
for i in range(n):
    element=input("Enter the element: ")
    li.append(element)
for i,value in enumerate(li):
    if i%2==1:
        if value.lstrip('-').isdigit():
            li[i] = int(value) * 2
print(li)
