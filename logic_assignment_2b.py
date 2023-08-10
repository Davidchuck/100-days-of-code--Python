#given (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q).

p=True
q=False

var_a=p and q #(p ∧ q)
var_b=(not p) and q #(¬p ∧ q)
var_c=(not p) and (not q) #(¬p ∧ ¬q)

result= var_a or var_b or var_c # (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q)

print(result)