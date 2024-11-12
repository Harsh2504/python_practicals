def addf(num1,num2) :
	sum1 = num1+num2
	print("\naddition : ",sum1)
	
def subf(num1,num2) :
	sub = num1-num2
	print("\nsubtraction : ",sub)
	
def mulf(num1,num2) :
	mul = num1*num2
	print("\nmultiplication : ",mul)
	
def divf(num1,num2) :
	div = num1/num2
	print("\ndivision : ",div)

def modf(num1,num2) :
	mod = num1%num2
	print("\nremainder : ",mod)
		
		
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

a=1 

while(a!=0) :
	print("\n1:addition \n2:subtraction \n3:multiplication \n4:division \n5:remainder \n6:exit")
	ch = int(input("enter your choice : "))
	
	if(ch == 1) :
		addf(num1,num2)
	elif(ch == 2) :
		subf(num1,num2)
	elif(ch == 3) :
		mulf(num1,num2)
	elif(ch == 4) :
		divf(num1,num2)
	elif(ch == 5)  :
		modf(num1,num2)
	else :
		a = 0
