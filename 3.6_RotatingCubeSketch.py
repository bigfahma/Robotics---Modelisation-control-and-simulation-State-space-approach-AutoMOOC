from autolib import * 
def draw3H(ax,M):
    ax.plot(M[0],M[1],M[2])

def add1(M): # Homogeneous transformation
    return vstack((M,ones(M.shape[1])))
    
Cube_Sketch = array([[0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1],
                     [0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0],
                     [0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0]])
                     
Cube_Sketch = add1(Cube_Sketch)
fig = figure()
ax = Axes3D(fig)
Ts = 5
dt = 0.1

for t in arange(0,Ts,dt):
    Rh = rot3H(t,0,0)
    Rotated_cube = Rh@Cube_Sketch
    clean3D(ax,-3,3,-3,3,-1,5)
    draw_axis3D(ax)
    draw3H(ax,Rotated_cube)
    pause(0.01)