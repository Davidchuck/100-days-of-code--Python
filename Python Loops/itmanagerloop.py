#Repetitive task for an IT manager: Trainings
#What could lead to training: New staff, change in process, refresher training, too many errors
#variables
print("Are there newly employed staff?, enter 0 for no and 1 for yes")
New_staff=int(input()) #1 represents theres new staff, 0 represents no  new staff

print("Has there been a process change in the system?, enter 0 for no and 1 for yes")
change_process=int(input()) #0 represent no change, 1 represent change

print("How many support requests did you get today?")
support_requests=int(input()) #Max 5 per day

print("How many refresher trainings have you done this year?")
refresher_training=int(input()) #Max 2 per year

for i in range(0,support_requests):
    for j in range(0,refresher_training):
        if(New_staff==1):
            print("You need to train all the new staffs")
            if(change_process==1):
                print("There is a change in processes, a training is needed")
                break
            
        else:
            print("All current staff are competent to use the system")
    else:
        if(refresher_training>2):
         print("You have done more than 2 refresher trainings.Full training is recommended")
else:
    if(support_requests>5 and refresher_training>2):
     print("This are far too many support requests. You definitely need to do a refresher Training")

            


