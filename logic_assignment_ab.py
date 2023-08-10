#given (p or q) not (¬q and ¬p)
p=True
q=False

Var_a=p or q # (p or q)
var_b= (not q) and (not q) #(¬q and ¬p)
var_c=not var_b #not (¬q and ¬p)

result=Var_a; not var_c

print (result)