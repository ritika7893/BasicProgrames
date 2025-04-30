def fib(n):
   first=0
   second=1
   print(first)
   print(second)
   for i in range(2,n):
        third=first+second
        first=second
        second=third
        print(",",third)
    
n=int(input("enter the number"))
fib(n)
