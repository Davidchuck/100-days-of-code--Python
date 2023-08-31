#case 1: Simple pattern
#Variables
pat=10

#nested for() Incremental pattern
'''for i in range(0, pat):
    for j in range (0, i+1):
        print("*", end="")
    print()'''

#decreamental pattern
'''for i in range(0,pat):
    for j in range(0, i-1):
        print("-", end="")
    print()  '''

#pat = 5 # You can adjust the number of rows as needed

'''for i in range(pat, 0, -1):
       for j in range(i):
           print("*", end="")
       print()'''
#intermediate complex example
#case brushing your teeth everyday

#Variables 
'''week=7 #for()
toothbrush=1 #1 present, 0 not Absent
toothpaste=1 #1 present, 0 not Absent
bakingsoda=5 #To be used 5 times a week for()
mirror=1
water=7 #for()

#Nested for
for i in range(0, week):
    for j in range(water):
        for w in range(bakingsoda):
            if(toothpaste==1):
                if(toothbrush==1):
                    print("You can brush your teeth")
                else:
                    print("Get yourself a toothbrush")
            else:
                print("go buy toothpaste")
        else:
            if(toothpaste==1 and toothbrush==1):
                print("Go and brush your teeth")
                break
'''


#Case study 3: Dish Washing
#Variables water 
period=7 #7 days
day=2 #twice a day
soap=1
washing_brush=1
dish_rack="Empty"
dishes=1
water=14 #14 times

#Nested for()
for i in range(period):
    for d in range(day):
        for w in range (water):
            if(soap==1):
                if(dishes==1):
                    if(washing_brush==1):
                        if(dish_rack=="Empty"):
                            print("Wash the disches and put then on the rack")
                            break
                        else:
                            print("Empty the disch rack first")
                    else:
                        print("Go buy a washing brush")
                else:
                    print("You have no dirty dishes")
            else:
                print("Go buy soap")
    else:
        print("You have completed the number of times to wash dishes in a day")




