from autolib import *

def f(x,u):
    theta,v,delta = list(x[1:4,0])
    return array([[v*cos(theta)*cos(delta), v*sin(delta), u[0][0], u[1][0]]])


ax = init_figure(-30,50,-20,50)
P= array([[0,-15], [1,-15], [1,15],[0,15]])
x=array([[-5],[2],[6.7],[0.1]])

dt = 0.01

for t in arange(0,4,dt):
    clear(ax)
    mx,theta,v,delta = list(x[0:4,0])
    y = array([[0.05*randn() + mx/sin(theta)], [v],[delta]])
    u = array([[0.1,0]]).T
    x = x +dt*f(x,u)
    draw_car([[-mx],[0],[theta],[v],[delta]],"blue",0.7,1)
    draw_polygon(ax,P,'green')
    d = y[0,0]
    plot([-mx,-mx+sin(theta)*d],[0,0-cos(theta)*d], 'red')

pause(10)