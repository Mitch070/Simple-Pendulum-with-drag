import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def pendulum(y, t):
    theta, omega = y
    dydt = (omega, -7 * theta)
    return dydt


y0 = [np.pi / 4, 0]
t = np.linspace(1, 10, 101)

sol = odeint(pendulum, y0, t)
plt.plot(t, sol)

plt.plot(t, sol[:, 0], 'a', label='theta(t)')
plt.plot(t, sol[:, 1], 'b', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
