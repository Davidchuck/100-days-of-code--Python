#Nested while loop
#case study 1, Turning on a particular appliance in the house
#variables to use: socket_var, Electricity, presence, time, mood
socket=0 #0=off , 1=on
electricity=0 #0=not available , 1=available
presence=0 #0=present , 1=not available
Time=0 # Goal of 3 hours
mood="happy" # for if block
bulb_switch=1
#process
presence=presence+1
electricity=electricity+1
socket=socket+1
#Nested while
while(presence==1):
    while(electricity==1):
        while(socket==1):
            if(mood=="happy"):
              Time=Time+3
              print("you can watch television or Listen to music for:", Time)
            else:
                print("Relax and go to sleep")
            break

        else:
            if(socket!=1):
                print("Turn on the socket")
            else:
                print("You can use your phone to stream")
        break
    else:
        if(electricity!=1 and bulb_switch==1):
            print("Relax, read a book as kplc do their thing")
    break
else:
    if(presence!=1):
        print("Get home first")


              
            
