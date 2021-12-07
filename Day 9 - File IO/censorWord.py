# Python program to censor a specific word from a document

f = open("sample.txt", "w")
f.write(str(input("Create the document:\n")))
f.close()

search = str(input("Enter the word you wish to censor:\n"))

f = open("sample.txt", "r")
content = f.read()
f.close()

f = open("sample.txt", "w")
if search in content:
    content = content.replace(search, "[REDACTED]")     # Replaces the word stored in the variable 'search' from the document with '[REDACTED]'
    f.write(content)

f.close()
