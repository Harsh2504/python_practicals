num = int(input("Enter a number upto which you want list of even numbers:"))

even = 0
i=0
while i<= num:
    if i%2 == 0:
        print(i)
        even = even+i
    i = i+1
print("Sum of even's: ",even)