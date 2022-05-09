from autolib import * 

def f(x1,x2):
    return -p1*x1*x2/N, p1*x1*x2/N-p2*x2


N = 100
p1,p2 = 0.3,0.1
Ts = 200 # day
dt = 0.1
ax = init_figure(0,Ts,0,N)
N0 = 1/1000000
x1,x2 = N-N0,N0

time = np.arange(0,Ts,dt)
x1_graph = []
x2_graph = []
x3_graph = []

for t in arange(0,Ts,dt):
    x1_graph.append(x1)
    x2_graph.append(x2)
    x3_graph.append(N-x1-x2)

    dx1,dx2 = f(x1,x2)
    x1 = x1 +dt*dx1
    x2 = x2 + dt*dx2


ax.plot(time,x1_graph,color ='blue')
ax.plot(time,x2_graph,color ='red')
ax.plot(time,x3_graph,color ='green')


pause(100)

