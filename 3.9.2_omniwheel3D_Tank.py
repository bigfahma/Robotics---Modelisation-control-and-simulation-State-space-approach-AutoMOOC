from autolib import * 

def draw_omniwheel3D(x):
    mx,my,theta,s1,s2,s3 = list(x[0:6])
    B = array([[a,-a/2,-a/2,a,0],                           #Sketch of the robot (without wheels)
               [0, a*sqrt(3)/2, -a*sqrt(3)/2,0,0],
               [r,r,r,r,r]])
    B = add1(B)
    W0 = wheel3H(r) # ref wheel
    W1 = tran3H(mx,my,0)@rot3H(0,0,theta)@tran3H(a,0,r)@rot3H(s1,0,0)@W0
    W2 = tran3H(mx,my,0)@rot3H(0,0,theta)@rot3H(0,0,2*pi/3)@tran3H(a,0,r)@rot3H(s2,0,0)@W0
    W3 = tran3H(mx,my,0)@rot3H(0,0,theta)@rot3H(0,0,4*pi/3)@tran3H(a,0,r)@rot3H(s3,0,0)@W0

    Chassis = tran3H(mx,my,0)@rot3H(0,0,theta)@B # position to initial reference
    draw3H(ax,Chassis,'black')
    draw3H(ax,W1,'red')
    draw3H(ax,W2,'blue')
    draw3H(ax,W3,'green')

def f(x,w):
    x,y,theta,s1,s2,s3 = x[0:6]
    w1,w2,w3 = w[0:3]
    xdot,ydot,thetadot = list((inv(A)@w))[0:3]
    #print(inv(A)@w)
    return array([xdot,ydot,thetadot,w1,w2,w3])


fig = figure()
ax= Axes3D(fig)
r,a = 1,3


Ts = 5
dt = 0.01

v = 5
u1,u2 = 1,1

x = array([0,0,0,0,0,0])
for t in arange(0,Ts,dt) :

    clean3D(ax)
    mx,my,theta,s1,s2,s3 = list(x[0:6])
    A = (1/r) * array([[sin(theta), -cos(theta), -a],
                      [sin(theta+2*pi/3), -cos(theta +2*pi/3), -a],
                     [sin(theta-2*pi/3),-cos(theta -2*pi/3), -a]])
    w = A@array([v*cos(theta),v*sin(theta),u1])
    x = x +dt*f(x,w)
    v = v + dt*u2
    draw_omniwheel3D(x)
    pause(0.01)
