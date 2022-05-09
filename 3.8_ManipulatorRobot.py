from autolib import *

U = array([[0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1],
          [0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0],
          [0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

e = 0.3 #thickness
L1 = 3
v1 = 2 # speed of arm1
L2 = 2
v2 = -4
v3 = 5
L3 = 1
dt =0.01
Ts = 3
fig = figure()


ax = Axes3D(fig)


S0 = tran3H(-0,-0.5,-0.5)@U

for t in arange(0,Ts,dt):
    clean3D(ax,-4,4,-4,4,-4,4)
    draw_axis3D(ax)

    alpha1 = v1*t
    alpha2 = v2*t
    alpha3 = v3*t

    arm1 = rot3H(0,0,alpha1)@diag([L1,e,e,1])@S0
    arm2 = rot3H(0,0,alpha1)@tran3H(L1,0,0)@rot3H(0,0,alpha2)@diag([L2,e,e,1])@S0
    arm3 = rot3H(0,0,alpha1)@tran3H(L1,0,0)@rot3H(0,0,alpha2)@tran3H(L2,0,0)@rot3H(alpha3,0,0)@diag([L3,e,e,1])@S0

    draw3H(ax,arm1,'blue')
    draw3H(ax,arm2,'green')
    draw3H(ax,arm3,'red')

    pause(0.01)

pause(10)