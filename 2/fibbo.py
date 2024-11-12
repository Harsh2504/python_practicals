num = int(input("Enter a number upto which you want fobonacci series:"))

i = 0
j = 1
print(i)
print(j)
while i <= num:
    c = i + j 
    print(c)
    i = j
    j = c
    num = num-1
