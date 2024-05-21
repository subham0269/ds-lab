#Write a python program to take input a string. Perform the following operations on that string and show the output:

#a. Check Lower case

input_string = input("Enter a string: ")
if input_string.islower():
    print("The string contains only lowercase characters.")
else:
    print("The string does not contain only lowercase characters.")


#b. Convert into Lower case

input_string = input("Enter a string: ")
lowercase_string = input_string.lower()
print("Lowercase string:", lowercase_string)


#c. Convert into upper case

input_string = input("Enter a string: ")
uppercase_string = input_string.upper()
print("Uppercase string:", uppercase_string)


#d. Display tokenized words.

input_string = input("Enter a string: ")
tokenized_words = input_string.split()
print("Tokenized words:", tokenized_words)


#e. Display distinct words in the paragraph

input_paragraph = input("Enter a paragraph: ")
words = input_paragraph.split()
distinct_words = set(words)
print("Distinct words in the paragraph:")
for word in distinct_words:
    print(word)


#f. Count total number of words

input_paragraph = input("Enter a paragraph: ")
words = input_paragraph.split()
total_words = len(words)
print("Total number of words in the paragraph:", total_words)


#g. Count distinct number of words

input_paragraph = input("Enter a paragraph: ")
words = input_paragraph.split()
distinct_words = set(words)
distinct_word_count = len(distinct_words)
print("Distinct number of words in the paragraph:", distinct_word_count)


#h. Print stopwords

# bash
# Commands for installing stopwords
# pip install nltk
# python -m nltk.downloader stopwords

from nltk.corpus import stopwords
english_stopwords = set(stopwords.words('english'))
print("Stopwords in English:")
print(english_stopwords)


#i. Count the number of stopwords

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
input_paragraph = input("Enter a paragraph: ")
words = input_paragraph.split()
english_stopwords = set(stopwords.words('english'))
stopword_count = 0
for word in words:
    if word.lower() in english_stopwords:
        stopword_count += 1
print("Number of stopwords in the paragraph:", stopword_count)


#j. Display first and last 3 characters of the string in concatenated fashion

input_string = input("Enter a string: ")
first_three = input_string[:3]
last_three = input_string[-3:]
concatenated = first_three + last_three
print("Concatenated string:", concatenated)