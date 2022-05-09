from sympy import * 
a = symbols('a')
b = symbols('b')

A = Matrix([[1,1,0],[0,1,0],[0,0,1]])
B = Matrix([[0,0],[1,0],[1,a]])
C = Matrix([[1,1,b],[0,1,0]])


G_con = B.row_join(A*B).row_join(A**2*B)
G_obs = C.col_join(C*A).col_join(C*A**2)
print('G_controllability :')
pprint(G_con)
print('Rank(G_con) = ')
pprint(G_con.rank())
print('G_Observability :')
pprint(G_obs)
print('Rank(G_Obs) = ')
pprint(G_obs.rank())

