

import abc
# Python program to find the sum of 'n' natural number 

num = int(input("Enter the limit of the natural number upto which you want to find the sum of:\n"))
if(num<0):
    print(f"{num} is not a natural number\n")
else:
    a=0
    sum = 0
    while(a<=num):
        sum += a
        a = a+1

    print(f"The sum of all natural numbers upto {num} is: {sum}")
