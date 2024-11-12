addf = lambda num1,num2 : num1+num2
subf = lambda num1,num2 : num1-num2
mulf = lambda num1,num2 : num1*num2
divf = lambda num1,num2 : num1/num2
modf = lambda num1,num2 : num1%num2

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

a=1 

while(a!=0) :
	print("\n1:addition \n2:subtraction \n3:multiplication \n4:division \n5:exit")
	ch = int(input("enter your choice : "))
	
	if(ch == 1) :
		print("addition :",addf(num1,num2))
	elif(ch == 2) :
		print("subtraction :",subf(num1,num2))
	elif(ch == 3) :
		print("multiplication :",mulf(num1,num2))
	elif(ch == 4) :
		print("division :",divf(num1,num2))
	elif(ch == 5)  :
		print("division :",modf(num1,num2))
	else :
		a = 0
