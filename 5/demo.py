# from math1 import arith ,conversion
from math1.arith import diff
from math1.conversion import *
from nlp_utils import lemmatize  # Add this import

print(diff(1, 2))

number = 42
print(f"Binary: {int_to_binary(number)}")
print(f"Hexadecimal: {int_to_hexadecimal(number)}")
print(f"Octal: {int_to_octal(number)}")

# Add lemmatization example
text = "The quick brown foxes are jumping over the lazy dogs"
lemmatized_text = lemmatize(text)
print(f"Original text: {text}")
print(f"Lemmatized text: {lemmatized_text}")