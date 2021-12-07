# Python program to check if a word is present inside a document

f = open("file.txt", "w")  # Creates/Opens text file
f.write(str(input("Enter the line(s) you want to inculde within the file:\n")))
f.close()

sea = str(input("Enter the word you wish to search within the file:\n"))

f = open("file.txt")
text = f.read()

if sea in text:     # Set what happens when the string stored in 'sea' is present inside the file "text"
    print(f"Yes. The word {sea} is present inside the document.\n")
else:
    print(f"The word {sea} is absent from the document.\n")
f.close()
