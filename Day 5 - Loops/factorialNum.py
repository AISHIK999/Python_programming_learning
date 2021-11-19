# Python program to find the factorial of a number

num = int(input("Enter the number:\n"))

mult = (num-1)
init = num
if(num<0):
    print("Enter a positive number:\n")
else:
    while(mult>0):
        num = num * mult
        mult = mult -1
    print(f"The factorial of {init} is: {num}\n")