class Employee:

    employeeNum = 0

    def __init__(self, name,email, salary,roles):
        self.name = name
        self.email = email
        self.salary = salary
        self.roles = roles
        Employee.employeeNum += 1

    def displayCount(self):
       print("Number of emplyees: " % Employee.employeeNum)

    def displayEmployee(self):
        print("Name = ",self.name, "Email:", self.email, " Salary:", self.salary, "Roles:", self.roles)


firstEmployee = Employee("Bryan musyoki","musyokibr@gmail.com",2000, "developer")
firstEmployee.displayEmployee()

secondEMployee = Employee("John Cena","cenajohn@gmail.com",3000, "janitor")
secondEMployee.displayEmployee()


class Manager(Employee):
    def __init__(self, name, email, salary, department):
        super.__init__(name=name, email=email, salary=salary, roles="manager")

thirdEMployee = Employee("John Cena","cenajohn@gmail.com",3000, "Manager")
thirdEMployee.displayEmployee()

print("Total Employee %d" % Employee.employeeNum)