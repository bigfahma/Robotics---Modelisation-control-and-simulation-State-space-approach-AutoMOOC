from autolib import *
def clock(x,q,c,dt):
    x1,x2,psi = x.flatten()
    c = c + dt
    if (q==0)&(c>5) | (q==1)&(x1+x2**2>20) | (q==2)&(x1<-2):
        q = (q+1)%3
        c=0

    psibar = {0:0, 1:pi/2, 2:4}

    x = x + dt*array([[cos(psi)],[sin(psi)],[sin(psibar[q]-psi)]])
    x[2,0] = sawtooth(x[2,0])
    return x,q,c
    

def p(x):
    q,c = 0,0
    while True :
        q2 = q
        x,q,c = clock(x,q,c,0.001)
        if(q2==2)&(q==0): # switch 
            return x    #  x is in the poincaré section

x = array([[-3],[1],[-1]])

for i in range(1,10):
    x = p(x)
    print('a =', x)

h = 0.001


dp2 = (p(x+[[0],[h],[0]]) - p(x))/h
dp3 = (p(x+[[0],[0],[h]]) - p(x))/h

J = hstack((dp2,dp3))[1:3,:]

print('J =', J)
print('eig, P = ', eig(J))