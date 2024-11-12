import pandas as pd

data = {
  "name": ["Namrata", "Harsh", "Siddhi"],
  "rollno": [66, 76, 55]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 