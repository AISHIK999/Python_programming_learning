# Python program to calculate the sum and dot product of a vector 

class Vector:
    def __init__(self, vector1):
        self.vector1 = vector1

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vector1:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vector1)):
            newList.append(self.vector1[i] + vec2.vector1[i])
        return Vector(newList)

    def __mul__(self, vector2):
        sum = 0
        for i in range(len(self.vector1)):
            sum += self.vector1[i] * vector2.vector1[i]
        return sum


ax = int(input("Enter the x coordinate of the first vector:\n"))
ay = int(input("Enter the y coordinate of the first vector:\n"))
az = int(input("Enter the z coordinate of the first vector:\n"))
bx = int(input("Enter the x coordinate of the second vector:\n"))
by = int(input("Enter the y coordinate of the second vector:\n"))
bz = int(input("Enter the z coordinate of the second vector:\n"))

x = Vector([ax, ay, az])
y = Vector([bx, by, bz])
print(f"The sum of the two vectors are: {x+y}")
print(f"The dot product of the two vectors are: {x*y}")
