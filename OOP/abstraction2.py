class complaint:
    def __init__(self):
        self.name=" "
        self.sku_no=0
        self.complaint=" "

   

#client 1
class client_1(complaint):

    #const
    def __init__(self):
        self.name=" "
        self.complain=" "
        self.sku_no=0

    #method 1
    def comp1(self):
        complaint=input("Enter the client concerns: ",)
        self.complain=complaint
        print("the cleint issues is: ", self.complain)

    #method 2
    def info1(self):
        nclient=input("Enter the client name: ", )
        sku_no=int(input("Enter the SKU_No: ", ))
        self.sku_no=sku_no
        self.name=nclient
        print("Client name: ", self.name)
        print("SKU Number: ", self.sku_no)

    #method 3
    def status(self):
        status=input("isthe issue resolved: ", ).lower()

        #decision
        if(status=='yes'):
            print("The complaint has been resolved")
        else:
            print("The compait needs attention")

#Object
mark=client_1()

#method
print(mark.comp1())
print(mark.info1())
print(mark.status())



    