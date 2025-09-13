li=[]
dict={}
n=int(input("Enter the number of element: "))
for i in range(n):
    element=input("Enter the element: ")
    li.append(element)
for i in li:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict.keys())
print(dict)
