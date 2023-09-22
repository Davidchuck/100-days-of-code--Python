#performing class operations
#use constractors in the class
#demonstrate the use of classes, objects, methods and constructors

#case study one: person in a company

class person:
#constructor self represents the object
    def __init__(self, name, age, id, gender): #initailization of the constror self
        self.name = name #attribute
        self.age=age
        self.id=id
        self.gender=gender

    #method to get the name
    def getName(self):
       # return "My Name is "+str(self.name)
        return self.name
    
    #method to calculate the age
    def getAge(self):
        new_age=self.age+2
       # return str("my Age is"+new_age)
        return new_age
    
    #method to return gender
    def getGender (self):
        #return ("I am" + self.gender )
        return self.gender
    
    #method to retun id
    def getId(self):
        return self.id
    
#create an object
new_person=person("David", 30, 232323, "Male")
#calling the object methods
print(new_person.getAge())
print (new_person.getName())
print(new_person)

#case 2
class cars:
    #Constructor
    def __init__(self, model, color):
        self.model=model
        self.color=color
        
    #method 1
    def getModel(self):
        return self.model
    #method 2
    def getColor(self):
        return self.color

#create object methods
car1=cars("Toyota", "Black")
car_2=cars("Audi", "White")
car_3=cars("Ford", "Jungle Green")

#calling the methods
#print("\nCar Model : ", car1.getModel(), "\t Car Color:", car1.getColor() )
print(car1.getModel())
print(car_2.getColor())


#Case study 3
class Fruits:
    #constructor defining
    def __init__ (self , shape, color, sugar_level, price):
        self.shape=shape
        self.color=color
        self.sugar_level=sugar_level
        self.price=price
    #Method 1
    def getShape(self):
        return self.shape
    #method 2
    def getSugarLevel(self):
        self.sugar_level=0
        new_level=self.sugar_level+(234/40)
        return new_level
    
    #method 3
    def setPrice(self):
        self.price=0
        no_of_pieces=14
        cost=15
        total_price=no_of_pieces*cost
        return total_price
    
    #method 4
    def getColor(self):
        return self.color
    
#creat object
fruit=Fruits("crecent", "yellow", 0,0)
fruit_2=Fruits("circle", "Orange",0,0)
fruit_3=Fruits("Oval","green", 0,0)

#Calling the methods
#print ("\nThe Shape of fruit is : ", fruit.getShape(),"\nSugar Level in percentage : ", fruit.getSugarLevel)
print(fruit_2.getSugarLevel())
print(fruit_2.getColor())
print(fruit_2.getShape())
print(fruit_2.setPrice())


