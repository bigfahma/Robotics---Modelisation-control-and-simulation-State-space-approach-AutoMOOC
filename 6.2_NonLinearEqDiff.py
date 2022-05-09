from sympy import *

t = symbols("t")
y = symbols("y",cls =Function)

E = Eq(y(t).diff(t,t) + (y(t).diff(t)**2), 0);pprint(E)
yt = dsolve(E,y(t)); pprint(yt)