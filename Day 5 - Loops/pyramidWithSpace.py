# Python program to print a pyramid using * with spaces between each floor

dep = int(input("Enter the depth of the pyramid:\n"))

if(dep<=0):
    print("Enter a positive number:\n")
else:
    for a in range(dep):
        print(" " * (dep-a-1), end="")

        # The end="" after the print function prints the statement 
        # while beginning the next funtion from the same line, i.e 
        # not from the next paragraph

        print("*" * (2*a-1), end="")
        print(" " * (dep-a-1))
