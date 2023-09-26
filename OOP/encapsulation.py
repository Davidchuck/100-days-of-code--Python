#Encapsulation == Data hinding
#We will define public and private members in code
#Python uses symbols instead of word representation of private or public
#private = _ (single underscope) 0r __ (double underscore) after the declared variable

#First example: Pricing case study
'''class price:
    def __init__ (self):
        self._price1=400

    #method 1
    def sellprice(self):
        sellprice=self._price1 * (120/100)
        print("The selling price is: ", sellprice)
    
   #method 2
    def getprofit(self):
        profit=sellprice-self._price1
        print("The profit is: ", profit)

#create object
#markedp=price()
#call method
#print(markedp.sellprice())

'''
#Example 2: Derived Class
#Example Salaried Employee
#base class
class person:
    #constructor
    def __init__(self):
        self._name=" "
        self._salary=0
        self._status=" "

    #create method
    def getName(self):
        name=input("Enter your name: ",)
        self._name=name
        print("Employee name is: ", self._name)

    #Method 2
    def getSalary(self):
        sal=int(input("Enter the employee salary: ",))
        self._salary=sal
        print("Salary due: ", self._salary)

    #method 3
    def Status(self):
        stat=input("Enter emp status: ", )
        self._status=stat
        print("Employement status is: ", self._status)

#Derived class
class NewSalary (person):
    #Method to calculate new salary
    def newSalary(self):
        sal_new=self._salary*(115/100)
        print("new salary is: ",sal_new)

#create object
Alice=person()
Alice=NewSalary()

#Call on Method
print(Alice.getSalary())
print(Alice.newSalary())

                



