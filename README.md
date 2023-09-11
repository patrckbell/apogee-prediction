# Welcome!!!!
This is a simple tool for projecting the apogee of a rocket using its drag and thrust curve data. 

In order to run the program, a .csv file that tracks the velocity of the rocket against the thrust, drag, and mass of the rocket is required (i.e a thrust curve, drag curve, and mass curve (if thats what its called). The velocity column must be named "Velocity", the mass column "Mass", the thrust column "Thrust", and the drag column "Drag"

## Superduper Boring Mathy Explaination
The formulae used throughout this tool were derrived through good ole calculus!\
In this particular instance, any force due to the wind has been ignored (for now).\
**Therefore:**
$$\sum_{} F_n = F_t - (mg + F_d)$$
And since the equation for drag force ($F_d$)\
 **is given by:**
$$F_d = \frac{1}{2} \rho v^2 A C_d$$
Since $v$ and $C_d$ are codependent, $C_d$ needs to be obtained though math.**EW!!!**\
There is hope, however. **Since**
$$\sum_{} F_n = F_t - (mg + F_d)$$
**and** $$\sum_{} F_n = ma$$
$$ma = F_t - (mg + F_d)$$
**Therefore:**
$$a = \frac{F_t - (mg + F_d)}{m}$$
also since, as we all (hopefully) know:
$$v = \frac{ds}{dt}, a = \frac{dv}{dt}$$
Using all of those fancy lookin equations we can derrive the following equation for $ds$ (the change in height over a given change in velocity $dv$):
$$ds = \frac{v}{\frac{F_t - (mg + F_d)}{m}}dv$$
\
Now, if I were to integrate $ds$ from 0 to a height $h$, it would simply return h. This would be equal to the height climbed as the velocity increased from its current velocity ($v_c$) to its velocity at height $h$ ($v_h$).\
**Therefore**
$$\int_{0}^{h} ds = \int_{v_c}^{v_h} \frac{v}{\frac{F_t - (mg + F_d)}{m}} dv$$
\
Therefore, given the drag curve, thrust curve, and mass curve of the rocket (thrust and mass can easily be substituted by linear functions as they decrease (somewhat) linearly), the apogee of the rocket can be obtained!!! 
