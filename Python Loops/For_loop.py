#for else loop
#For() executes first then else() block
#case study 1

food=[0,0,0] # Food present
exhausted=3 # If exhausted to level 3, noo cooking
guest=5 #This is part of else block

#For loop

for i in food:
    exhausted=exhausted+1
    if(exhausted >3):
        print("You can Buy food")
    else:
        print("Go in the kitchen and cook")
else:
    if(guest>=5):
        print("Go Buy some food")

    else:
        print("Cook for the guests")