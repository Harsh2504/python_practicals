value = input("Enter a value to check if it is pallindrome or not ?     ")

bool = True
i = 0
j = len(value)-1
while i <= j:
    if value[i] != value[j]:
        bool = False
    i = i+1
    j = j-1
if bool == True:
    print("Palindrome")
else:
    print("Not a palindrome")