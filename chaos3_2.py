from autolib import *

def f(x):
    return 4*x*(1-x)

def fi(X,i):  # recursive function that return fofof..f  i time
    if(i==0): return X
    return f(fi(X,i-1))

ax = init_figure(0,1,0,1)
X = arange(0,1,0.001)
plot(X,fi(X,3), 'blue',linewidth = 2)

plot(X,X,'green',linewidth = 2)

pause(100)
