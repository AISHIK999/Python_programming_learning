# Python program to add and multiply complexNumber numbers

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return ComplexNumber(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return ComplexNumber(mulReal, mulImg)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"


xa = input("Enter the real part of the first complex number:\n")
ya = input("Enter the imaginary part of the first complex number:\n")
xb = input("Enter the real part of the second complex number:\n")
yb = input("Enter the imaginary part of the second complex number:\n")

c1 = ComplexNumber(xa, ya)
c2 = ComplexNumber(xb, yb)

print(f"The sum of the two complex numbers are: {c1 + c2}")
print(f"The product of the two complex numbers are: {c1 + c2}")
