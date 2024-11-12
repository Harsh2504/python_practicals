import array as arr

a = arr.array("i",[1,2,3,4,5])

print("array : ")
for i in range (0,4) :
	print(a[i],)


b=1 

while(b!=0) :
	print("\n1:modify \n2:append \n3:remove \n4:exit")
	ch = int(input("\nenter your choice : "))
	
	if(ch == 1) :
		k = int(input("\nenter index you want to modify : "))
		val = int(input("\nenter value : "))
		a[k] = val
		print("\narray after modify : ",a)
		
	elif(ch == 2) :
		j = int(input("\nenter number you want to append : "))
		a.append(j)
		print("\narray after remove an element : ",a)
		
	elif(ch == 3) :
		i = int(input("\nenter number you want to remove : "))
		a.remove(i)
		print("\narray after remove an element : ",a)
		1
	elif(ch == 4) :
		b = 0
