from sympy import *


s = symbols("s")

A = Matrix([[1,3],[2,0]])
B = Matrix([1,1])
C = Matrix([[1,2],[1,0]])
D = Matrix([2,0])


print('\n A =')
pprint(A)
print('\n B =')
pprint(B)
print('\n C =')
pprint(C)
print('\n D =')
pprint(D)

G = C*(s*eye(2)-A).inv()*B + D
print(G)
G = simplify(G)

print('\n G =')
pprint(G)

