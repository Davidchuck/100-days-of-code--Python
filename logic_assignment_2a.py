#given a and  b ∧ ¬c =  a or (b ∧ (¬c)).

a=True
b=False
c=True

var_bc=b and not c #b ∧ ¬c False and false = false
var_bc1= b and (not c) # (b ∧ (¬c)). false and not false =false
var_x=a and var_bc # a and  b ∧ ¬c True and false = false
var_y=a or var_bc1 #a or (b ∧ (¬c)) True and false =false
result=var_x = var_y # false=false, true

print(result)


