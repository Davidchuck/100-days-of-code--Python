#This is a try exception handling code
#It will demonstrate the use of the try statements 
#Works in error handling
'''var_a=34
var_b="Kin"

#Try() block starts here
try:
    calc=var_a+var_b
    print(calc)
except:
    print("An error has occured")

#Second demonstration
#Perimeter, Area and Volume of a rectangle shape

length=14
height=13
width=8

#Try() Block to calculate the area
try:
    per=2*(length+width)
    area=length*width
    vol=length*width*height

    #print findings
    print(per)
    print(area)
    print(vol)

except:
    print("An operation error occured")

    #Error handling demo 3
    #Control structure'''

situation="Home Alone"

try:
    if(situation=="Home Alone"):
        dec_1=print("Go out and wear nice shoes")
        dec_2=print("Stay home and wear flip flops")
        final=dec_1 or dec_2
        print(final)

    else
        print("you are stuck at work")
except:
    print("An error occured")


