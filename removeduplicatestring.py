s=input("Enter the String: ")
res=""
unique=set()
for ch in s:
    if ch not in unique:
        unique.add(ch)
        res+=ch
print(res)
    
