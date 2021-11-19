# Program to check whether a number is prime or not

num = int(input("Enter the number:\n"))

if(num<0):
    print("A negative number cannot be a prime number.\n")
else:
    for a in (2, ((num/2)+1)):
        if(num % a) == 0:
            print("The number is not prime number\n")
            break   # Stops the loop if the number is not prime
    else:
        print("The number is a prime number.\n")
