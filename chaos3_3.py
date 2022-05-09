from autolib import *

def f(x):
    return 4*x*(1-x)

ax = init_figure(0,1,0,1)
X=arange(0,1,0.01)
Y=f(X)
plot(X,Y,'red')
plot(X,X,'green')
x1=0.2
x2 = 0.20001

for k in range(0,100):

    y1=f(x1)
    plot([x1,x1,y1],[x1,y1,y1],'black')
    x1=y1

    y2=f(x2)
    plot([x2,x2,y2],[x2,y2,y2],'blue')
    x2=y2
    print(x2-x1)


    
pause(100)    

