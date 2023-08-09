#given (p ∨ q) ∧ (p or  ¬ q)

p=False
q=True

var_pq=p or q # (p ∨ q)
var_pq2=p or (not q) # (p or  ¬ q)

result=var_pq and var_pq2 #(p ∨ q) ∧ (p or  ¬ q)

print (result)