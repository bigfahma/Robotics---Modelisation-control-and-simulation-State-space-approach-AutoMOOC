from autolib import * 


def wheel3H(r):
    n = 12
    W0 = [[0,0,0],[r,0,r],[0,0,0],[1,1,1]]
    W = W0
    R = rot3H(2*pi/n,0,0)
    for i in range(n+1):
        W0 = R@W0
        W = hstack((W,W0)) 

    return W   


def draw_3Dtricycle(x):
    mx,my,theta,v,delta,s1,s2,s3 = list(x[0:8])
    a = 0.5
    B = array([[-1,2,1,0,-1,-1,2,1,0,-1,0,0,1,1,2,L,2,0,0,0],
            [-1,-1,-a,-a,-1,1,1,a,a,1,a,-a,-a,a,1,0,-1,-1,-e,e],
            [0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
    Rb = tran3H(mx,my,r)@rot3H(0,0,theta) # rotate the heading by theta & translate to (x,y,r)

    # Wheel
    W = wheel3H(r)
    R1 = Rb@tran3H(0,-e,0)@rot3H(0,s1,0)@rot3H(0,0,pi/2) # rotation pi/2 to align the wheel, then by S1, then translate by -e to put it in it's initial place => by Rb
    R2 = Rb@tran3H(0,e,0)@rot3H(0,s2,0)@rot3H(0,0,pi/2)
    R3 = Rb@tran3H(L,0,0)@rot3H(0,0,delta)@rot3H(0,0,pi/2) # rotation pi/2 to align the wheel, then by S3,then by delta, then translate by L to put it in it's initial place => by Rb
    
    draw3H(ax,R1@W,'red')
    draw3H(ax,R2@W,'red')
    draw3H(ax,R3@W,'red')
    draw3H(ax,Rb@B,'blue')

def f(x,u):
    mx,my,theta,v,delta = list(x[0:5,0])
    u1,u2 = list(u[0:2,0])

    return array([[v*cos(delta)*cos(theta)],
                 [v*cos(delta)*sin(theta)],
                 [v*sin(delta)/L],
                 [u1],
                 [u2],
                 [(v/r)*(cos(delta) + e*sin(delta)/L)],
                 [(v/r)*(cos(delta) - e*sin(delta)/L)],
                 [v/r]])



L, e, r = 3, 2, 0.5
Ts = 5
dt  = 0.005
u = array([[1],[1]])

fig = figure()
ax = Axes3D(fig)

x =array([[-2],[-2],[-1],[15],[0.3],[0],[0],[0]])
for t in arange(0,3,dt):
    clean3D(ax)
    x = x +dt*f(x,u)
    draw_3Dtricycle(x)
    pause(0.005)

pause(100)
    