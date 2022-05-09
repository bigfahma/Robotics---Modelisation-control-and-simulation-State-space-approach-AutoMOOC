from autolib import *

def draw_snake(x,u):
    mx,my,theta,v,delta = x[0:5]
    u1,u2 = u[0:2]
    beta = arctan(u1)

    M0 = add1(array([[0,-0.3,0.3,0,0,-0.3,0.3,0,0,1],
               [-0.4,-0.4,-0.4,-0.4,0.4,0.4,0.4,0.4,0,0]]))
    R1 = tran2H(mx,my)@rot2H(theta) # ref transfor
    Sledge1 = R1@M0
    Sledge2 = R1@rot2H(delta)@tran2H(-1,0)@M0
    W = array([[-0.4,0.4],[0,0],[1,1]])
    Skate = R1@tran2H(1,0)@rot2H(beta)@W
    
    plot2D(Sledge1,'blue')
    plot2D(Sledge2,'black')
    plot2D(Skate,'red')

def f(x,u):
    mx,my,theta,v,delta = x[0:5]
    u1,u2 = u[0:2]

    return array([v*cos(theta),v*sin(theta),v*u1,-(u1+sin(delta))*u2 -v, -v*(u1+sin(delta))])


xmin,xmax,ymin,ymax = -5,5,-5,5
ax = init_figure(xmin,xmax,ymin,ymax)
Ts = 10
dt = 0.01
x = array([0,0,2,0.1,0])          #x,y,theta,v,delta
p1,p2,p3,p4 = 0.5,3,0,5 
thetaref = pi/6

for t in arange(0,Ts,dt):
    clear(ax)
    mx,my,theta,v,delta = x[0:5]
    p3 = sawtooth(thetaref - theta) # Kp*(thetaref - theta) modulo(2pi)
    u1 = p1*cos(p2*t) + p3
    u2 = p4*sign(-v*(u1+sin(delta)))
    u = array([u1,u2])
    x = x + dt*f(x,u)
    draw_snake(x,u)
    pause(0.01)