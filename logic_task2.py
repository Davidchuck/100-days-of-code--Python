#Given (not P and not Q ) or (Q and not R)
P=True
Q=False
R=False

var_p=(not P) and (not Q) #false
var_q=Q and (not R) #false

result=var_p or var_q #false

print(result)

