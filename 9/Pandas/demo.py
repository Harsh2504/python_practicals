import pandas as pd

mydata = {
  'name': ["Vishval", "Shamal", "Namrata"],
  'rollno': [64, 62, 66]
}

myvar = pd.DataFrame(mydata)

print(myvar)