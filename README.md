#  Potential Energy Surface Visualizer

##  Overview
This project visualizes and models the **Potential Energy Surface (PES)** of a diatomic molecule using numerical data. It fits the data to a physically meaningful model and extracts key molecular properties such as equilibrium bond length.

---

##  Theory

###  Potential Energy Surface 
A **Potential Energy Surface** describes how the energy of a molecular system varies with changes in geometry.

For a diatomic molecule:
- **X-axis:** Bond length (Å)  
- **Y-axis:** Energy (kcal/mol)  

The minimum point on the curve represents:
- Stable molecular configuration  
- Equilibrium bond length  

---

###  Morse Potential
The Morse potential is a realistic model used to describe bond stretching:

<img width="251" height="52" alt="image" src="https://github.com/user-attachments/assets/c2d4a362-b626-44a0-bc32-9f1ca31de5d9" />


Where:
- **De** → Dissociation energy  
- **re** → Equilibrium bond length  
- **a** → Controls the width of the potential well  

Unlike the harmonic oscillator model, the Morse potential accounts for:
- Bond breaking  
- Anharmonic behavior  

---

##  Features
- Plot energy vs bond length  
- Fit data using Morse potential  
- Detect equilibrium bond length  
- Visualize results clearly  

---

##  Requirements

Install dependencies:

```bash
pip install numpy matplotlib scipy
```
---

## Author 
Made by me \\(^0^)/
