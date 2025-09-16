class_and_teacher={}
n=int(input("Enter the no of classes"))
i=0
while i<n:
    classes=int(input("enter the classes: "))
    class_teacher=input("Enter class teacher name: ")
    class_and_teacher[classes]=class_teacher
    i+=1
for i in class_and_teacher:
    print(i,class_and_teacher[i])
