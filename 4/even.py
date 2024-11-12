# func even num from list 

def func(l,n) :
	for j in range(0,n):
		if(l[j]%2 == 0):
			print(l[j])

n = int(input("how many numbers you want in list : "))

l= []

print("enter numbers : ")
for i in range(0,n) :
	num = int(input())
	l.append(num)
	
print("even numbers are : ")
func(l,n)	
