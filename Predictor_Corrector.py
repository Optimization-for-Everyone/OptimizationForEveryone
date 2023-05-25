import numpy as np
import matplotlib.pyplot as plt

def solve_nonlinear_system(f, m, h, x0, y0, v0, dt, num_steps):
    # Initialize arrays to store the solution
    t = np.zeros(num_steps + 1)
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    v = np.zeros(num_steps + 1)

    # Set initial conditions
    t[0] = 0.0
    x[0] = x0
    y[0] = y0
    v[0] = v0

    # Perform time integration using Improved Euler method
    for i in range(num_steps):
        t[i+1] = t[i] + dt

        # Predictor step
        x_pred = (1 + dt * (f - v[i])) * x[i]
        y_pred = (1 - dt) * y[i] + dt * x[i] * v[i]
        v_pred = (1 - dt * (m * x[i] + h)) * v[i] + dt * y[i]

        # Corrector step
        x[i+1] = 0.5 * (x[i] + (1 + dt * (f - v_pred)) * x_pred)
        y[i+1] = 0.5 * (y[i] + (1 - dt) * y_pred + dt * x_pred * v_pred)
        v[i+1] = 0.5 * (v[i] + (1 - dt * (m * x_pred + h)) * v_pred + dt * y_pred)

    print("x: ", x)
    return t, x, y, v

# Constants
f = 0.36
h = 0.0
m = 0.02

# Initial conditions
x0 = 0.4
y0 = 0.0
v0 = 0.1

# Time step size and number of steps
dt = 0.1
num_steps = 200

# Solve the nonlinear system
t, x, y, v = solve_nonlinear_system(f, m, h, x0, y0, v0, dt, num_steps)

# Plot the solutions
plt.plot(t, x, label='x')
plt.plot(t, y, label='y')
plt.plot(t, v, label='v')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Solution of the Nonlinear System')
plt.show()
