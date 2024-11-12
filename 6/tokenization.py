# import nltk
# nltk.download()
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


# word tokenization
str = "Namrata Daphale .DYPCET"
words = word_tokenize(str)
print(words)

sentence = sent_tokenize(str)
print(sentence)

# import nltk 
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = sent_tokenize(sentence_data) 
print (nltk_tokens)

