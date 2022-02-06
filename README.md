> Dear all,
> &emsp; Your winter vacation homework is to simulate RLC circuit with Python,
> and a preview of  Runge-Kutta methods (RK4).
> The recommened IDE is
> 1.    Colab (from Google)
> 2.    Jupyter notebook (Anaconda)
> 
> &emsp;You need at least to simulate the current as the function of time in 3 different types of oscillations     by Euler method, and compare your results with analytical solution.
> &emsp;Output your results and plot them with Igor.


Using Kirchhoff’s voltage law, the second-order differential equation of the RLC circuit can be write down as :    
$$L\frac{d^2i}{dt^2}+R\frac{di}{dt}+\frac{1}{C}i = 0$$

We can not use the Euler methods directly on second-order differential equation, thus we have to convert the equation into two first-order differential equation.

let $s = \frac{di}{dt}$ , the equation becomes : 

$$L\frac{ds}{dt}+R\times{s}+\frac{1}{C} = 0$$

rearrange the equation we can get that $\frac{ds}{dt} = -(S\times{\frac{R}{L}}+\frac{1}{L\times{C}})$
By Euler's method we can know that : 
$$s_{k+1} = s_{k}-\Delta{t}\times{s_k}\times{\frac{R}{L}}-\frac{\Delta{t}}{L\times{C}}$$
$$i_{k+1} = i_k + \Delta{t}\times{s_k}$$
# Implementation
The implement of Euler method for RLC circuit
```python=
t = [ti]
i = [i0]
s = [0]
for j in range(int((tf-ti)/dt)):
    t.append(t[j] + dt)
    i.append(i[j] + dt*s[j])
    s.append(s[j] - dt*s[j]*R/L - dt*(1/(L*C))*i[j+1])
```

With these code we can calculate the point step by step. 

The analytic result to compare is defined by : 
- Under damped
$$\omega = \sqrt{1/LC-(R/(2\times{L}))^2}$$
$$I(t) = \frac{V_0}{\omega{L}}{\times}e^{(\frac{-Rt}{2L})}\sin(\omega{t})$$

- Over damped

$$\omega = \sqrt{-1/LC+(R/(2\times{L}))^2}$$

$$I(t) = \frac{V_0}{\omega{L}}{\times}e^{\frac{-Rt}{LC} }\sinh(\omega{t})$$

-Cricical damped

$$I(t) = \frac{V_0t}{{L}}e^{\frac{-Rt}{2L}}$$

# Result
- Under damped case
![](https://i.imgur.com/HW9i07p.png)
![](https://i.imgur.com/a1I6kg2.png)

We can see that when the step is getting smaller and smaller the percision of the Euler methods becomes more higher, in the case as figure shown the orange line is almost equals to the analitic solution.

To qunatify the error, I use the mean square error to calculate the error
![](https://i.imgur.com/tChfSzW.png)

We can see that the error becomes smaller when the step become smaller.

We can now see what will happen in overdamped and critical damped case.

- Over damped case :
![](https://i.imgur.com/7OIcftW.png)
![](https://i.imgur.com/Dx8mAHS.png)

Similarily the orange line was overlapped on the analytic result.
![](https://i.imgur.com/hiEPiG9.png)
The error become smaller too.
- Critical damped case
![](https://i.imgur.com/MKSzvYl.png)
![](https://i.imgur.com/ztcvTdk.png)

Again, the orange line was overlapped on the analytic result.
Also, the orange line's error is smaller.

# Runge-Kutta method (order 4)
Runge-Kutta method provide a more percise solution for differential equation, it uses more computing power to let the result more close to the analytic result (whether there is or not)

- difinition of RK4

for a first-order differential equatoion
$$y'=f(t,y)$$ and $$y(t_0)=y_0$$

For each step $dt$
Next step can be calculate by : 

$$k_1 = f(t_n,y_n)$$
$$k_2 = f(t_n+\frac{dt}{2},y_n+\frac{dt}{2}k_1)$$
$$k_3 = f(t_n+\frac{dt}{2},y_n+\frac{dt}{2}k_2)$$
$$k_4 = f(t_n+dt,y_n+dt\times{k_3})$$

$$y_{n+1} = y_n+\frac{dt}{6}(k_1+2\times{k_2}+2\times{k_3}+k_4)$$
