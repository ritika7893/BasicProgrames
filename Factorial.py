def factorial(n):
    
    if n==0 or n==1:
        return 1
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
   
    return fact
n=int(input("enter the number"))
fact=factorial(n)
print(fact)
