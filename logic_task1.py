#given ((P or Q) and R) or ((P and R) or (Q and R))
P=True
Q=False
R=False

var_p=P or Q #True or False=True
Var_q= R # False
var_pq=var_p and Var_q #True and False =False

var_x=P or R #True of False = True
var_y=Q and R #False and False =False
var_xy=var_x or var_y #True or False =True

result=var_pq or var_xy #False or True = True

print(result) #Result therefore is True

