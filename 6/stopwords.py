import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

str1 = "Namrata a Daphale .DYPCET,Namrata in a Daphale .DYPCET is as Cse the dept High"
words = word_tokenize(str1)
filter = [word for word in words if word.lower() not in stop_words]
print(filter)