# Python program to find the value of a number raised to a power using OOP

class Calculate:
    def power(self, num, pow):
        return (num ** pow)

    @staticmethod
    def greet():
        print("Hello!")


val = Calculate()
val.greet()
val.int = int(
    input("Enter the integer of which you want to determine the power:\n"))
val.pow = int(input("Enter the power you wish to raise the integer ot:\n"))
ans = val.power(val.int, val.pow)
print(f"The required answer is:\n{ans}")
