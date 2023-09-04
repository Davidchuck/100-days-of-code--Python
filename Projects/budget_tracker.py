# variables
#expenses, income, goals, logic, 
#saving rules, 
#30,30,30,10
#50,30,20
#Zero based

#We need:
#output
#Decision
#Goal

#Inputs
#income variables
salary=int(input("Enter your salary: "))
sidehustle=int(input("Enter your monthly side hustle income: "))

#Expenses
utilitybills=int(input("Monthly utility bills: "))
glocery=int(input("Glocery spendings: "))
rent=int(input("How much is your rent: "))
allowances=int(input("Enter other expense: "))

#Goals
goal1="Improve setup"
goal2="Go on a vacation"
goal3="Start business"
goal4="Education bills"

mygoal=goal1

#Logics
if(mygoal==goal1):
    newincome=salary+sidehustle

    if(newincome>=40000):
       # expenses=utilitybills+glocery+rent+allowances
        #savings=balance=newincome-expenses
        expense_net=newincome*50/100
        allowance_net=newincome*30/100
        savings_net=newincome*20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newincome>=50000):
        expense_net=newincome*30/100
        allowance_net=newincome*30/100
        savings_net=newincome*30/100
        leisure_net=newincome*10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry your incme category is not listed")

elif(mygoal==goal2):
    newincome=salary+sidehustle

    if(newincome>=40000):
       # expenses=utilitybills+glocery+rent+allowances
        #savings=balance=newincome-expenses
        expense_net=newincome*50/100
        allowance_net=newincome*30/100
        savings_net=newincome*20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newincome>=50000):
        expense_net=newincome*30/100
        allowance_net=newincome*30/100
        savings_net=newincome*30/100
        leisure_net=newincome*10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry your incme category is not listed")


        

        
        

    
