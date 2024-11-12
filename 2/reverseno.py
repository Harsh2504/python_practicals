num = int(input("Enter a to print reverse of it: "))

rev = 0
rem = 0
while num>0:
    rem = num % 10
    rev = 10*rev + rem
    num = num // 10
print(rev)
