from autolib import *

m,M,l,g,p,Jp = 10,1,1,9.81,1,10

Jm = 0.5*M*p**2
u1 = Jm+p**2*(m+M)
u2 = Jp + m*l**2
u3 = p*m*l
ug = g*l*m

dt = 0.01 #sampling time
Ts = 10 # Simulation time

def f(x,u):
    s,theta,sdot,thetadot = list(x[0:4,0])
    denominator = (u1*u2 - u3**2*cos(theta)**2)

    s2dot  = (u3*(u2*thetadot**2 - ug*cos(theta))*sin(theta) + u*(u2+u3*cos(theta))) / denominator
    theta2dot = (u1*ug - u3*thetadot**2*cos(theta)*sin(theta) - (u1 +u3*cos(theta)*u)) / denominator
    return array([[sdot], [thetadot], [s2dot], [theta2dot]])

ax = init_figure(-10,10,-10,10)
x = array([[0],[0.5],[0], [0]]) # Initial condition

u = 0 # no external torque

for t in arange(0,Ts,dt):

    x = x +dt*f(x,u) # euler integration
    clear(ax)
    draw_segway(ax,x,'black',1)

pause(3)