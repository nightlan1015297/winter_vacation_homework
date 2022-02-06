# Differential equation of RLC circuit
# L*d^2i/dt^2 + R*di/dt + 1/C*i = 0
# replace di/dt with s 
# equation becomes: L * ds/dt + s*R + 1/C = 0
# Then we can Euler method to solve the equation numercially

import matplotlib.pyplot as plt
import numpy as np

# Over damped case

R = 100
C = 0.00001
L = 0.01
ti = 0
tf = 0.02
i0 = 5

t1 = [ti]
i1 = [i0]
s1 = [0]

dt = 0.0001

for j in range(int((tf-ti)/dt)):
    t1.append(t1[j] + dt)
    i1.append(i1[j] + dt*s1[j])
    s1.append(s1[j] - dt*s1[j]*R/L - dt*(1/(L*C))*i1[j+1])

dt = 0.000001
t2 = [ti]
i2 = [i0]
s2 = [0]
for j in range(int((tf-ti)/dt)):
    t2.append(t2[j] + dt)
    i2.append(i2[j] + dt*s2[j])
    s2.append(s2[j] - dt*s2[j]*R/L - dt*(1/(L*C))*i2[j+1])

omega = np.sqrt(-1/(L*C)+(R/(2*L))**2)

# Analytical solution
def Overdamped(V0,t):
    return V0/(omega*L)*np.exp((-R/(2*L))*t)*np.sinh(omega*t)



best  = -1
error = 999

# Find the best value of initial charge on the capacitor
# Since we can't know the exact value from the initial current 
step = (650-550)/10000
for i in range(10000):
    vol = 550+i*step
    err = abs(Overdamped(vol,0.00026599999999999996)-5)
    if err<error:
        best = vol
        error = err

t3 = [ti]
i_exect = [Overdamped(best,ti)]
dt = 0.000001

for j in range(int((tf-ti)/dt)):
    t3.append(t3[j] + dt)
    i_exect.append(Overdamped(best,t3[-1])) 
x_offset = i_exect.index(max(i_exect))

# Error analysis
# Error is the difference between the analytical solution and the numerical solution
# To qunatify the error, we use the mean square error to calculate the error
error_1 = 0
error_2 = 0
for i in range(len(t1)):
    error_1 += (i1[i]-Overdamped(best,t1[i]-t3[x_offset]))**2
for i in range(len(t2)):
    error_2 += (i2[i]-Overdamped(best,t2[i]-t3[x_offset]))**2    
# print the error
print("Error (step = 0.0001) : ",np.sqrt(error_1/len(t1)))
print("Error (step = 0.00001) : ",np.sqrt(error_2/len(t2)))

# plot the graph (current vs time)
plt.plot(t1, i1,label='step = 0.0001')
plt.plot(t2, i2,label='step = 0.00001')
plt.plot([time-t3[x_offset] for time in t3[x_offset:]], i_exect[x_offset:],label='Exact')
#add legend
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('RLC circuit')
# set the x-axis limit
plt.show()