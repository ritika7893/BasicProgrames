#Reverse A String
def reverse_str(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev

s=input("Enter the String")
result=reverse_str(s)
if(result!=s):
    print("Not a palindrome")
else:
    print("Palindrome")
print(result)
