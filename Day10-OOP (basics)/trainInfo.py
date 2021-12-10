# Python program to display information about a specific train using OOP
# The information provided is purely imaginary and in no way is meant for real time use

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getInfo(self):
        print(f"{self.name} has {self.seats} and each seat costs INR {self.fare}")

print("Choose your train:\n1. Rajdhani Express\n2. Duronto Express\n3. Intercity Express\n")
choice = int(input("Enter your choice:\n"))

if(choice == 1):
    train = Train("Rajdhani Express", 500, 200)
    train.getInfo()
elif(choice == 2):
    train = Train("Duronto Express", 200, 100)
    train.getInfo()
elif(choice == 3):
    train = Train("Intercity Express", 100, 50)
    train.getInfo()
else:
    print("Incorrect choice")
