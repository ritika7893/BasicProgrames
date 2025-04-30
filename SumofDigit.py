def sum_of_digit(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the number"))
sum=sum_of_digit(n)
print("sum",sum)
