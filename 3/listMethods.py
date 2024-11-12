print("List Methods\n")

ls = [66,"Namrata",21,89.70]
print("list : ",ls)

print("length of list : ",len(ls))

ls.append("dypcet")
print("list after append : ",ls)

ls.insert(2,"Daphale")
print("list after insert : ",ls)

ls.remove(66)
print("list after remove : ",ls)

ls.pop()
print("list after pop : ",ls)

ls.count(66)
print("list count function : ",ls.count(66))

ls1 = [10,50,10.50,40.60,30,20]
ls1.sort()
print("list after sort : ",ls1)
