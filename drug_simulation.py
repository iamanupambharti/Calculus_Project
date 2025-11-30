import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

A = 15.0   
k = 0.8    
t_end = 10 

def concentration(t):
    return A * t * np.exp(-k * t)

if __name__ == "__main__":
    print(f"Concentration at t=1: {concentration(1):.2f}")

t_values = np.linspace(0, t_end, 500)
c_values = concentration(t_values)

t_peak = 1 / k
c_peak = concentration(t_peak)

auc_value, error = quad(concentration, 0, 6)

print(f"-"*30)
print(f"Calculus Verification:")
print(f"1. Peak Time (Max Concentration): {t_peak:.2f} hours")
print(f"2. Peak Concentration: {c_peak:.2f} mg/L")
print(f"3. Total Drug Exposure (AUC 0-6h): {auc_value:.2f} mg*hr/L")
print(f"-"*30)