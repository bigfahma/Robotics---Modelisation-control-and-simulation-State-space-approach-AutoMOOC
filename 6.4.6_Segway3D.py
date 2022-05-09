from autolib import *

def RegulKLHseg(A,B,C,E,pcom,pobs):
    K=place(A,B,pcom)
    L=place(A.T,C.T,pobs).T
    H=-inv(E@inv(A-B@K)@B)
    Ar=A-B@K-L@C
    Br=hstack((B@H,L))
    Cr=-K
    Dr=hstack((H,0*(B.T@C.T))) 
    return Ar,Br,Cr,Dr  

m,M,l,g,p,Jp = 10,1,1,10,1,10

Jm = 0.5*M*p**2
u1 = Jm+p**2*(m+M)
u2 = Jp + m*l**2
u3 = p*m*l
ug = g*l*m

dt = 0.03
Ts = 10 

def f(x,u):
    theta,sdot,thetadot,px,py,psi,s1,s2 = x[0:8,0]
    print('theta',theta)
    ui1,ui2 = u[0:2,0]
    denominator = (u1*u2 - u3**2*cos(theta)**2)

    s2dot  = (u3*(u2*thetadot**2 - ug*cos(theta))*sin(theta) + (u2+u3*cos(theta))*ui1) / denominator
    theta2dot =  ((u1*ug - u3**2*thetadot**2*cos(theta))*sin(theta) - (u1 +u3*cos(theta))*ui1) / denominator
    pxdot = cos(psi)*sdot
    pydot = sin(psi)*sdot
    s1dot = sdot - ui2
    s2dot = sdot + ui2
    return (array([ [thetadot, s2dot, theta2dot,    pxdot,    pydot,    ui2,   s1dot,   s2dot] ],dtype = float)).T


A = array([ [0,0,1,0],  [0,0,0,1],  [0,-u3*ug/(u1*u2 - u3**2),0,0], [0,u1*ug/(u1*u2-u3**2),0,0] ])
B = (array([[ 0,    0,    (u2+u3)/(u1*u2 - u3**2),  (-u1-u3)/(u1*u2-u3**2)]])).T
print('B',B.shape)
C = array([[1,0,0,0]])


E = array([[1,0,0,0]]) 

fig = figure()
ax = Axes3D(fig)

x= (array([0,0,0,0,0,0,0,0]).T).reshape(8,1) # Initial condition
xr = (array([0,0,0,0]).T).reshape(4,1)

#w = 2.0
pcon = [-2.0,-2.1,-2.2,-2.3]
pobs = [-2.0,-2.1,-2.2,-2.3]
Ar, Br, Cr, Dr = RegulKLHseg(A,B,C,E,pcon,pobs)

C = array([ [0,0,0,0,0,0,0.5,0.5]    ])
print(x.shape)
for t in arange(0,Ts,dt):
    clean3D(ax,-2,20,-2,20,-1,5)
    w = t # 
    y = C@x +0.01*randn()
    print('y',y)
    theta,sdot,thetadot,posx,posy,psi,s1,s2 = list(x[0:8,0])

    psibar = 1

    u = array([ [Cr@xr + Dr@vstack((w,y)) , array(psibar - psi)] ]).T.astype(float)
    print(u)

    x = x +dt*f(x,u) 
    xr = xr + (Ar@xr + Br@vstack((w,y)))*dt
    print('xr',xr)
    print('x',x)
    print('u',u.shape)
    print('f',f(x,u))
    draw_segway3D(ax,posx,posy,theta,psi,s1,s2)


pause(3)