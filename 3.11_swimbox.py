from autolib import *

def draw_swimbox(x):
    x1,x2 = x[0:2]
    Hull = tran2H(x1,0)@(add1(array([[-5,5,5,-5,-5],
                   [0,0,2,2,0]])))
    Weight = tran2H(x1+x2,0)@(add1(array([[-1,1,1,-1,-1],
                   [0,0,1,1,0]])))

    plot2D(tran2H(x1,0)@Hull,'black')
    plot2D(tran2H(x1+x2,0)@Weight,'red')

def f(x,u):
    x1,x2,v1,v2 = x[0:4]
    return array([v1,v2,-u -v1*abs(v1), 2*u +v1*abs(v1)])

xmin,xmax,ymin,ymax = -15,15,-5,5
ax = init_figure(xmin,xmax,ymin,ymax)

Ts = 50
dt =0.05

x = array([0,0,0,0])
z, u = 0,0.4
for t in arange(0,Ts,dt):
    x1,x2,v1,v2 = x[0:4]
    if (x2>1)&(z==0) : z,u = 1,-0.7
    if (x2<0)&(z==1) : z,u =0,0.4
    clear(ax)
    x = x + f(x,u)*dt
    draw_swimbox(x)

    


