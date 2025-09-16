tup1=(1,2,3,4)
tup2=(3,4,5,35,45)
tup1, tup2 = tup2, tup1

print("tup1:", tup1)
print("tup2:", tup2)
print(tup1 < tup2)   # True
print(tup1 > tup2)   # False
print(tup1 == tup2) 
