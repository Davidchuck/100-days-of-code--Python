#codelab for nested ifs#
#example 1

weather="Rainy"
status=1
color="grey"
ocass="official"
comfort=1

if(weather=="Rainy"):
    if(color=="blue"):
        print("Wear the cloth")
    elif(status==1):
        print("Wear the cloth because its clean")
    else:
        print("Wear anything clean!")
else:
    if(color=="grey"):
        print("check the weather condition")
    elif(comfort==1):
        print("You can wear it")
    else:
        print("Look for something else to wear")
        

#Second Example
#Tea or coffee Decision

coffee=1
tea=1
sugar=1
milk=1
time="afternoon"
#Nested if
if(time=="morning"):
    if(tea==1):
        if(sugar==1):
            if(milk==1):
                print("You can have tea")
            else:
                print("you can have black coffee")
        else:
            print("Go buy sugar")
    else:
        print("you drink some hot water")
else:
    if(coffee==1):
        if(sugar==1):
            if(milk==1):
                print("you can have some mocha")
            else:
                print("You can have nescafe 3 in 1")
        else:
            print("Include them in your next shopping")

            
#Example 3
#University selection

distance=1 #1=near, 0=Far
cluster=30
convinience=1 #1=convinient, 0= inconvinient
upkeep=0 #1=expensive, 0=affordable
cost=1 #1=affrodable, 0=Expensive

#Nested ifs
if(cluster>=35):
    if(convinience==1):
        if(upkeep<1):
            if(cost==1):
                print("Select the university")
            else:
                print("Look for another school")
        else:
            print("Look for an affordable school")
    else:
        print("Decide on whether to study only or work only")
else:
    if(convinience==1):
        if(upkeep==0):
            print("You can do that course")
        else:
            print("Choose anoother course")
    else:
        print("you can choose another university")
