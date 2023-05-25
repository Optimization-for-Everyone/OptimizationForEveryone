import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
f = 0.36
h = 0.0
m = 0.02

# Define the system of equations
def equations(t, variables):
    x, y, v = variables
    dx_dt = f * x - x * v
    dy_dt = x * v - y
    dv_dt = y - m * x * v - h * v
    return [dx_dt, dy_dt, dv_dt]

# Initial conditions
x0 = 0.4
y0 = 0.0
v0 = 0.1

# Time range
t_start = 0.0
t_end = 20.0
num_points = 100

# Time array
t = np.linspace(t_start, t_end, num=num_points)

# Solve the system of equations
sol = solve_ivp(equations, [t_start, t_end], [x0, y0, v0], t_eval=t)

# Extract the solutions
x_values = sol.y[0]
y_values = sol.y[1]
v_values = sol.y[2]

# Plot the solutions
plt.plot(t, x_values, label='x')
plt.plot(t, y_values, label='y')
plt.plot(t, v_values, label='v')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Solution of the Nonlinear Equation System')
plt.show()
