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