num = int(input("Enter a number upto which you want list of odd numbers:"))

odd = 0
i=0
while i<= num:
    if i%2 != 0:
        print(i) 
        odd = odd+i
    i = i+1
print("Sum of odd's: ",odd)