from pygame import init
from autolib import *

def lqr(A,B,Q,R):
    X = solve_continuous_are(A,B,Q,R)
    K = inv(R)@(B.T@X) 
    eigVals, eigVecs = eig(A-B*K) 
    print('eigvals',eigVals)
    print('K', K)
    return K

mc,l,g,mr = 5,1,9.81,1
def f(x,u):
    s,theta,sdot,thetadot = x[0,0],x[1,0],x[2,0],x[3,0]

    s2dot = (mr*sin(theta)*(g*cos(theta) - l*thetadot**2) + u)/(mc+mr*sin(theta)**2)
    theta2dot = (sin(theta)*((mr+mc)*g - mr*l*thetadot**2*cos(theta)) + cos(theta)*u) /(l*(mc+mr*sin(theta)**2))
    #print(s,theta,sdot,thetadot)
    return  (array([[sdot],[thetadot],[s2dot], [theta2dot]])).reshape(4,1)

A = np.array([[0,0,1,0],[0,0,0,1], [0,mr*g/mc,0,0], [0,(mc+mr)*g/(mc*l),0,0]])
B = np.array([[0,0,1/mc, 1/(mc*l)]]).T
C = np.array([[1,0,0,0]])

Pcon = [-0.1,-0.1,-0.03,-0.11]
K2 = lqr(A,B,diag([1,20,1,100]), diag([1]))
x0 = array([[50,0,0,0]]).T

dt, kmax = 0.1,200
tmax = dt*kmax
ax = init_figure(-3,55,-20,20)
U2 = zeros(kmax)

x2 = x0
X1Plot = zeros(kmax)

for k in range(0,kmax):
    clear(ax)
    draw_invpend(ax,x2,'blue')

    u2 = -K2@x2

    U2[k] = u2
    x2 = x2 + dt*f(x2,u2)   
    X1Plot[k] = x2[0,0]

pause(1)

ax = init_figure(0,tmax,-50,50)
T = arange(0,tmax,dt)
plot(T,U2,'blue')
plot(T, X1Plot,color = 'red')


pause(100)