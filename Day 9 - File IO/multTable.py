# Python program to print out the multiplication table of numbers in a text file inside specified directory

from os import write

a = int(input("Enter the limiting number of the table:\n"))
b = int(input("Enter the range of the table:\n"))

for i in range(1, (a+1)):
    f = open(f"tables/Multiplication_table_of_{str(i)}.txt", 'w')
    for j in range(1, (b+1)):
        f.write(f"{i} X {j} = {i*j}\n")

print("The tables have been saved inside the 'tables' directory")