#given (p∨¬q) and q

var_p=True
var_q=False
Var_pq=var_p or (not var_q)
result=Var_pq and var_q

print(result)