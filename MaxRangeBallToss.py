import numpy as np
import matplotlib.pyplot as plt

def prange(ttheta, v0, r0):
    """
    Calculate the range of a projectile given an angle,
    initial velocity, and initial position

    Parameters:
    - ttheta: Launch angle in radians
    - v0: Initial velocity (m/s)
    - r0: Initial position as a NumPy array [x , y]

    Returns:
    - r[0]: Horizontal displacement when projectile lands (y < 0)
    """
    g = np.array([0, -9.8]) # Acceleration gravity (m/s^2)
    m = 0.05                # Mass (kg)
    p = m * np.array([np.cos(ttheta), np.sin(ttheta)]) # Initial momentum
    t = 0                   # Time (s)
    dt = 0.001              # Time step (s)
    r = np.array(r0, dtype=float) # Position vector

    while r[1] >= 0:
        F = m * g           # Force gravity
        p = p + F * dt      # Update momentum
        r = r + (p * dt) / m # Update position
        t = t + dt          # Update time

    return r[0]

# Initialize parameters
theta = 1 * np.pi / 180       # Start angle (1 degree in radians)
dtheta = 1 * np.pi / 180      # Angle increment (1 degree in radians)
vstart = 7                     # Initial velocity (m/s)

angles_deg = []
ranges = []

# Loop over angles from 1 to 89 degrees
while theta < 89 * np.pi / 180:
    trange = prange(theta, vstart, [0, 2])  # Calculate range
    angles_deg.append(theta * 180 / np.pi)   # Convert to degrees
    ranges.append(trange)                    # Append range
    theta = theta + dtheta                   # Increment angle

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(angles_deg, ranges, 'b-', label='Range vs Angle')
plt.title('Projectile Range vs Launch Angle')
plt.xlabel('Theta [deg]')
plt.ylabel('Range [m]')
plt.grid(True)
plt.legend()
plt.show()



