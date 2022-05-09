from autolib import * 

def f(x1,x2):
    return -p1*x1*x2/N, p1*x1*x2/N-p2*x2


N = 100
p1,p2 = 0.3,0.1
Ts = 200 # day
dt = 0.1
N0 = 1/1000000
x1,x2 = N-N0,N0

time = np.arange(0,Ts,dt)
x1_graph = []
x2_graph = []

ax = init_figure(0,N,0,N/2)
draw_field(ax,f,0,N,0,N/2,5)
for t in arange(0,Ts,dt):
    x1_graph.append(x1)
    x2_graph.append(x2)

    dx1,dx2 = f(x1,x2)
    x1 = x1 +dt*dx1
    x2 = x2 + dt*dx2


ax.plot(x1_graph,x2_graph,color ='red')
pause(10)

