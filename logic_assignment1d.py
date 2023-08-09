#given p ∨ (q ∧ r) 

p=True
q=True
r=False

var_x= q and r #(q ∧ r)

result= p or var_x #p ∨ (q ∧ r)

print(result)