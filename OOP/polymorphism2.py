#Second example of polymorphism
#Animal example

#Origin class
class animal:
    #constructor
    def __init__(self):
        self.movement=" "
        self.sound=" "
        self.name=" "
#form 1
class cat(animal): #class cat inheriting from animal
    #method:name
    def name_cat(self):
        name=input("Enter the cat name: ", )
        self.name=name
        return self.name
    
#form 2: Dog
class dog (animal):
    def getName_2(self):
        name_2=input("Enter the dog name: ",)
        self.name=name_2
        return self.name
    
#Form 3: Parot
class parrot(animal):
    def get_name_3(self):
        name_3 = input ("Enter the parrot's name:",)
        self.name=name_3
        return self.name
    
#object creation
cat=cat()
dog=dog()
parrot=parrot()

#call method
print(cat.name_cat())
print(dog.getName_2())
print(parrot.get_name_3())