from autolib import * 

xmin,xmax,ymin,ymax = -10,100,-10,100
ax = init_figure(xmin,xmax,ymin,ymax)


def Draw_car(x,col='red',L=1,w=2):
    mx,my,theta,v,delta = list(x[0:5])
    Car_sketch = L * array([[-0.3, 1.3, 1.6,1.6,1.3,-0.3,-0.3,-0.3, 0, 0,-0.3, 0.3, 0,0,-0.3,0.3, 0, 0,1,1, 1],  
                            [-0.7,-0.7,-0.3,0.3,0.7, 0.7,-0.7,-0.7,-0.7,-1,-1,-1,-1,1, 1,1, 1, 0.7,0.7,1,-1]]) # Car sketch

    Car_sketch_homoge = add1(Car_sketch) # homogeneous transformation for M1

    R = tran2H(mx,my)@rot2H(theta) # translate by (mx,my) and rotate by theta

    FrontWheel_Sketch = L*array([[-0.3,0.3],[0,0]]) # FrontWheel sketch
    FrontWheel_Sketch_homoge = add1(FrontWheel_Sketch)

    plot2D(R@Car_sketch_homoge,col,w) # Transformation of the Car by R
    plot2D(R@tran2H(L,L)@rot2H(delta)@FrontWheel_Sketch_homoge,col,w)
    plot2D(R@tran2H(L,-L)@rot2H(delta)@FrontWheel_Sketch_homoge,col,w)

def f(x,u):
    theta,v,delta = list(x[2:5])
    u1,u2 = list(u[0:2])
    return array([v*cos(delta)*cos(theta), v*cos(delta)*sin(theta),v*sin(delta)/L,u1,u2])



x = array([1,0,0,50,0])
L = 3
Ts = 5
dt = 0.1

for t in arange(0,Ts,dt):
    u = array([0,0.05])
    x = x + f(x,u)*dt
    clear(ax)
    Draw_car(x,"blue",L,1)
    pause(0.1)
    
