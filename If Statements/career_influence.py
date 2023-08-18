#Declare what would influence a career
print("This activity is meant to help you decide which is the best coarse for you.\nFor each question enter Y, to mean yes or N, to mean No")
print("Would you go for lots of theory relates course?")
influence_1=input()

print("You love lots of practical lesson")
influence_2=input()

print("You love to practically solves modern problems")
influence_3=input()
#print("Would you go for lots of theory relates course?")
#influence_2=input("It's technology related")
#influence_3=input("Practically solves modern problems")

if(influence_1=="Y" or influence_1=="y"):
    print("Tech is not for you")
else:
    print("You are a practical person")

if(influence_2=="Y" or influence_2=="y" and influence_1=="N" or influence_1=="n"):
        print("You can try a tech or Engineering course")

if(influence_1=="Y" or influence_1=="y" and influence_2=="Y" and influence_2=="y"):
     print("You cannot love too much theory and be practical")

if(influence_1=="N" or influence_1=="n" and influence_2=="y" or influence_2=="Y" and influence_3=="y" or influence_3=="Y"):
      print("You should definitely persue a tech related coarse")
else:
       print("Please Try Other careers from tech")
   
#if(influence_1=="Has lots of theory" and influence_2=="It's technology related"):
       # print("This is not for me either")

#if(influence_2=="It's technology related" and influence_3=="Practically solves modern problems"):
      #  print("Nice, this is definitely for me")

