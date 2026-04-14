import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

bond_length = np.array([0.5, 0.6, 0.7, 0.74, 0.8, 1.0, 1.5, 2.0])
energy = np.array([-687.584, -721.280, -732.516, -733.377,
                   -732.166, -716.380, -662.238, -620.821])

def morse(r, De, a, re):
    return De * (1 - np.exp(-a * (r - re)))**2

params, _ = curve_fit(morse, bond_length, energy, p0=[100, 1, 0.7])
De, a, re = params

r_fit = np.linspace(min(bond_length), max(bond_length), 200)
E_fit = morse(r_fit, De, a, re)

min_index = np.argmin(energy)
eq_bond_length = bond_length[min_index]
min_energy = energy[min_index]

plt.scatter(bond_length, energy, label="Data Points")
plt.plot(r_fit, E_fit, label="Morse Fit")
plt.scatter(eq_bond_length, min_energy, marker='x', s=100, label="Equilibrium Point")

plt.xlabel("Bond Length (Å)")
plt.ylabel("Energy (kcal/mol)")
plt.title("Potential Energy Surface (PES)")
plt.legend()
plt.grid()

plt.show()

print("=== RESULTS ===")
print(f"Equilibrium Bond Length: {eq_bond_length} Å")
print(f"Minimum Energy: {min_energy} kcal/mol")
print("\nFitted Morse Parameters:")
print(f"De = {De}")
print(f"a  = {a}")
print(f"re = {re}")
