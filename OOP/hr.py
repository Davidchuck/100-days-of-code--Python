class Employee:
    def __init__(self):
     self.emp_id =" "
     self.name = " "
     self.position =" "
     self.salary =" "

    def get_empid(self):
        emp_id = input("Enter the Employee ID: ", )
        self.emp_id=emp_id
        print("Employee ID is: ", self.emp_id)

    def getName(self):
       name = input("Enter the Employee Full Names: ", )
       self.name=name
       print("Employee name is: ", self.name)

    def getPosition(self):
       position = input("Enter the Employee Position: ", )
       self.position=position
       print("Employee Position is: ", self.position)

    def getSalary(self):
       salary = input("Enter the Employee salary: ", )
       self.salary=salary
       print("Employee salary is: ", self.salary)

    def list_employees(self):
       for employee in self.employees:
          print(employee)

class NewSalary(Employee):
   print(Employee.get_empid)