# Python program to calculate and back calculate increment of salary of an employee using decorators

class Employee:
    salary = 1000
    increment = 20  # 20% increment in salary

    @property
    def salaryAfterIncrement(self):
        return self.salary + ((self.increment/100)*self.salary)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):
        self.increment = ((newSalary - self.salary)/self.salary)*100


e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)
