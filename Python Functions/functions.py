#syntax
#def():
#statement
#Function caall

#case study 1
#Printing function
'''
def output():
    print("This is my first function")
#output()
v=output()
print(v)

#case 2
#Function to calculate area of a triangle
base=25
height=16
def area():
    a=base*height*0.5
    print(a)
area()'''

#A function that prints 3 statement
statementA="Today is monday"
StatementB="Tomorrow is Tuesday"
statementC="Day after tomorrow is Wednesday"
StatementD="Then here comes Thursday"
def statements():
    a=statementA + StatementB
    b=StatementB + statementC
    c=statementA + statementC
    print(a)
    print(b)
    print(c)
statements()