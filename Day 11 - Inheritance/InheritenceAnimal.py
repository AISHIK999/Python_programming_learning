# Python program to inherit a class 'dogs', which is inherited from a class 'Pets', again inherited from a class 'Mammal'

class Animals:
    type = "Mammal"


class Pets:
    legs = "4"


class Dogs:
    @staticmethod
    def age():
        print("The age is: 5")


animal = Dogs()
animal.age()
