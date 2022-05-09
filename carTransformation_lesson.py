from autolib import *

def add1(M): # Homogeneous transformation
    return vstack((M,ones(M.shape[1]))) #Stack arrays in sequence vertically (row wise).

def tran2H(x,y): # Translation matrix by a vector(x,y)
    return array([[1,0,x], [0,1,y],[0,0,1]])

def rot2H(angle): # Rotation matrix by angle in a plane (Rz)
    return array([[cos(angle),-sin(angle),0], [sin(angle),cos(angle),0], [0,0,1]]) 

xmin,xmax,ymin,ymax = -10,10,-10,10
ax = init_figure(xmin,xmax,ymin,ymax)

P = array([[0,0],[3,0],[0,3]]) # Reference polygone(triangle)
draw_polygon(ax,P,'green')

mx,my,theta,delta = 0,1,1,1 # initialX,initialY,headingAngle,steeringAngle
scale  = 1

Car_sketch = array([[-1,4,5,5,4,-1,-1,-1,0,0,-1,1,0,0,-1,1,0,0,3,3,3],
      [-2,-2,-1,1,2,2,-2,-2,-2,-3,-3,-3,-3,3,3,3,3,2,2,3,-3]]) # Car sketch

Car_sketch_homoge = add1(scale*Car_sketch) # homogeneous transformation for M1

R = tran2H(mx,my)@rot2H(theta) # translate by (0,1) and rotate by theta

FrontWheel_Sketch = array([[-1,1],[0,0]]) # FrontWheel sketch
FrontWheel_Sketch_homoge = add1(scale * FrontWheel_Sketch)
plot2D(Car_sketch_homoge,'black')
plot2D(R@Car_sketch_homoge,'red') # Transformation of the Car by R
plot2D(R@tran2H(3*scale,3*scale)@rot2H(delta)@FrontWheel_Sketch_homoge,'blue')
plot2D(R@tran2H(3*scale,-3*scale)@rot2H(delta)@FrontWheel_Sketch_homoge,'black')

pause(100)