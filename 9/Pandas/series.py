import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
myvar1 = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar1)