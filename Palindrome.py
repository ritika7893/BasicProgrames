def palin(n):
    temp=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if rev==temp:
        return True
    return False
n=int(input("enter the number"))
pal=palin(n)
if pal==True:
    print("palindrome")

else:
    print("Not palindrome")
