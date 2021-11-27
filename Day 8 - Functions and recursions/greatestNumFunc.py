# Python program to find the greatest number using a function

numList = []
n = int((input("How many numbers you wish to input?\nYour answer:\n")))

for num in range (0, n):
    numList.append(int(input("Enter the element number "+ str(num+1) +":\n")))

for i in range (0, n-1):
    if (numList[i] > numList[i+1]):
        gre = numList[i]
    elif (numList[i] <= numList[i+1]):
        gre = numList[i+1]

print("The greatest of the given numbers is:" + str(gre))
