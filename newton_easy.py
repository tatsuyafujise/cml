import numpy as np 

# x=float(input(""))
x=float(10)
while True:
    xp = x - (x-2*np.cos(1.3*x))/(1+2*1.3*np.sin(1.3*x))
    if abs(xp-x)<0.00001:
       break
    x = xp

print("x=",xp)

# x = 0.8644783765297862