# Python program to duplicate and rename a text file
# The entire program has been separated into separate blocks of code

import os   #Import python library function

#-------------------------------------------------------------------------------------------------

# Code that copies the contents of a document into another document

# Creates the initial document
f = open("sample.txt", "w")
f.write(str(input("Create the document:\n")))
f.close()

# Reads the initial document
f = open("sample.txt")
content = f.read()      #Stores the data inside the intital text file into the variable 'content'
f.close()


f = open("copy.txt", "w")
f.write(content)    # Writes the data stored in the variable 'content' into the file 'copy.txt,
f.close

#-------------------------------------------------------------------------------------------------

# Code that checks whether the file is successfully copied

file1 = "sample.txt"
file2 = "copy.txt"

with open("sample.txt") as f:
    content1 = f.read()

with open("copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Successfully duplicated!\n\n")

#-------------------------------------------------------------------------------------------------

# Code that renames the copied document from 'copy.txt'

newName = str(input("Enter the name of the duplicated file:\n"))
with open("copy.txt") as f:
    inside = f.read()   #The variable 'inside' in this case is just the same as 'content'. I chose different name for better explanation

with open(f"{newName}.txt", "w") as f:
    f.write(inside)

os.remove("sample.txt")     #Removes the specified file using library function
os.remove("copy.txt")
