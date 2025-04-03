import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# Constants (in natural units where ħ = 1)
hbar2_over_2m = 20.735  # MeV*fm^2, reduced Planck's constant squared over 2*mass
E_bound = -2.2  # Bound state energy (MeV)
R = 2.1  # fm, radius of the nuclear potential well

# Define the potential well function
def V(r, V0):
    return np.where(r <= R, -V0, 0)

# Schrödinger equation in second-order form
def schrodinger(r, y, V0):
    P, dP = y
    V_r = V(r, V0)
    d2P = (2/hbar2_over_2m) * (V_r - E_bound) * P
    return np.vstack((dP, d2P))

# Boundary conditions: P(0) = 0, P(infinity) -> 0
def bc(ya, yb):
    return np.array([ya[0], yb[0]])

# Discretize the radial domain
r_max = 10  # fm, max radius to consider
r = np.linspace(0.01, r_max, 500)
y_guess = np.zeros((2, r.size))

# Solve for P(r) using boundary value problem solver
V0_guess = 35  # Initial guess for V0 (MeV)
sol = solve_bvp(lambda r, y: schrodinger(r, y, V0_guess), bc, r, y_guess)

# Plot results
plt.figure(figsize=(10, 5))

# Plot wavefunction
plt.subplot(1, 2, 1)
plt.plot(sol.x, sol.y[0], label="Wavefunction P(r)")
plt.xlabel("r (fm)")
plt.ylabel("P(r)")
plt.title("Deuteron Wavefunction Solution")
plt.legend()
plt.grid()

# Plot potential function
plt.subplot(1, 2, 2)
r_vals = np.linspace(0, r_max, 500)
V_vals = V(r_vals, V0_guess)
plt.plot(r_vals, V_vals, label="Potential V(r)", color='r')

# Add the straight line for the energy level from -2.224 MeV to the potential difference for J=1^+
E_1_plus = -3.0  # Example potential difference for J=1^+ state (MeV) -- modify this value as needed
plt.plot(r_vals, np.full_like(r_vals, -2.224), label="Energy Level (-2.224 MeV & J=1^+)", color='b', linestyle='--')


plt.xlabel("r (fm)")
plt.ylabel("V(r) (MeV)")
plt.title("Potential Function V(r)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

