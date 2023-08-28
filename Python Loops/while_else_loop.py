''''
shower=1
work=1
laziness=1
interview=1
no_of_showers=3

while(shower == 1 and no_of_showers > 2):
    
    if(work == 1 and laziness == 1):
        if(interview == 1):
            print("Go take a shower!")
        else:
            print("You can decide not to take a shower")
    else:
        print("Shower and Stay in the house")
else:
    if(laziness == 1 and interview == 1):
        if(shower == 1):
            print("Go take a shower.")
        else:
            print("Stay untidy")
    else:
        print("Become a couch potato")
no_of_showers = no_of_showers + 1
'''
withdrawal_amt=500
bal=3000
location="Nairobi"
deposit=2500

while(bal<= 1000 and location == "Nairobi"):
    if(bal < 1000):
      bal = bal + deposit
      print(bal)
      
    elif(bal>1000):
      bal=bal- withdrawal_amt
      print(bal)
      print("You have withdrawn.")
else:
   print(" You can withdraw after depositing")