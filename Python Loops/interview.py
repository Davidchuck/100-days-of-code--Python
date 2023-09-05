#Interview all shortlisted candidates 
#Variables
candidates=9
rating=int(input("Rate the candidate\'s performance 1-10. One being the weakest and 10 the strongest: "))
Appoint=1 #1 being success and 0 being unsuccessful

while (candidates<10):
    candidates=candidates+1
    if(rating>7):
        print("Consider this candidate for the next level.")
        if(Appoint==1):
            print("Conraturatoins you passed the interview.")
        else:
            print("Sorry, we couldn\'t proceed with you.")
    else:
        print("You did not do well in this interview.7
         Best of luck next time")
