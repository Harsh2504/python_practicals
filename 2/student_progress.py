#prog to check student progress
print("enter mark")
n = int(input())
if(n>= 90 ):
	print("progress : exelent")
elif(n>= 80 ):
	print("progress : very good")
elif(n>= 70 ):
	print("progress : good")
elif(n>= 60 ):
	print("progress : average")
else:
	print("progress : poor")
