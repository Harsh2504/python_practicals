import re
# def rmNum(str):
#     res = re.sub(r'\d+','',str)
#     return res

# input = "Namrata is 21 years old"
# result = rmNum(input)

# print("New str:",result)

str = "Namrata is good girl 22 Namrata"
result = re.findall("[a-d]",str)
print(result)

result = re.findall("\d",str)
print(result)

result = re.findall("N..r",str)
print(result)

result = re.findall("^Good",str)
# print(result)
if result:
    print("Yes starts with Good")
else:
    print("not starts with Good")


result = re.findall("Namrata$",str)
# print(result)
if result:
    print("Yes ends with Namrata")
else:
    print("not ends with Namrata")