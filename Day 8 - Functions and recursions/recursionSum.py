# Python program to print the sum of n natural numbers

def natSum(n):
   if n <= 1:
       return n
   else:
       return n + natSum(n-1)

n = int(input("Enter the limit of the sum:\n"))
print("The sum of all natural numbers upto " + str(n) + " is: " + str(natSum(n)))
