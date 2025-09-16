li=[]
n=int(input("Enter the number of element: "))
for _ in range(0,n):
    ele=int(input("Enter the element"))
    li.append(ele)
for i in range(1,len(li)):
    if li[i]%5==0:
        li[i],li[i-1]=li[i-1],li[i]

print(li)
