# A python dictionary to store some hindi words and returns the user their english meaning

# Creating the dictionary
hindiDict = {
    "namaste" : "hello",
    "mera" : "my / mine",
    "naam" : "name",
    "hai" : "is",
    "paani" : "water",
    "hawa" : "air",
    # Like this we continue to add new 'elements : correspondingValues' in the dictionary
}

print("Welcom to the Hindi to English dictionary\nEnter the hindi word you wish to find the meaning of")
searchWord = input("Your word:\n")

print("The english meaning of " + searchWord + " is:")
print(hindiDict.get(searchWord))    #we get the search word from the dictionary and print it 
