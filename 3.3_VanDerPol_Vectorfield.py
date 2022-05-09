from autolib import * 


def draw_field(ax,f,xmin,xmax,ymin,ymax,sampling):
    M1 = arange(xmin,xmax,sampling)
    M2 = arange(ymin,ymax,sampling)
    
    X1,X2 = meshgrid(M1,M2)
    V1, V2 = f(X1,X2)
    R = sqrt(V1**2 + V2**2) # for normalization
    quiver(M1,M2,V1/R,V2/R) #Plot a 2D field of arrows.

def f(x1,x2):
    return x2, -(x1**2 -1)*x2 - x1

def f1(x):
    x1,x2 = f(x[0],x[1])
    return array([x1,x2])

xmin,xmax,ymin,ymax = -3,3,-3,3
sampling = 0.2
ax = init_figure(xmin,xmax,ymin,ymax)

draw_field(ax,f,xmin,xmax,ymin,ymax,sampling)


dt = 0.1
Ts = 50
xe = array([0.1,0]) 
xRK= array([0.1,0])

for t in arange(0,Ts,dt):
    xe = clock_Euler(f1,xe,dt)
    xRK = clock_RK(f1,xRK,dt)
    ax.scatter(xe[0],xe[1],4,color = 'red')
    ax.scatter(xRK[0],xRK[1],4,color = 'blue')
    pause(0.1)

pause(10)
