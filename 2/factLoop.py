num = int(input("Enter a number for factorial:"))
 
fact = 1
i = 1
while i <= num:
    fact = fact*i
    i = i+1
print("factorial: ",fact)