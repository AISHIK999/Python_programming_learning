# Python program to return the date to the user alongwith name

from datetime import date   # Import date class from datetime module
now = date.today()  # Assign today's date to the variable 'now'

name = input("Enter your name: ")

print("Hello", name, ". Today is", now)

