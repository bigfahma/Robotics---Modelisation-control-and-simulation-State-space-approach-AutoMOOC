from autolib import * 


def f(x,t):
    x1,x2,x3,x4,x5 = list(x[0:5,0])
    u1,u2 = list(u(t)[0:2,0])
    return array([[x4*cos(x3)], [x4*sin(x3)], [x5], [u1], [u2]])

def u(t):
    return array([[cos(t)],[sin(t)]])

def udot(t):
    return array([[-sin(t)],[cos(t)]])

def Euler(x,t,dt):
    return x + dt*f(x,t)

def RK(x,t,dt):
    return x+ dt*(0.25*f(x,t) + 0.75*(f(x+dt*0.75*f(x,t),t+0.75*dt)))

def Taylor(x,t,dt):
    x1,x2,x3,x4,x5 = list(x[0:5,0])
    u1,u2 = list(u(t)[0:2,0])
    u1dot, u2dot = list(udot(t)[0:2,0])
    xdot = f(x,t)

    x1_2dot = u1*cos(x3) - x4*x5*sin(x3)
    x2_2dot = u1*sin(x3) + x4*x5*cos(x3)
    x3_2dot = u2
    x4_2dot = u1dot
    x5_2dot = u2dot
    x2dot = array([[x1_2dot],[x2_2dot],[x3_2dot],[x4_2dot],[x5_2dot]])
    return x + dt*xdot + (0.5*dt**2)*x2dot


Ts = 12
dt = 0.05
x0 = array([[0],[0],[0],[5],[-0.5]])

xE = x0
xRK = x0
xTaylor = x0

xmin,xmax,ymin,ymax = -15,20,-10,20
ax = init_figure(xmin,xmax,ymin,ymax)

for t in arange(0,Ts,dt):

    xE = Euler(xE,t,dt)
    xRK = RK(xRK,t,dt)
    xTaylor = Taylor(xTaylor,t,dt)
    
    draw_tank(xE,'red',2)
    draw_tank(xRK,'blue',2)
    draw_tank(xTaylor,'Green',2)


    clear(ax)
    