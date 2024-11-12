from nltk.stem import PorterStemmer 
ps = PorterStemmer()

words = ["running", "runner", "ran", "runs"]
stemmed = [ps.stem(word) for word in words]
print(stemmed)
