from autolib import * 


def draw_field(ax,f,xmin,xmax,ymin,ymax,sampling):
    M1 = arange(xmin,xmax,sampling)
    M2 = arange(ymin,ymax,sampling)
    
    X1,X2 = meshgrid(M1,M2)
    V1, V2 = f(X1,X2)
    R = sqrt(V1**2 + V2**2) # for normalization
    quiver(M1,M2,V1/R,V2/R) #Plot a 2D field of arrows.

def f(x1,x2):
    return x1+x2, x1-x2

xmin,xmax,ymin,ymax = -2,2,-2,2
sampling = 0.2
ax = init_figure(xmin,xmax,ymin,ymax)

draw_field(ax,f,xmin,xmax,ymin,ymax,sampling)

pause(10)