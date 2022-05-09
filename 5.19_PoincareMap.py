from autolib import *

def draw_tank(x,col='darkblue',r=1,w=2):
    mx,my,θ=list(x[0:3])
    M = r*array([[1,-1,0,0,-1,-1,0,0,-1,1,0,0,3,3,0], [-2,-2,-2,-1,-1,1,1,2,2,2,2,1,0.5,-0.5,-1]])
    M=add1(M)
    plot2D(tran2H(mx,my)@rot2H(θ)@M,col,w)

def clock(x,q,c,dt):
    x1,x2,psi = x
    c = c + dt
    if (q==0)&(c>5) | (q==1)&(x1+x2**2>20) | (q==2)&(x1<-2):
        q = (q+1)%3
        c=0

    psibar = {0:0, 1:pi/2, 2:4}
    color = {0:'blue',1:'red',2:'green'}
    clear(ax)
    draw_tank(x,color[q],0.1,2)
    x = x + dt*array([cos(psi),sin(psi),sin(psibar[q]-psi)])
    x[2] = sawtooth(x[2])
    return x,q,c

x = array([-3,1,-1])
q,c = 0,0
dt = 0.1
ax = init_figure(-4,4,-1,7)
k = 0
x1_points = []
x2_points = []
while True :
    k+=1
    #print(k)
    x1_points.append(x[0])
    x2_points.append(x[1])
    x,q,c = clock(x,q,c,dt)
    if k == 1000 : 
        ax.scatter(x1_points,x2_points,1)
        pause(10)

    