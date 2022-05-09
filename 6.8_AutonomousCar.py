from autolib import *
def g(x):
    mx,my,theta,v,delta = list(x[0:5,0])
    u = [sin(theta), -cos(theta)]
    m = [mx,my]
    d = inf

    for i in range(len(P)-1):
        a,b = P[i],P[i+1]
        alpha = det([a-m,b-a]) / det([u,b-a])
        if (det([a-m,u])*det([b-m,u]) <= 0 and alpha >=0):
            d = min(alpha,d)
    return array([[d,v,delta]]).T

def f(x,u):
    theta,v,delta = list(x[2:5,0])
    return array([[v*cos(theta)*cos(delta), v*cos(delta)*sin(theta), v*sin(delta), u[0][0], u[1][0]]]).T

def draw_laser(x,d):
    mx,my,theta,v,delta = list(x[0:5,0])
    plot([mx,mx+sin(theta)*d], [my,my-cos(theta)*d], 'red')


ax = init_figure(-30,50,-20,50)
P=array([[-10,-5],[-10,5],[0,15],[10,20],[20,20],[32,15],[35,10],[30,0],[20,-3],[0,-6],[-10,-5]]) 
x=array([[-15],[0],[pi/2],[1],[0.01]])

dt = 0.03

for t in arange(0,10,dt):
    clear(ax)
    y = g(x)
    u = array([[0.1,0]]).T
    x = x +dt*f(x,u)
    draw_car(x,"blue",0.7,1)
    draw_polygon(ax,P,'green')
    draw_laser(x,y[0,0])

pause(10)