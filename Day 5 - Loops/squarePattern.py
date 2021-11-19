# Python program to print a square pattern with * 

len = int(input("Enter the depth of the pyramid:\n"))

if(len<=0):
    print("Enter a positive number:\n")
else:
    line = 1
    while(line <= len):
        if(line == 1 or line == len):
            print("*" * len)
        else:
            print("*" + " " * (len-2) + "*")
        line = line +1
