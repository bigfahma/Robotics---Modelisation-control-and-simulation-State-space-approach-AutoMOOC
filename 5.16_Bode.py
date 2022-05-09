from autolib import *

w =1
Aobs = [[-2,w], [-1/w,0]]
Bobs = [[2*w],[1-w**2]]
Cobs = [[1/w, 0]]
Dobs = [0]

demodulator = ss(Aobs,Bobs,Cobs,Dobs)

bode(demodulator, Hz = False)

pause(100)