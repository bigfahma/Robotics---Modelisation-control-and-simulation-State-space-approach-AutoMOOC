from autolib import *

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

E = array([[1,0,0,0]])
Pcon = [-2,-2.1,-2.2,-2.3]
Pobs = [-2,-2.1,-2.2,-2.3]

theta_list = []
u_list = []
s_list = []
Ar,Br,Cr,Dr = RegulKLH(A,B,C,E,Pcon,Pobs)

dt = 0.1
Ts = 20
x = array([[0,0.02,0,0]]).T
xhat = array([[0,0,0,0]]).T
print(xhat.shape)


ax = init_figure(-3,3,-3,3)
T_list = arange(0,Ts,dt)


for t in T_list:
    clear(ax)
    w = sign(sin(t*0.3))
    y = C@x + mvnrnd1(0.001**2)
    plot(w,0.5,'o')

    draw_invpend(ax,x)


    u = Cr@xhat+ Dr@vstack((w,y))

    xhat = xhat + dt*( Ar@xhat + Br@vstack((w,y)))
    x = x + dt*f(x,u)
    #print(x)
    u_list.append(u)
    s_list.append(x[0,0])
    theta_list.append(x[1,0])

u_list = np.array(u_list).reshape(200,1)
s_list = np.array(s_list).reshape(200,1)
theta_list = np.array(theta_list).reshape(200,1)

ax = init_figure(0,Ts,-10,10)

clear(ax)
plot(T_list, u_list, color = 'red')
plot(T_list, s_list,color = 'blue')
plot(T_list,theta_list,color = 'black')

pause(10)