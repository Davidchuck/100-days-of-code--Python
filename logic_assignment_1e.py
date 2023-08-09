# given ¬(p ∧ q) ∨ (p ∨ q)

p=False
q=True

var_x=p and q #(p ∧ q)=True
var_z=not var_x #¬(p ∧ q) = false
var_y=p or q #(p ∨ q) =true


result=var_z or var_y #¬(p ∧ q) ∨ (p ∨ q) 

print(result)