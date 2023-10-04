class Employee:
    def __init__(self, emp_id, name, position, salary):
     self.emp_id = emp_id
     self.name = name
     self.position = position
     self.salary = salary

    def __str__(self):
       return f"Employee ID: {self.emp_id}\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}"

class Department:
    def __init__(self, name):
        self.name =name
        self.employees =[]

    def add_employee(self, employee):
       self.employees.append(employee)

    def list_employees(self):
       for employee in self.employees:
          print(employee)

class HRSystem:
    def __init__(self):
     self.departments = {}

    def add_department(self, department):
       self.departments[department.name] = department

    def get_department(self, department_name):
       return self.departments.get(department_name, None)
    
    def list_departments(self):
       for department_name, department in self.departments.items():
          print(f"Department: {department_name}")
          department.list_employees()

# Create employees
employee1 = Employee(101, "James Kigen", "Manager", 600000)
employee2 = Employee(102, "Jane Smith", "Developer",500000)
employee3 = Employee(103, "Jane Doe", "Marketer", 480000)

# Create departments
hr_department = Department("HR")
it_department = Department("IT")

# Add employees to departments
hr_department.add_employee(employee1)
it_department.add_employee(employee2)
it_department.add_employee(employee3)

# Create an HR system
hr_system = HRSystem()
hr_system.add_department(hr_department)
hr_system.add_department(it_department)
# List departments and their employees
hr_system.list_departments()