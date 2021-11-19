# Python program to search names from a list using initials

nameList = []

ans = "y"
while(ans == "y" or ans == "Y"):
    nameList.append(input("Enter the name:\n"))
    ans = input("Enter 'y' if you want to add another name:")

search = input("Enter the first letter of the name you wish to search:\n")

for name in nameList:
    if name.startswith(search):     # The startswith() function collects the strings starting with a specific character
        print("Name found: " + name)
