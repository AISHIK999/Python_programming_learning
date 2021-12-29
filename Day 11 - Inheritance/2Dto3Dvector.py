# Python program to take a 2D vector and convert it to a 3D vector based on user inputs

class vector2D:
    def __init__(self, i, j):
        self.x = i
        self.y = j

    def __str__(self):
        return f"{self.x}i + {self.y}j"


class vector3D(vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.kcap}k"


xc = input("Enter the x coordinate of the 2D vector:\n")
yc = input("Enter the y coordinate of the 2D vector:\n")
v2d = vector2D(xc, yc)
print(f"The 2D vector is: {v2d}")

zc = input("Enter the z coordinate of the 3D vector:\n")
v3d = vector3D(xc, yc, zc)
print(f"The 3D vetor is: {v3d}")
