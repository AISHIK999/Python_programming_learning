# Multiplication table of a number using for loop

a= int(input("Enter the number you want to know the multiplication table of: \n"))
n= int(input("Enter the limit of the multiplication table: \n"))

print("The multiplication table is:\n")
for num in range(0, n):
    print(str(a) + "x" + str(num) + "=" + str(a*num))

# You can also use f-string, like this:
#
#print(f"{num} X {a} = {num*a}")
