#Shopping list with prices and total expenditure

print("This price list is in ksh.")

print("Please enter the items you wish to buy")

print("Item 1")
item1=input()
print("Quantity")
qty1=int(input())
print("Cost per unit")
price1=int(input())
item1_total=qty1*price1

print("Item 2")
item2=input()
print("Quantity")
qty2=int(input())
print("Cost per unit")
price2=int(input())
item2_total=qty2*price2


print("Item 3")
item3=input()
print("Quantity")
qty3=int(input())
print("Cost per unit")
price3=int(input())
item3_total=qty3*price3

Total_spendings=item2_total + item1_total + item3_total

print("You have entered to buy; %r Kg of %r, %r kg of %r, and %r litres of %r" % (qty1, item1, qty2, item2, qty3, item3))

print("You will therefore spend Ksh.", Total_spendings)


