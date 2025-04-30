def sumofList(li):
    sum=0
    for i in li:
       
            sum=sum+i
    return sum
n=int(input("enter the number"))
li=[]
for i in range(0,n):
    li.append(int(input(f"Enter element {i+1}: ")))
sum=sumofList(li)
print(sum)
