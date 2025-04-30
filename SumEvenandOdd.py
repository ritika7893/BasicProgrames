
def sumofList(li):
    sumeven=0
    sumodd=0
    for i in li:
       if(i%2==0):
           sumeven=sumeven+i
       else:
           sumodd=sumodd+i
           
    return sumeven, sumodd
n=int(input("enter the number"))
li=[]
for i in range(0,n):
    li.append(int(input(f"Enter element {i+1}: ")))
even_sum, odd_sum = sumofList(li)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
