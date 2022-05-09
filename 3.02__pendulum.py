from autolib import *  # available at https://www.ensta-bretagne.fr/jaulin/autolib.py

       
def draw_pend(x,col): 
    θ=x[0]
    plot([0,-sin(θ)],[0,-cos(θ)],col, linewidth = 2)

def f(x1,x2):
    return x2,-sin(x1)

def f1(x):
    x1,x2 = f(x[0],x[1])
    return array([x1,x2])    

s=3 
x=array([[1],[2]])
ax=init_figure(-s,s,-s,s)


dt = 0.1
Ts = 50
xe = array([0,0.5]) 
xRK= array([0,0.5])


for t in arange(0,Ts,dt):
    xe = clock_Euler(f1,xe,dt)
    xRK = clock_RK(f1,xRK,dt)
    clear(ax)
    draw_pend(xe,'red')    
    draw_pend(xRK,'blue')    


    pause(0.1)

pause(10)
    
    



