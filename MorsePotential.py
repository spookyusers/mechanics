
# Morse Potential Function

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the symbolic variables and constants
r = sp.Symbol('r')
A, R, S = sp.symbols('A R S')

# Define the Morse Potential
U_r = A * ((sp.exp((R-r) / S) - 1)**2 - 1)

# Generate a lambda function for numerical evaluation
U_r_lambdified = sp.lambdify(r, U_r.subs({A: 1, R: 1, S: 1}), 'numpy')

# Create an array of r values
r_vals = np.linspace(0.5, 3, 400)

# Compute U(r) for each value r
U_vals = U_r_lambdified(r_vals)

# Plot the function
plt.plot(r_vals, U_vals)
plt.xlabel('r (distance between atoms)')
plt.ylabel('U(r) (potential energy)')
plt.title('Morse Potential')
plt.grid(True)
plt.show()


