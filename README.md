# Welcome!!!!
This is a simple tool for projecting the apogee of a rocket using its drag curve data. I used [this lovely package by Chasmani](https://github.com/chasmani/piecewise-regression) to segment the drag curve into much more digestable straight lines. My next step is to phase out the use of this plugin in order to speed up the calculations. 

Right now, the parameters are all over the place (sorry!!!) You should be able to change the number of regressions (n) on line 27, the mass of the rocket (m) on line 56, and the height of burnout (height_at_burnout) on line 81. Also, make sure the velocities of your rocket are in the first collumn of your .csv file in a collumn titled Velocities, and your corresponding drag forces are in the second collumn titled Drag.

## Superduper Boring Mathy Explaination
The formulae used throughout this tool were derrived through good ole calculus!
In this particular instance, I ignored any forces on the rocket besides the gravitational and drag forces.
**Therefore:**
$$\left( \sum_{} F_n \right) = -(mg) - F_d$$

And since the equation for drag force ($F_d$) **is given by:**
$$\frac{1}{2} \rho v^2 A C_d$$
