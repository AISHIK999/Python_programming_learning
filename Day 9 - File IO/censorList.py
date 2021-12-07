# Python program to censor out a list of words from a document

f = open("censor.txt", "w")
f.write(str(input("Create the document:\n")))
f.close()

# Creates empty an empty list
censorWords=[]

# Adds words as string into the created empty list
choice = 1
i = 0
while choice == 1:
    word = str(input("Enter the word you wish to censor:\n"))
    censorWords.append(word)
    print(f"[sucessfully added {word} to the list\n")
    i += 1
    choice = int(input("Do you wish to add another word to the list?\nIf YES, enter '1'\nYour choice:\n"))

f = open("censor.txt", "r")
content = f.read()
f.close()

# Scans each string inside the list and replaced the string from the text file
for j in range(0, i):
    f = open("censor.txt", "w")
    if censorWords[j] in content:
        content = content.replace(censorWords[j], "[REDACTED]")     # Replaces the word stored in the variable 'search' from the document with '[REDACTED]'
        f.write(content)

f.close()
