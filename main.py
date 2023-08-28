#imports
import piecewise_regression
import csv
import matplotlib.pyplot as plt

#Gather data from the csv file into two lists
#This data is from the team's last successful launch, Big Blue, which has a projected apogee of 1636m
#The data is from simulated conditions in which there exists 0 wind
filename = open('big_blue_drag_curve_data.csv', 'r')
file = csv.DictReader(filename)
 
velocities = []
drag_forces = []

for col in file:
    velocities.append(col['Velocity'])
    drag_forces.append(col['Drag'])

#convert data to floats and store these floats in x and y lists
x = []
y = []
for i in range(len(velocities)):
    x.append(float(velocities[i]))
    y.append(float(drag_forces[i]))

#n is the number of breakpoints
n = 15

#perform the regression and display data
pw_fit = piecewise_regression.Fit(x, y, n_breakpoints=n)
pw_fit.summary()

#returns library with all the data of the lines including their startpoints and slopes!!!!!!
estimates = pw_fit.get_results()

n+=1
#find the velocity at the next breakpoint
def calculate_next_velocity(current_velocity, x):
    i = 'alpha'+str(n-x)
    k = estimates['estimates'][i]['estimate']
    x += 1
    if (n-x) > 0:
        z = 'breakpoint'+str(n - x)
        next_velocity = estimates['estimates'][z]['estimate']
    else:
        next_velocity = 0
    return [next_velocity, k, x]

#calculate the incremental increase in height from the current velocity until the velocity at the next breakpoint
def calculate_height(current_velocity, x, current_drag):
    next_vel_calc = calculate_next_velocity(current_velocity, x)
    vn = next_vel_calc[0] #m/s
    k = next_vel_calc[1] #slope of the current regression line
    vc = current_velocity #m/s
    g = 9.81 #acceleration due to gravity (m * s^-2)
    m = 8.47 #mass of the rocket (kg)
    next_drag = calculate_next_drag(current_drag, k, vc, vn)
    coefficient_current = -1*((m*(vc**2))/(2*((g*m)+current_drag)))
    coefficient_new = -1*((m*(vn**2))/(2*((g*m)+current_drag)))
    height = coefficient_new - coefficient_current
    print(height)
    return [height, next_drag]

def calculate_next_drag(current_drag, current_slope, current_velocity, next_velocity):
    next_drag = current_drag - (current_slope*(current_velocity - next_velocity))
    return next_drag

def calculate_apogee(current_velocity, height, x, current_drag):
    calc = calculate_height(current_velocity, x, current_drag)
    height += calc[0]
    current_velocity = calculate_next_velocity(current_velocity, x)[0]
    next_drag = calc[1]
    if current_velocity > 0:
        return calculate_apogee(current_velocity, height, x+1, next_drag)
    else:
        return height

#run the thing
initial_velocity = x[0] #m/s
initial_drag = y[0]
height_at_burnout = 400
apogee = calculate_apogee(initial_velocity, height_at_burnout, 0, initial_drag)
print("Projected Apogee: " + str(round(apogee, 2)) + "m")

# Plot the data, fit, breakpoints and confidence intervals
pw_fit.plot_data(color="grey", s=20)
# Pass in standard matplotlib keywords to control any of the plots
pw_fit.plot_fit(color="red", linewidth=4)
pw_fit.plot_breakpoints()
pw_fit.plot_breakpoint_confidence_intervals()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.close()
