print("String Methods\n")

str1 = "Namrata Daphale"

print("length of string : ",len(str1))

print("slicing : ",str1[0:5])

print("lower case : ",str1.lower())

print("upper case : ",str1.upper())

print("strip : ",str1.strip())

print("replace function : ",str1.replace("S","M"))

print("split function : ",str1.split())

print("capitalize function :",str1.capitalize())

print("casefold function :",str1.casefold())

print("count function a : ",str1.count("a"))

print("encode function :",str1.encode())

print("expand function :",str1.expandtabs(5))

print("formatmap function :",str1.format_map(7))

print("index function :",str1.index("a"))

print("isaplha function : ",str1.isalpha())

print("isascii function : ",str1.isascii())

print("isdecimal function : ",str1.isdecimal())

print("isdigit function : ",str1.isdigit())

print("isidentifier function : ",str1.isidentifier())

print("isnumeric function : ",str1.isnumeric())

print("isprintable function : ",str1.isprintable())

print("isspace function : ",str1.isspace())

print("istitle function : ",str1.istitle())

str1 = str1.upper()

print("islower function : ",str1.islower())

print("isuppper upper : ",str1.isupper())

print("join function : ",str1.join("student"))

str2 = "good"
str3 = str1+str2
print("concatination of string : ",str3)

print("ljust function : ",str1.ljust(100))

print("lstrip function : ",str1.lstrip())

print("maketrans function : ",str1.maketrans("a","i"))

print("partition function : ",str1.partition("a"))

print("rfind function : ",str1.rfind("a"))

print("rindex function : ",str1.rindex(" "))

print("rjust function : ",str1.rjust(100))

print("rpartition function : ",str1.rpartition("a"))

name = """Namrata"""

print("tripal quotes : ",name)

print("multiple string : ",name*2)