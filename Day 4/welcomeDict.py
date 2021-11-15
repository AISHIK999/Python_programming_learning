# Python program to print a greeting message based on the username of the user based on python dictionary

welcomeDict = {}    # Creates an empty dictionary

name1 = input("Enter your real name:\n")
user1 = input("Enter your username:\n")

welcomeDict.update({name1 : user1})     # Updates the dictionary

name2 = input("Enter your real name:\n")
user2 = input("Enter your username:\n")

welcomeDict.update({name2 : user2})

name3 = input("Enter your real name:\n")
user3 = input("Enter your username:\n")

welcomeDict.update({name3 : user3})

name4 = input("Enter your real name:\n")
user4 = input("Enter your username:\n")

welcomeDict.update({name4 : user4})

name5 = input("Enter your real name:\n")
user5 = input("Enter your username:\n")

welcomeDict.update({name5 : user5})

keyword = input("Enter your name:\n")
print("Hello there! " + welcomeDict.get(keyword))
