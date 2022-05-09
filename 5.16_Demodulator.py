from autolib import *

dt, Tmax = 0.01, 10
w = 1
a = 2

xhat = array([[0],[0]])
Aobs = array([[-2,w], [-1/w,0]])
Bobs = array([[2*w],[1-w**2]])
Cobs = array([[1/w, 0]])


ax = init_figure(0,Tmax,-3,3)

y_points = []
yhat_points = []
ahat_points = []
t_points = arange(0,Tmax,dt)

for t in t_points :
    y = a*cos(w*t) + 0.1*randn(1,1)
    xhat = xhat + (Aobs@xhat + Bobs*y)*dt
    ahat = (1/w)*norm(xhat)
    yhat = Cobs@xhat

    yhat_points.append(yhat)
    ahat_points.append(ahat)
    y_points.append(y)

ax.scatter(t_points, y_points, 2, color = 'red')
ax.scatter(t_points, yhat_points, 2, color = 'black')
ax.scatter(t_points, ahat_points, 2, color = 'blue')

pause(100)