import csv
import matplotlib.pyplot as plt

filename = open('Final_Diemos_Drag_and_Thrust_Data.csv', 'r')
file = csv.DictReader(filename)

velocities = []
drag_forces = []
thrust_forces = []
masses = []

for col in file:
    velocities.append(col['Velocity'])
    drag_forces.append(col['Drag'])
    thrust_forces.append(col['Thrust'])
    masses.append(col['Mass'])

#convert data to floats and store these floats in x and y lists
v = []
Fd = []
Ft = []
m = []
for i in range(len(velocities)):
    v.append(float(velocities[i]))
    Fd.append(float(drag_forces[i]))
    Ft.append(float(thrust_forces[i]))
    m.append(float(masses[i]))

y = []

i = 0
h = 0
g = 9.81
while v[i] > 0:
    coefficient_one = (m[i]*(v[i]**2))/(2*(Ft[i]-((m[i]*g)+Fd[i])))
    coefficient_two = (m[i]*(v[i+1]**2))/(2*(Ft[i]-((m[i]*g)+Fd[i])))
    h += (coefficient_two - coefficient_one)
    y.append(h)
    i += 1

x = list(range(i))
print(i)
print(h)
plt.plot(x, y)
plt.show()
