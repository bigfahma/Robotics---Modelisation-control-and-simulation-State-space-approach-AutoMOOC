from autolib import *

m,M,l,g,p,Jp = 10,1,1,10,1,10

Jm = 0.5*M*p**2
u1 = Jm+p**2*(m+M)
u2 = Jp + m*l**2
u3 = p*m*l
ug = g*l*m

dt = 0.03
Ts = 10 

def f(x,u):
    s,theta,sdot,thetadot = list(x[0:4,0])
    denominator = (u1*u2 - u3**2*cos(theta)**2)

    s2dot  = (u3*(u2*thetadot**2 - ug*cos(theta))*sin(theta) + (u2+u3*cos(theta))*u) / denominator
    theta2dot =  ((u1*ug - u3**2*thetadot**2*cos(theta))*sin(theta) - (u1 +u3*cos(theta))*u) / denominator
    return array([[sdot], [thetadot], [s2dot], [theta2dot]]).astype(float)


A = array([ [0,0,1,0],  [0,0,0,1],  [0,-u3*ug/(u1*u2 - u3**2),0,0], [0,u1*ug/(u1*u2-u3**2),0,0] ])
B = array([ [0],    [0],    [(u2+u3)/(u1*u2 - u3**2)],  [(-u1-u3)/(u1*u2-u3**2)]    ])
C = array([[1,0,0,0]])

E = array([[-p,0,0,0]]) # - because of the direction


ax = init_figure(-2,7,-1,8)
x0 = array([[0],[0],[0], [0]]) # Initial condition
x,xr = x0,x0
#w = 2.0
Ar, Br, Cr, Dr = RegulKLH(A,B,C,E,[-2.0,-2.1,-2.2,-2.3],[-2.0,-2.1,-2.2,-2.3])
for t in arange(0,Ts,dt):
    w = t # 
    y = C@x +0.01*randn()
    u = (Cr@xr + Dr@array([[w],[y]]))

    x = x +dt*f(x,u) 
    xr = xr + dt*(Ar@xr + Br@array([[w],[y]]))
    clear(ax)
    draw_segway(ax,x,'black',1)


pause(3)
