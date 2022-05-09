from sympy import *

s = symbols("s")

A = Matrix ([[-1,1,0,0], [0,1,0,0], [1,1,1,1], [0,1,0,1]])
B = Matrix([1,0,1,0])
C = Matrix([[1,1,0,0]])
D = Matrix([1])

G = C*(s*eye(4) - A).inv()*B + D

print(simplify(G))
print('-----------------------------------')

Eigenvalues = A.eigenvals()
print('Eigen Values :',Eigenvalues)
print('-----------------------------------')
P = A.charpoly(s)

print('Characteristic polynomial :',factor(P.as_expr()))