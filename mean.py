li=[]
n=int(input("Enter the number of element"))
for i in range(0,n):
    n=int(input("Enter the element"))
    li.append(n)
sum=0
for i in range(len(li)):
    sum+=li[i]
mean=sum/len(li)
print(mean)
