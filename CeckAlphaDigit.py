def check(ch):
    if ch.isalpha():
        print("Alphabet")
    elif ch.isdigit():
        print("Digit")
    else:
        print("special")
        
ch=input("Enter the Character")
check(ch)
    
