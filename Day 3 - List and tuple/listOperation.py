# Python program to make operations on a list with values

a = input("Enter the first number: \n")
b = input("Enter the second number: \n")
c = input("Enter the third number: \n")
d = input("Enter the fourth number: \n")
e = input("Enter the fifth number: \n")
f = input("Enter the sixth number: \n")

numList = [a, b, c, d, e, f]

print("Sorting elements:\n")
numList.sort()

print("The sorted list:\n " )
print(numList)

print("Reverse sorting elements:\n")
numList.reverse()

print("The reverse sorted list: \n")
print(numList)

print("Append a ne4w element at the end:\n")
n = input("Enter the element you wish to append:\n")
numList.append(n)

print("The new list: \n")
print(numList)

print("Insert new element at an index:\n")
newNum = int(input("Enter the value of the element you wish to insert:\n"))
numPos = int(input("Enter the index where you wish to insert the new element:\n"))
numList.insert(numPos, newNum)

print("The sorted list: ")
print(numList)
