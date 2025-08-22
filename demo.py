import numpy as np
import matplotlib.pyplot as plt

# parameters
v0 = 20      # initial velocity (m/s)
g = 9.8      # gravity (m/s^2)
t = np.linspace(0, 2*v0/g, 100)  # time array

# trajectory
y = v0 * t - 0.5 * g * t**2

plt.plot(t, y)
plt.title("Projectile Motion")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.savefig("trajectory.png")  # save image
plt.show()
