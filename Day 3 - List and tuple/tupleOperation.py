# Python program to perform operations on a tuple

a = input("Enter the first number: \n")
b = input("Enter the second number: \n")
c = input("Enter the third number: \n")
d = input("Enter the fourth number: \n")
e = input("Enter the fifth number: \n")
f = input("Enter the sixth number: \n")

newTup = (a, b, c, d, e, f)

print(newTup)

print("Counting the number of occurences in the tuple\n")
elem = input("Enter the value of the element you wish to search the occurence of:\n")
newCount = newTup.count(elem)
print("Occurences of the entered element is: :")
print(newCount)

print("Showing the index of an element\n")
newElem = input("Enter the value of the element you wish to see the index of:\n")
newInd = newTup.index(newElem)
print("The element is present at index: ")
print(newInd)
