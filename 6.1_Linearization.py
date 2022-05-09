from sympy import *
from autolib import *


x1,x2 = symbols("x1 x2")

F = Matrix([(1-x2)*x1,  (x1-1)*x2])
X = Matrix([x1,x2])
J = F.jacobian(X); pprint(J)

x1bar,x2bar = 1,1
Xbar = Matrix([x1bar,x2bar]); pprint(Xbar)
Ybar = F.subs({x1:x1bar, x2:x2bar}); pprint(Ybar)
Jbar = J.subs({x1:x1bar, x2:x2bar}); pprint(Jbar)

L = Ybar + Jbar*(X-Xbar); pprint(L)

fl = lambdify((x1,x2), L) # a function that can be called
f = lambdify((x1,x2), F) # a function that can be called

def fl_(x1,x2): return fl(x1,x2)[0,0], fl(x1,x2)[1,0]
def f_(x1,x2): return f(x1,x2)[0,0], f(x1,x2)[1,0]

xmin,xmax,ymin,ymax = 0,2,0,2

ax = init_figure(xmin,xmax,ymin,ymax)
draw_field(ax,fl_,xmin,xmax,ymin,ymax,0.1)
draw_field(ax,f_,xmin,xmax,ymin,ymax,0.1,color ='red')

pause(10)


