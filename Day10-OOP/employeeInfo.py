# Python program to store information about employees in an organization

org = str(input("Enter the name of the organization:\n"))

# Create a class for each employee

class Employee:
    compamy = org

    # create functions under the employee class
    def name(self):
        pass
    def employeeCode(self):
        pass
    def salary(self):
        pass
    def printInfo(self):
        print(f"\n\n\nName of the employee is {self.name}\nEmployee code is:{self.employeeCode}\nSalary is: INR {self.salary}")

choice = 1

while choice == 1:
    i = 1
    employee = Employee()
    employee.name = str(input("Enter the name of the employee:\n"))
    employee.employeeCode = str(0000+i)
    i=i+1
    employee.salary = str(input("Enter the salary of the employee in INR:\n"))
    employee.printInfo()
    choice = int(input("\n\n\n\nDo you wish to add another entry?\nIf YES, enter: 1 otherwise enter 0\nDEAFULT IS 1\nYour choice:\n"))

    