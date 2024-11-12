import numpy as np

arr=np.array([1,2,3,4,5])
arr2=np.array([[11,22,33],[44,55,66]])
arr3=np.array([[[10,20,30],[40,50,60],[70,80,90]]])
print(arr)
print(arr2)
print(arr3)

#slicing
print("Slicing")
print(arr[1:3])
print(arr2[0:2:3])
print(arr3[:,:2,:2])