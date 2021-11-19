# Python program to print out half of a pyraming using * pattern

dep = int(input("Enter the depth of the pyramind:\n"))

if(dep<=0):
    print("Enter a positive number:\n")
else:
    for a in range(dep):
        print("*" * (a+1))
