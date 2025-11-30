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

plt.figure(figsize=(10, 6))

plt.plot(t_values, c_values, label=r'$C(t) = 15te^{-0.8t}$', color='blue', linewidth=2)

plt.plot(t_peak, c_peak, 'ro', label=f'Peak ({t_peak:.2f}h, {c_peak:.2f} mg/L)')
plt.vlines(t_peak, 0, c_peak, linestyles='dashed', colors='red', alpha=0.5)

t_fill = np.linspace(0, 6, 100)
plt.fill_between(t_fill, concentration(t_fill), color='skyblue', alpha=0.4, label=f'AUC (0-6h) = {auc_value:.2f}')

plt.title('Pharmacokinetics: Drug Concentration Over Time', fontsize=14)
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Concentration (mg/L)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig('concentration_graph.png')
print("Graph saved as 'concentration_graph.png'")

plt.show()