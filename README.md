# Deuteron Wavefunction Solver

## Overview
This project numerically solves the Schrödinger equation for a bound-state problem using the shooting method with a boundary value problem solver (`solve_bvp`). The deuteron, a bound state of a proton and neutron, is modeled inside a finite square well potential.

## Features
- Implements the Schrödinger equation in natural units (MeV, fm).
- Uses the `solve_bvp` function from SciPy to compute the wavefunction.
- Plots both the wavefunction and the potential well.
- Compares computed results with the known bound state energy of the deuteron (-2.224 MeV).

## Requirements
Ensure you have Python installed along with the following dependencies:
```bash
pip install numpy matplotlib scipy
```

## Usage
Run the Python script to solve the Schrödinger equation and visualize the results:
```bash
python deuteron_solver.py
```

## Code Explanation
- **Potential Function `V(r, V0)`**: Defines a square well with depth `V0`.
- **Schrödinger Equation `schrodinger(r, y, V0)`**: Second-order differential equation for the wavefunction.
- **Boundary Conditions `bc(ya, yb)`**: Ensures the wavefunction satisfies physical constraints.
- **Numerical Solution**: Uses `solve_bvp` to find the eigenfunction for a given potential depth `V0`.
- **Plotting Results**: Visualizes the wavefunction and potential.

## Future Improvements
- Implement an adaptive solver for dynamically adjusting `V0`.
- Improve boundary conditions to ensure a more accurate tail behavior.
- Extend to include other nuclear potentials (e.g., Yukawa potential).

## License
This project is released under the MIT License.

