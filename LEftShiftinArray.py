li=[]
n=int(input("Enter the number of element: "))
for _ in range(0,n):
    ele=int(input("Enter the element"))
    li.append(ele)
if li:
    s=li.pop(0)
    li.append(s)
print(li)
