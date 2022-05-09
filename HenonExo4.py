from autolib import *

def f(x1,x2):
    return x2+1-1.4*x1*x1,0.3*x1

ax = init_figure(-1.5,1.5,-0.5,0.5)


for k in range(1,3000):  # Plot 3000 points
    x1 = 4*rand() - 2
    x2 = 4*rand() - 2
    for ind in range(1,100): # 100 iteration to obtain those in inv(A)

        if (x1<2)&(x1>-2)&(x2<2) &(x2>-2): # f(x1,x2) included in A=[-2,2]*[2,2]
            x1,x2 = f(x1,x2)
    ax.scatter(x1,x2, color = 'red',linewidth=0.1)

pause(10)




