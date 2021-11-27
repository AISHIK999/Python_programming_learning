# Python program to remove a word from a string and strip it
# Stripping means to remove excess blank spaces

def strAndStrp(string, word):
    newString = string.replace(word, " ")
    return newString.strip()    # .strip() removes the excess spaces

string = input("Enter your string/sentence:\n")
word = input("Enter the word(s) you wish to remove from the input string\n[For multiple words, separate each by a single space\nYour answer:\n")

newString = strAndStrp(string, word)
print("The new string is: " + newString)
