# Python program to print out all the unique ratings provided by 10 users
# Pretty useles to be honest (like most of the other basic programs)

print("--------------------\nPlease rate your experience\n--------------------")
print("Value    ->  Rating")
print("  1           Bad")
print("  2           Somewhat bad")
print("  3           Average")
print("  4           Somewhat good")
print("  5           Good")

rateSet = set() #create empty set 

rate1 = input("Enter the desired value:")
rateSet.add(rate1)   #Add the values in the empty set 'rateSet'
print("Thank you")

rate2 = input("Enter the desired value:")
rateSet.add(rate2)
print("Thank you")

rate3 = input("Enter the desired value:")
rateSet.add(rate3)
print("Thank you")

rate4 = input("Enter the desired value:")
rateSet.add(rate4)
print("Thank you")

rate5 = input("Enter the desired value:")
rateSet.add(rate5)

print("Thank you")
rate6 = input("Enter the desired value:")
rateSet.add(rate6)
print("Thank you")

rate7 = input("Enter the desired value:")
rateSet.add(rate7)
print("Thank you")

rate8 = input("Enter the desired value:")
rateSet.add(rate8)
print("Thank you")

rate9 = input("Enter the desired value:")
rateSet.add(rate9)
print("Thank you")

rate10 = input("Enter the desired value:")
rateSet.add(rate10)
print("Thank you")

print(rateSet)
