#using parent classes and no super class

#case 1: shopping centre/suppermarket

#base class 1
class supermarket:
    #constructor
    def __init__(self, grocery, detergent, bakery):
        self.grocery=grocery
        self.detergent=detergent
        self.bakery=bakery

        #method 1
    def getglocery(self):
        groc=input("Enter yout glocery of choice: ",)
        self.grocery=groc
        return self.grocery
        
        #method 2
    def getdetergent(self):
        deter=input("Enter your detergents of choice: ",)
        self.detergent=deter
        return self.detergent
        
        #method 3
    def getbakery(self):
        bake=input("Enter the confectionary of choice: ", )
        self.bakery=bake
        return self.bakery
        
#Base class 2
class shop:
    #constructor
    def __init__(self, Toiletry, crockery):
        self.Toiletry = Toiletry
        self.crockery = crockery

    #method 1
    def gettoiltry(self):
        toil= input ("enter your toiletry essentials: ", )
        self.Toiletry=toil
        crock=input("Enter crockery of choice; ", )
        self.crockery=crock
        return (self.Toiletry + self.crockery)

#Multiple inheritance
#derivedd class
class shopping(supermarket, shop):
    #due to the different constructors both constructors are initialized here
    #A new constructor is created from voth parent classes
    def __init__(self):
        supermarket.__init__(self, '','','')
        shop.__init__(self, '', '')
    
    #Method
    def getlist(self):
        print(self.grocery)
        print(self.detergent)
        print(self.bakery)
        print(self.Toiletry)
        print(self.crockery)

#create objects
shopping=shopping()

#calling the methods
print(shopping.getbakery())
print(shopping.getdetergent())
print(shopping.getglocery())
print(shopping.gettoiltry())
print (shopping.getlist())
        