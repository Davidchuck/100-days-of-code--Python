#App user class
class User:
    def __init__(self):
        self.username = " "
        self.email = " "
        self.user_type = " "

    #get username
    def getUsername(self):
        self.username=input("Enter username: ")
        return self.username
    #get email address
    def getUserEmail(self):
        self.email=input("Enter your Email Address: ")
        return self.email
    #set user type
    def getUserType(self):
        self.user_type=input("Select user type, single or Married: ")
        return self.user_type
    
#House details
class House:
    def __init__ (self):
        self.available=" "
        self.location=" "
        self.size=" "
        self.water=""
        self.rent=0

    #Check if house is available fore renting
    def checkAvailability(self):
        self.available=int(input("Is the house vaccant enter 1 for yes and 0 for not"))
        if self.available==0:
            print ("Sorry the house is not currently available for rental")
        elif self.available==1:
            print("The house is currently available for Rent.")           
        else:
            print ("You entered an invalid response")
        return self.available

    #get house location
    def setLocation(self):
        self.location=input("Please Enter The Location of the house: ")
        return self.location
    #Get size of house in sqm
    def setSize(self):
        self.size=float(input('How big would you like to make it?'))
        return self.size
    #check water availability
    def checkWaterAvailabilty(self):
        self.water=bool(int(input("Does this property have a functioning water source? Enter 1 for Yes and 0 for No")))
        return self.water
    #Rent Details
    def getRent(self):
        self.rent=float(input("How much is the rent?"))
        return self.rent

#Decision Maker
class activity(User, House):
    def __init__(self):
        User.__init__(self)
        House.__init__(self)

    #Method 1
    def Tenant_details(self):
        print(self.username)
        print(self.user_type)
        print(self.email)

    #method 2
    def house_status(self):
        print(self.available)
        print(self.location)
        print(self.size)
        print(self.water)
        print(self.rent)


action1=activity()
#call the methods
print("\n\tWelcome To My Application!\n")
action1.getUsername()
action1.getUserEmail()
action1.getUserType()
print("\n\t Welcome You have entered the following personal details\n")
action1.Tenant_details()

print("\n\tBelow is a list of houses available for rent\n")
action1.checkAvailability()
action1.checkWaterAvailabilty()
action1.setLocation()
action1.setSize()
action1.getRent()

#action1.house_status()




  