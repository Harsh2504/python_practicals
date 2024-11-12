import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lem =  WordNetLemmatizer()
words = ["running", "runner", "ran", "runs"]
lemmatized = [lem.lemmatize(word, pos='v') for word in words]
print(lemmatized)  