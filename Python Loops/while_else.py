#While loop with a break for repetition
#Case of fruits shopping
#Bananas=300, oranges=400
shopping_budget=1500
bananas=0
oranges=0

#decreasing while loop
while(shopping_budget>=900):
    shopping_budget=shopping_budget-300
    print("The amount remaining is", shopping_budget)
    bananas=bananas+20
    print("the bananas i have bought are", bananas)
else:
    print("The oranges i have bought are" , oranges)